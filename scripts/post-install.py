import os

result = ""
for i, l in sorted(os.environ.items()):     
    result += i + ' : ' + l + '\n'

file_text = open("output.txt", "w")
file_text.write(result)
file_text.close()