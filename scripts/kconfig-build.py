
Import("env")
Import("projenv")
import os
global_env = DefaultEnvironment()

# First, get our variables from the environment
this_dir = os.path.join(env.subst('$PROJECT_LIBDEPS_DIR'), env.subst('$PIOENV'), 
                        "Robusto-PlatformIO", "scripts")
project_dir = env.subst('$PROJECT_DIR')
pio_env = env.subst('$PIOENV')
build_dir = os.path.join(env.subst('$BUILD_DIR'), "config")
framework = projenv.subst('$PIOFRAMEWORK')
Kconfig_filename = os.path.join(project_dir, "Kconfig.{0}".format(pio_env))
config_filename = os.path.join(project_dir, ".config.{0}".format(pio_env))
targets = env.get("__PIO_TARGETS") 
#print("--------------------------------------------------")
#print(env)
#print("--------------------------------------------------")
print("Build dir: ", build_dir)
print("Script dir: ", this_dir)
print("Environment: ", pio_env)
print("Framework: ", framework)
print("Kconfig_filename: ", Kconfig_filename)
print('kconfig_src_filename:', config_filename) 
if not os.path.exists(build_dir):
  # Create the build folder
  print("Create the build folder: {0}".format(build_dir))
  os.makedirs(build_dir)


if os.path.isfile(config_filename):
    os.environ["KCONFIG_CONFIG"] = config_filename
    build_dir = os.path.join(project_dir, ".pio", "build", pio_env)
    gen_command = "genconfig {0} --header-path {1}".format(Kconfig_filename, os.path.join(build_dir, "config", "robconfig_.h"))
    print("gen_command: ", gen_command)
    os.system(gen_command)


if  framework.lower() != "espidf":
    print(" --Add menu item---")
    curr_env = env.subst('$PIOENV')
    curr_dir = os.path.join(env.subst('$PROJECT_LIBDEPS_DIR'), curr_env, "Robusto-PlatformIO", "scripts")

    menuconfig_cmd = "python {0} {1} ".format(
        os.path.join(curr_dir, "run_menuconfig.py"),curr_env
        )
    print("Adding target, command: {0}".format(menuconfig_cmd))
    global_env.AddTarget(
        name="menuconfig",
        dependencies=None,
        group="General",
        actions=[
            menuconfig_cmd
        ],
        title="Run menuconfig",
        description="Menuconfig is a tool for configuring an environment"
    )

#env.AddPreAction("buildprog", add_menu)

