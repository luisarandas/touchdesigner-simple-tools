
# luis arandas 02-04-2024
# get current installed libraries on the env this is being called from

import subprocess
import os

def execute_pair_file():
    python_executable = os.environ.get('MY_PYTHON', 'python')  # Default to 'python'
    toe_directory = project.folder
    path_to_script = os.path.join(toe_directory, "test_udp.py") 
    command_list = [python_executable, path_to_script]
    # Create a STARTUPINFO structure to specify that the subprocess window is not created
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    try:
        result = subprocess.run(command_list, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=toe_directory, startupinfo=startupinfo)
        print("Output from test_udp.py:")
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error calling test_udp.py: {e}")
    print("Command executed:", command_list)

execute_pair_file()

