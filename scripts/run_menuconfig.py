
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
config_filename = os.path.join(project_dir, ".config.{0}".format(pio_env))
print('kconfig_src_filename:', config_filename) 

# Create the base for the files (TOOD: Can you pipe a stream to Kconfig, perhaps?)
file = open(Kconfig_filename, "w")
# TODO: We probably need more sources here
file.write("orsource \"components/**/Kconfig.projbuild\"\n")
file.write("orsource \".pio/libdeps/" + pio_env + "/**/Kconfig.projbuild\"\n")
file.write("orsource \"examples/src/Kconfig.projbuild\"\n")
file.close()


print("Running menuconfig on ", Kconfig_filename, " save at ", config_filename)
# Create an environment for the process
env_kconfig = {}
env_kconfig.update(os.environ)
env_kconfig.update({"KCONFIG_CONFIG": config_filename})

#if not os.path.isfile(config_filename):
#    print("Create minimal config at: ", Kconfig_filename)
#    subprocess.run(["savedefconfig", "--kconfig", Kconfig_filename, "--out", config_filename], cwd=project_dir, env=env_kconfig, start_new_session=False)

#if not os.path.isfile(config_filename):
#    print("Create minimal config with defaults: ", config_filename)
#    subprocess.run(["defconfig", config_filename, "--kconfig", Kconfig_filename], cwd=project_dir, env=env_kconfig, start_new_session=False)

# Call menuconfig to configure a specified file
subprocess.run(["menuconfig", Kconfig_filename], cwd=project_dir, env=env_kconfig, start_new_session=False)

if os.path.isfile(config_filename):
    os.environ["KCONFIG_CONFIG"] = config_filename
    build_dir = os.path.join(project_dir, ".pio", "build", pio_env)
    gen_command = "genconfig {0} --header-path {1}".format(Kconfig_filename, os.path.join(build_dir, "config", "robconfig_.h"))
    print("gen_command: ", gen_command)
    os.system(gen_command)
