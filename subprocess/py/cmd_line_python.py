

# luis arandas 24-07-2022 # based on matthew ragan's code
# subprocess execute command line

import subprocess
import os
# point to our script that we're going to execute

current_dir = str(os.getcwd())
print(current_dir)

cmd_python_script = current_dir + os.sep + "py" + os.sep + "extern_py.py" # '{}/scripts/cmd_line_python.py'.format(project.folder)
 
# quick debug print
print(cmd_python_script)

# var for custom python lib python_exe = 'C:/Program Files/Python35/python.exe'
# call our script with subprocess
# subprocess.Popen(['python', cmd_python_script], shell=False)

# construct a list of arguments for out external script
script_args = ['-i', 'Hello', '-i2', 'TouchDesigner']
 
# join our python instructions with our scirpt args
command_list = ['python', cmd_python_script] + script_args
 
# call our script with subprocess
subprocess.Popen(command_list, shell=False)



"""

# this should take a long time in touchdesigner to execute

-------------

import time
import sys
 
# a variable a divider that we're going to use
divider = '- ' * 10
 
# a for loop to print all of the paths in our sys.path
for each in sys.path:
    print(each)
 
# our divider
print(divider)
 
# a for loop that prints numbers 
for each in range(10):
    print(each)
 
# a call to time.sleep to keep our terminal open so we can see what's happening
time.sleep(120)

-------------

"""