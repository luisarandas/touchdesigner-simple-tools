# 02-04-2024 luisarandas
# Useful set of functions to deal with OS (tested: Windows 11)
import os
import winreg


def list_registry_keys_values(hive, key_path):
    output = f"\nListing registry keys and values under: {key_path}\n"
    try:
        with winreg.OpenKey(hive, key_path, 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY) as key:
            i = 0
            while True:
                try:
                    subkey_name = winreg.EnumKey(key, i)
                    output += f"Subkey: {subkey_name}\n"
                    i += 1
                except OSError:
                    break

            j = 0
            while True:
                try:
                    value_name, value_data, value_type = winreg.EnumValue(key, j)
                    output += f"Value: {value_name}, Data: {value_data}, Type: {value_type}\n"
                    j += 1
                except OSError:
                    break
    except FileNotFoundError:
        output += f"Key not found: {key_path}\n"
    return output



def search_for_key_in_registry_list(hive, key_path, search_term):
    result = ""
    try:
        with winreg.OpenKey(hive, key_path, 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY) as key:
            i = 0
            while True:
                try:
                    subkey_name = winreg.EnumKey(key, i)
                    full_subkey_path = os.path.join(key_path, subkey_name)
                    if search_term.lower() in subkey_name.lower():
                        result += list_registry_keys_values(hive, full_subkey_path)
                    # Recurse into subkey
                    result += search_for_key_in_registry_list(hive, full_subkey_path, search_term)
                    i += 1
                except OSError:
                    break
    except FileNotFoundError:
        pass  # Simply pass if a key is not found
    return result



def find_touchdesigner_exe(base_dirs=None):
    if base_dirs is None:
        base_dirs = [
            os.environ.get("PROGRAMFILES", "C:\\Program Files"),
            os.environ.get("PROGRAMFILES(X86)", "C:\\Program Files (x86)")
        ]
    for base_dir in base_dirs:
        derivative_path = os.path.join(base_dir, "Derivative")
        if os.path.exists(derivative_path) and os.path.isdir(derivative_path):
            for item in os.listdir(derivative_path):
                if "TouchDesigner" in item:
                    touchdesigner_path = os.path.join(derivative_path, item, "bin", "TouchDesigner.exe")
                    if os.path.exists(touchdesigner_path):
                        return touchdesigner_path
    return "TouchDesigner executable not found."




# PRINT VSTS IN PROGRAM FILES /COMMON FILES

def main():
    print("Utilities for TouchDesigner Scripts")
    # td_path = find_touchdesigner_exe()
    # print(td_path)
    # list_registry_keys_values(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\")
    # search_results = search_for_key_in_registry_list(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE", "Derivative")
    # print(search_results)


if __name__ == "__main__":
    main()

