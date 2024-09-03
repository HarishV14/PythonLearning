import os,glob
import humanize

pathname=os.getcwd()

print(pathname)

#concating in the given directory
print(os.path.join("/user/harish/example/",'hello.py'))

#concating in the current directory where using expanduser(~)
print(os.path.join(os.path.expanduser("~"),'helloFilename','hello.py'))


pathname = '/Users/pilgrim/diveintopython3/examples/humansize.py'

(dirname,filename)=os.path.split(pathname)

print(dirname,"---",filename)

(shortname,extension)=os.path.splitext(filename)

print(shortname,"---",extension)


print(glob.glob('DataTypes/*.py'))
os.chdir("DataTypes/")
print(os.getcwd())
print(glob.glob('*test*.py'))


metadata=os.stat('SetConcept.py')
print(metadata)
print("----------------------------------------------------")

# hmSize=humanize.(metadata.st_size)
# print(hmSize)

print(os.getcwd())
print(os.path.realpath('SetConept.py'))