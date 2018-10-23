f = open('test-file.txt','r')
file_lines = list(l for l in f)
#print(file_lines)

for line in file_lines:
    if 'dimension: _' in line:
        line = line+'\n\t hidden: yes'
        print(line)
    else:
        pass

#print(f.read())

f.close()