import os

print(os.getcwd())
os.chdir("C:\\Users\\Dell\\Documents\\Word")
print(os.getcwd())
os.chdir("C:\\Users\\Dell\\Documents\\PythonConcepts")
print(os.getcwd())

print(os.listdir()) #current directory
print(os.listdir("C:\\Users\\Dell\\Documents\\PythonConcepts\\FileConcept")) #particular directory


# os.mkdir("test")
# os.rmdir("test")

os.chdir("C:\\Users\\Dell\\Documents\\PythonConcepts\\FileConcept")
# os.mkdir("test")
# os.rename("test","test1")
os.chdir("C:\\Users\\Dell\\Documents\\PythonConcepts\\FileConcept\\test1")

# os.mkdir("file.py")