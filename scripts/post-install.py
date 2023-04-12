import os
from SCons.Script import DefaultEnvironment 
global_env = DefaultEnvironment()
for i, l in sorted(global_env.items()):     
    result += i + ' : ' + l + '\n'

file_text = open("output.txt", "w")
file_text.write(result)
file_text.close()