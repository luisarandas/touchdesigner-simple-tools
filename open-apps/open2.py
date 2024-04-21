# luisarandas 21-04-2024
import os
import subprocess

def get_app_name_from_operator(_operator):
    app_name = str(_operator.par.Value0)
    if app_name:
        return find_and_open_application(app_name)
    else:
        print("No application name provided in the operator parameter.")
        return False

def find_and_open_application(app_name):
    app_name = app_name if app_name.lower().endswith(".exe") else f"{app_name}.exe"
    executables = op('search_app_paths').fetch('executables', {})
    for full_path, folder in executables.items():
        file_name = os.path.basename(full_path)
        if file_name.lower() == app_name.lower():
            try:
                subprocess.Popen([full_path], close_fds=True)
                print(f"Successfully launched {app_name} from {folder}")
                return True
            except Exception as e:
                print(f"Failed to launch {app_name} from {folder}: {str(e)}")
                return False

    print(f"{app_name} not found.")
    return False

app_name_str = get_app_name_from_operator(op('app_name'))
print("return: ", app_name_str)
