
import os

Import("env")

this_dir = os.path.join(env.subst('$PROJECT_LIBDEPS_DIR'), env.subst('$PIOENV'), 
                        "Robusto-PlatformIO", "scripts")
project_dir = env.subst('$PROJECT_DIR')

# Do we need to add a menuconfig target?
targets = env.get("__PIO_TARGETS")
if targets == None:
        print("No targets defined.")

if "menuconfig" not in targets.values():
    if framework.lower() != "espidf":
        menuconfig_cmd = "python {0} {1} ".format(
            os.path.join(this_dir, "run_menuconfig.py"),pio_env
            )
        print("Addimg target, command: {0}".format(menuconfig_cmd))
        env.AddTarget(
            name="menuconfig",
            dependencies=None,
            group="General",
            actions=[
                menuconfig_cmd
            ],
            title="Run menuconfig",
            description="Menuconfig is a tool for configuring an environment"
        )

