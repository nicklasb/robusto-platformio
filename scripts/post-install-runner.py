import os
import subprocess
cmd = os.environ["PIO_PYTHON_EXE"] + " " + os.path.join(os.environ["PWD"], "post-install.py")
print("Run the PIO Python:" + cmd)
returned_value = subprocess.call(cmd)
if returned_value != 0:
    exit(returned_value)