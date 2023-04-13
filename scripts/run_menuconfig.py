import os

import sys
import subprocess
cwd =os.getcwd()
# First, get our variables from the environment
pio_env = sys.argv[1]
template_filename = os.path.join(cwd, "scripts", "Kconfig.{0}".format(pio_env)))
file = open(template_file, "w")
file.write(os.path.join("components", "**", "Kconfig"))
file.write(os.path.join("components", "**", "Kconfig.projbuild"))
file.write(os.path.join(".pio", "libdeps", pio_env, "**", "Kconfig"))
file.write(os.path.join(".pio", "libdeps", pio_env, "**", "Kconfig.projbuild"))
file.close()

# Todo
config_filename = os.path.join(cwd, "scripts", "Kconfig.{0}".format(pio_env)))
subprocess.call("menuconfig", env={"KCONFIG_CONFIG": config_filename}, args=["Kconfig.{0}".format(pio_env)])
