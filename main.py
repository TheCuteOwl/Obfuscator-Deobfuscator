




import base64
import re
infile = "obfuscated.txt"
outfile = "deobfuscated.txt"


delete_list = ["__0x_1ucif3r", "__", '"', '+', '=', '\\', 'exec(import(x62x61x73x65x36x34).b64decode(.encode(x75x74x66x2dx38)).decode(x75x74x66x2dx38))', 'x']
with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)



# Open the file
with open(outfile, 'r') as file:
    # Read the lines of the file
    lines = file.readlines()

# Open the file for writing
with open(outfile, 'w') as file:
    # Write each line to the file, with no line breaks
    for line in lines:
        file.write(line.strip())
        file.write(' ')

with open(outfile, 'r') as file:
    # Read the contents of the file
    contents = file.read()

# Remove all spaces from the contents
contents = contents.replace(' ', '')

# Open the file for writing
with open(outfile, 'w') as file:
    # Write the modified contents back to the file
    file.write(contents)


print("Done!")
with open("deobfuscated.txt", "r") as f:
    content = f.read()

decoded = bytes.fromhex(content).decode("utf-8")

with open("deobfuscated.txt", "w") as f:
    f.write(decoded)

import re

def unescape(s):
    
    s = re.sub(r'\\x([0-9a-fA-F]{2})', lambda m: chr(int(m.group(1), 16)), s)
    s = re.sub(r'\\u([0-9a-fA-F]{4})', lambda m: chr(int(m.group(1), 16)), s)

    return s


deobfuscated = unescape(decoded)

deobfuscated = base64.b64decode(deobfuscated)
deobfuscated = deobfuscated.decode("utf-8")

print(f'Deobfuscated : \n {deobfuscated}')
with open(outfile, 'w+', encoding='utf-8') as f:
    f.write(deobfuscated)



print('Deobfuscated version in deobfuscated.txt')
input('Successfully Deobfuscated Press Enter to Quit')



