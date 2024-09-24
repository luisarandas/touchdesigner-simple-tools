# 12-09-2024 luisarandas
# parser from Resolume-exported XML files into TouchDesigner operators

# Specifically, we need to look for the <BezierWarper> data within each <Slice>
# This file parses the XML into variables we can access on op('get_xml_data')
# e.g. $ x = mod.get_xml_data.COMPOSITION_SIZE


import xml.etree.ElementTree as ET
import os

# Global variables
global COMPOSITION_SIZE, LEFT_SCREEN, RIGHT_SCREEN

def parse_resolume_xml(file_path):
    global COMPOSITION_SIZE, LEFT_SCREEN, RIGHT_SCREEN
    
    if not os.path.exists(file_path):
        return f"Error: File not found at {file_path}"

    tree = ET.parse(file_path)
    root = tree.getroot()

    composition_size = root.find(".//CurrentCompositionTextureSize")
    width = int(composition_size.get('width'))
    height = int(composition_size.get('height'))
    COMPOSITION_SIZE = (width, height)

    screens = {}
    for screen in root.findall(".//Screen"):
        screen_name = screen.get('name')
        screen_data = {
            'name': screen_name,
            'slices': []
        }
        for slice in screen.findall(".//Slice"):
            input_rect = slice.find("InputRect")
            output_rect = slice.find("OutputRect")
            bezier_warper = slice.find(".//BezierWarper")

            input_points = [tuple(map(float, v.attrib.values())) for v in input_rect.findall('v')]
            output_points = [tuple(map(float, v.attrib.values())) for v in output_rect.findall('v')]

            control_width = int(bezier_warper.get('controlWidth'))
            control_height = int(bezier_warper.get('controlHeight'))
            warp_points = [tuple(map(float, v.attrib.values())) for v in bezier_warper.find('vertices').findall('v')]

            slice_data = {
                'input_rect': input_points,
                'output_rect': output_points,
                'warp_grid': {
                    'width': control_width,
                    'height': control_height,
                    'points': warp_points
                }
            }
            screen_data['slices'].append(slice_data)
        screens[screen_name] = screen_data

    LEFT_SCREEN = screens.get('LEFT', {})
    RIGHT_SCREEN = screens.get('RIGHT', {})

    return {
        'composition_size': COMPOSITION_SIZE,
        'screens': list(screens.values())
    }

def print_resolume_info():
    print("Resolume Composition Information:")
    print(f"Composition Size: {COMPOSITION_SIZE[0]}x{COMPOSITION_SIZE[1]}")
    print("\nScreens:")
    for screen in [LEFT_SCREEN, RIGHT_SCREEN]:
        if screen:
            print(f"\n  Screen: {screen['name']}")
            for i, slice in enumerate(screen['slices']):
                print(f"    Slice {i+1}:")
                print(f"      Input Rectangle: {slice['input_rect']}")
                print(f"      Output Rectangle: {slice['output_rect']}")
                print(f"      Warp Grid:")
                print(f"        Width: {slice['warp_grid']['width']}")
                print(f"        Height: {slice['warp_grid']['height']}")
                print(f"        Total Points: {len(slice['warp_grid']['points'])}")
                print(f"        First Few Points: {slice['warp_grid']['points'][:5]}...")



def fill_resolume_table(table_op):
    # Clear the existing table
    table_op.clear()
    # Add header row
    headers = ['Screen', 'Slice', 'Data Type', 'Value']
    table_op.appendRow(headers)
    # Add composition size
    table_op.appendRow(['Composition', '', 'Size', f"{COMPOSITION_SIZE[0]}x{COMPOSITION_SIZE[1]}"])
    # Function to add rows for a screen
    def add_screen_data(screen_data, screen_name):
        for i, slice in enumerate(screen_data['slices']):
            # Input Rectangle
            table_op.appendRow([screen_name, f'Slice {i+1}', 'Input Rectangle', str(slice['input_rect'])])
            # Output Rectangle
            table_op.appendRow([screen_name, f'Slice {i+1}', 'Output Rectangle', str(slice['output_rect'])])
            # Warp Grid Width
            table_op.appendRow([screen_name, f'Slice {i+1}', 'Warp Grid Width', str(slice['warp_grid']['width'])])
            # Warp Grid Height
            table_op.appendRow([screen_name, f'Slice {i+1}', 'Warp Grid Height', str(slice['warp_grid']['height'])])
            # Warp Grid Points
            for j, point in enumerate(slice['warp_grid']['points']):
                table_op.appendRow([screen_name, f'Slice {i+1}', f'Warp Point {j}', str(point)])

    # Add data for LEFT_SCREEN
    if LEFT_SCREEN:
        add_screen_data(LEFT_SCREEN, 'LEFT')
    # Add data for RIGHT_SCREEN
    if RIGHT_SCREEN:
        add_screen_data(RIGHT_SCREEN, 'RIGHT')





# Main execution

file_path = 'example-resolume-export.XML'
parsed_data = parse_resolume_xml(file_path)

if isinstance(parsed_data, str):  # Error occurred
    print(parsed_data)
else:
    print_resolume_info()


# COMPOSITION_SIZE : Defined in Resolume 'Composition Size' and 'Virtual Output'
# (In Resolume each composition has multiple layers)
# LEFT_SCREEN : Named "LEFT" as the 1st layer
# RIGHT_SCREEN : Named "RIGHT" as the 2nd layer

print("\nAccessing global variables:")
print(f"Composition size: {COMPOSITION_SIZE}")

print(f"LEFT screen input rectangle: {LEFT_SCREEN['slices'][0]['input_rect']}")
print(f"RIGHT screen input rectangle: {RIGHT_SCREEN['slices'][0]['input_rect']}")

print(f"LEFT screen warp grid width: {LEFT_SCREEN['slices'][0]['warp_grid']['width']}")
print(f"RIGHT screen warp grid width: {RIGHT_SCREEN['slices'][0]['warp_grid']['width']}")


resolume_table = op('ResolumeTable')
if resolume_table:
    fill_resolume_table(resolume_table)
    print("ResolumeTable has been updated with parsed data.")
else:
    print("Error: ResolumeTable not found.")