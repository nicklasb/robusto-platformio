
Import("env")

import os
global_env = DefaultEnvironment()
# First, get our variables from the environment
this_dir = os.path.join(global_env.subst('$PROJECT_LIBDEPS_DIR'), global_env.subst('$PIOENV'), 
                        "Robusto-PlatformIO", "scripts")
project_dir = global_env.subst('$PROJECT_DIR')
pio_env = global_env.subst('$PIOENV')
build_dir = os.path.join(global_env.subst('$BUILD_DIR'), "config")
framework = global_env.subst('$PIOFRAMEWORK')

print("Build dir: ", build_dir)
print("Script dir: ", this_dir)
print("environment: ", pio_env)
print("framework: ", framework)
# Create the build folder
print("mkdir -p {0}".format(build_dir))
os.system("mkdir -p {0}".format(build_dir))

# Copy the include to there
copy_include_cmd = "cp {0} {1} ".format(os.path.join(this_dir, "robconfig.h"), build_dir)
print(copy_include_cmd)
os.system(copy_include_cmd)


# If its not ESP-IDF, we add the settings header anyway so that the framework and applications don't have to care.
if framework != "espidf":
    # Check if there is anything for us to do here. TODO: Create the file if it is missing? Default configs?
    kconfig_filename = os.path.join(project_dir, "Kconfig." + pio_env)
    if os.path.isfile(kconfig_filename):
        # Generate the config
        gen_command = "KCONFIG_CONFIG=.config.{0} genconfig {1} --header-path {2}".format(pio_env, kconfig_filename, os.path.join(build_dir, "robconfig_.h"))
        print(gen_command)
        os.system(gen_command)
    else: 
        print("Won't do any config, no", kconfig_filename, " file.")  
else: 
    print("Skipping ESP-IDF framework, it has its own Kconfig handling.")  


# Add files to path
global_env.Append(CPPPATH=[build_dir])
global_env.BuildSources(build_dir, build_dir)

def add_menu(source, target, global_env):
    curr_env = global_env.subst('$PIOENV')
    curr_dir = os.path.join(global_env.subst('$PROJECT_LIBDEPS_DIR'), curr_env, "Robusto-PlatformIO", "scripts")
    
    # Co we need to add a menuconfig target?
    targets = global_env.get("__PIO_TARGETS")
    if targets:
        print("No targets")
    else:
        print("all targets: ")
        print(targets.values())

    if "menuconfig" not in targets.values():
        if framework.lower() != "espidf":

            menuconfig_cmd = "python {0} {1} ".format(
                os.path.join(curr_dir, "run_menuconfig.py"),curr_env
                )
            print("Addimg target, command: {0}".format(menuconfig_cmd))
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

global_env.AddPreAction("$PROGPATH", add_menu)

