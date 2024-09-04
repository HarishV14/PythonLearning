import os
os.chdir("c:\\Users\\LENOVO\\Documents\\PythonConcepts\\PythonLearning\\DiveInPython\\FileConcept")


with open("writeContent.txt",mode='w',encoding='utf-8') as file1:
    file1.write("Hello this is from python file")

with open('writeContent.txt', mode='a', encoding='utf-8') as a_file: 
    a_file.write(' and again')

with open("writeContent.txt",encoding='utf-8') as file1:
    print(file1.read())

#rb as no encoding method
with open("lion.jpg",mode='rb') as file:
    print(file.read(1)) #reading first word of binary file of image
    data=file.read()
    print(type(data))
    print(len(data))


import gzip

#gzip file is used to write the data in binary 

with gzip.open('out.log.gz', mode='wb') as z_file: 
    z_file.write('A nine mile walk is no joke, especially in the rain.'.encode('utf-8'))
# exit()

with open('out.log.gz',mode='rb') as file:
    print(file.read())