import os
import subprocess
cmd = os.environ["PIO_PYTHON_EXE"]
param =os.path.join(os.environ["PWD"], "scripts", "post-install.py")
print("Run the PIO Python:" + cmd + " " + param)
returned_value = subprocess.call([cmd, param])
if returned_value != 0:
    exit(returned_value)