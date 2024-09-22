# Script to return the current area being hovered on the Slider2D Map
# 22-09-2024 luisarandas

def onOffToOn(channel, sampleIndex, val, prev):
	return

def whileOn(channel, sampleIndex, val, prev):
	return

def onOnToOff(channel, sampleIndex, val, prev):
	return

def whileOff(channel, sampleIndex, val, prev):
	return



def onValueChange(channel, sampleIndex, val, prev):
    # Get the current slider values
    x = float(op('slider_values')['v1'])
    y = float(op('slider_values')['v2'])

    # Number of divisions (you can change this or make it dynamic)
    n = int(op('number_of_files').par.value0)
    # Ensure n is at least 1
    n = max(n, 1)
    
    # Compute the number of rows and columns (matching GLSL logic)
    sqrt_n = n ** 0.5
    rows = int(sqrt_n)
    if rows < 1:
        rows = 1
    cols = int((n + rows - 1) // rows)  # Equivalent to ceil(n / rows)
    
    # Calculate the size of each grid cell
    cell_width = 1.0 / cols
    cell_height = 1.0 / rows
    
    # Determine the current column and row indices
    col = int(x / cell_width)
    row = int(y / cell_height)
    
    # Clamp indices to ensure they are within grid bounds
    col = max(0, min(col, cols - 1))
    row = max(0, min(row, rows - 1))
    
    # Calculate the cell index (matching GLSL indexing)
    cell_index = row * cols + col
    
    # Print the results
    print("Slider Position: X = {}, Y = {}".format(x, y))
    print("Grid Size: {} rows x {} columns".format(rows, cols))
    print("Cell Position: Row {}, Column {}".format(row, col))
    print("Cell Index: {}".format(cell_index))
    
    # Check if the cell is valid (within the number of audio files)
    if cell_index < n:
        print("Valid cell: File to call {}".format(cell_index + 1))
    else:
        print("Invalid cell: Outside the range of files")
    
    return

