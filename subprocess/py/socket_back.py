

# luis arandas 24-07-2022 # based on matthew ragan's code
# subprocess get output from sockets

import subprocess
import os

# point to our script that we're going to execute

port = str(op('udpin1').par.port.val)

interval = '1'
loop = '15'

current_dir = str(os.getcwd())
print(current_dir)

cmd_python_script = current_dir + os.sep + "py" + os.sep + "extern2_py.py" # '{}/scripts/cmd_line_python.py'.format(project.folder)

# print our script path - quick debug
print(cmd_python_script)

# clear the last entries from the UDPin DAT
op('udpin1').par.clear.pulse()

# construct a list of our python args - which python and which script
python_args = ['python', cmd_python_script]

# construct a list of arguments for out external script
script_args = ['-p', port, '-i', interval, '-l', loop]

# join our two lists - python args and scirpt args
cmd_args = python_args + script_args

# call our script with subprocess
subprocess.Popen(cmd_args, shell=True)