import os

import sys
import subprocess
project_dir =os.getcwd()
# First, get our variables from the environment
pio_env = sys.argv[1]
print("Environment: ", pio_env)
run_path = os.path.dirname(sys.argv[0])
print("Run path: ", run_path)
print("Project dir: ", project_dir)
Kconfig_filename = os.path.join(project_dir, "Kconfig.{0}".format(pio_env))
print("Kconfig_filename: ", Kconfig_filename)

# Create the base for the files (TOOD: Can you pipe a stream to Kconfig, perhaps?)
file = open(Kconfig_filename, "w")
file.write("orsource \"" + os.path.join("components", "**", "Kconfig") + "\"\n")
file.write("orsource \"" + os.path.join("components", "**", "Kconfig.projbuild") + "\"\n")
file.write("orsource \"" + os.path.join(".pio", "libdeps", pio_env, "**", "Kconfig") + "\"\n")
file.write("orsource \"" + os.path.join(".pio", "libdeps", pio_env, "**", "Kconfig.projbuild") + "\"\n")
file.close()

config_filename = os.path.join(project_dir, ".config.{0}".format(pio_env))
print("Running menuconfig on ", Kconfig_filename, " save at ", config_filename)
# Create an environment for the process
env_kconfig = {}
env_kconfig.update(os.environ)
env_kconfig.update({"KCONFIG_CONFIG": config_filename})
# Call menuconfig to configure a specified file
subprocess.run(["menuconfig", Kconfig_filename], cwd=project_dir, env=env_kconfig, start_new_session=False)
