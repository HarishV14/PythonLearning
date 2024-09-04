import os

os.chdir("c:\\Users\\LENOVO\\Documents\\PythonConcepts\\PythonLearning\\DiveInPython\\FileConcept")
print(os.getcwd())
file1=open('readContent.txt',encoding='utf-8')

print(file1.name,file1.encoding,file1.mode)


#it read the whole content in the file once file read then another reading same file cannot it doest not return error gives empty string
print(file1.read())
print(type(file1.read()))


#with used automatically close file handle the setup and clean up the operation
line_number = 0
with open("read2.txt",encoding="utf-8") as file2:
    print(file2.seek(23))
    print(file2.read(1)) 
    print(file2.tell())
    
with open("read2.txt",encoding="utf-8") as file2:

    for a_line in file2:                                               
        line_number += 1
        # print(a_line)
        print('{:>4} {}'.format(line_number, a_line.strip())) 


#Making sting as dumy file

print("---------------------------------------------------")
strings="I am acting as file but i am string"

import io

file=io.StringIO(strings)

print(file.read())
# file.write("hell0")  #cannot overwrite 
# print(file.read())