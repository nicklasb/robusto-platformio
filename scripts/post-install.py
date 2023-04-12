import os

result = ""
for i, l in sorted(os.environ.items()):     
    result += i + ' : ' + l + '\n'

print(result, file="output.txt")