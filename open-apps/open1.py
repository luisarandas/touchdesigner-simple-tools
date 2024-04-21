# luisarandas 21-04-2024
import os
import threading

executables = {}

def thread_function(name):
    print(f"Thread {name}: starting")
    global executables
    common_paths = [
        "C:\\Program Files",
        "C:\\Program Files (x86)",
        os.path.expanduser("~\\AppData\\Local\\Programs"),
    ]    
    for base_path in common_paths: # only first level
        try:
            entries = os.listdir(base_path)
            top_level_folders = [entry for entry in entries if os.path.isdir(os.path.join(base_path, entry))]
            for folder in top_level_folders:
                folder_path = os.path.join(base_path, folder)
                try:
                    folder_entries = os.listdir(folder_path)
                    exe_files = [file for file in folder_entries if file.lower().endswith('.exe')]
                    for exe in exe_files:
                        full_path = os.path.join(folder_path, exe)
                        executables[full_path] = folder
                except Exception as e:
                    print(f"Error accessing {folder_path}: {str(e)}")
        except PermissionError:
            print(f"Permission denied: Unable to access {base_path}")
        except FileNotFoundError:
            print(f"File not found: {base_path} does not exist or is not accessible")
        except Exception as e:
            print(f"Error accessing {base_path}: {str(e)}")

    print(f"Thread {name}: finishing with {len(executables)} executables found.")
    for path, folder in executables.items():
        print(f"{path} in {folder}")


def onOffToOn(panelValue):
    print("Main: before creating thread")
    th = threading.Thread(target=thread_function, args=(1,))
    print("Main: before running thread")
    th.start()
    print("Main: waiting for the thread to finish")
    th.join()
    print("Main: all done")
    op("search_app_paths").store("executables", executables)
    print("Updated storage")


def whileOn(panelValue):
	return

def onOnToOff(panelValue):
	return

def whileOff(panelValue):
	return

def onValueChange(panelValue):
	return

