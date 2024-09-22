
# Make the GLSL grid from the number of files in folder
# 22-09-2024 luisarandas

from typing import List, Optional
from pathlib import Path

def check_files_in_directory(directory_path: str) -> Optional[List[str]]:
    """
    Checks and lists all files in the specified directory.

    Args:
        directory_path (str): The path to the directory to check.

    Returns:
        Optional[List[str]]: A list of file names in the directory, or None if an error occurs.
    """
    try:
        path = Path(directory_path)
        if not path.exists():
            print(f"Error: The directory '{directory_path}' does not exist.")
            return None
        if not path.is_dir():
            print(f"Error: The path '{directory_path}' is not a directory.")
            return None

        files = [f.name for f in path.iterdir() if f.is_file()]
        
        if not files:
            print(f"No files found in directory '{directory_path}'.")
        else:
            print(f"Found {len(files)} files in '{directory_path}':")
            for file in files:
                print(f" - {file}")
        
        return files

    except Exception as e:
        print(f"An error occurred while accessing the directory: {e}")
        return None

def update_touchdesigner_op(op_name: str, value: int) -> None:
    """
    Updates a TouchDesigner operator with a given value.

    Args:
        op_name (str): The name of the TouchDesigner operator.
        value (int): The value to set.
    """
    try:
        op(op_name).par.value0 = value
        print(f"Updated {op_name} with value: {value}")
    except Exception as e:
        print(f"Failed to update TouchDesigner operator '{op_name}': {e}")

def update_grid_uniforms(new_size):
    """
    Updates the GLSL TOP's input_audio_files uniform.

    Parameters:
        new_size (int): The new grid size to set.
    """
    # Reference to the GLSL TOP (replace 'RandomGridGLSL' with your GLSL TOP's actual name)
    glsl_top = op('GridGLSL')  # Ensure this path is correct

    if glsl_top is None:
        print("Error: GLSL TOP 'RandomGridGLSL' not found.")
        return

    # Clamp the new_size to a reasonable range
    new_size = max(1, min(new_size, 20))  # Ensures new_size is between 1 and 20

    # Update the 'input_audio_files' uniform
    glsl_top.par.input_audio_files = new_size

    print(f"Updated GLSL TOP uniforms: input_audio_files = {new_size}")



# Main execution

input_directory_str = str(op('input_directory_null')[0,1].val)
directory = input_directory_str
files = check_files_in_directory(directory)


if files is not None:
    file_count = len(files)
    update_touchdesigner_op('number_of_files', file_count)
    
    print(f"Total number of files: {file_count}")
    
    # Optional: Process files
    print("\nProcessing files:")
    for file in files:
        # Replace this with your desired file processing logic
        print(f"Processing {file}")

