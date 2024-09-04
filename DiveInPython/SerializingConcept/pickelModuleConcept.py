shell=1
entry = {} 
entry['title'] = 'Dive into history, 2009 edition'
entry['article_link'] = 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition'
entry['comments_link'] = None
entry['internal_id'] = b'\xDE\xD5\xB4\xF8'
entry['tags'] = ('diveintopython', 'docbook', 'html')
entry['published'] = True
import time
entry['published_date'] = time.strptime('Fri Mar 27 22:20:42 2009') 
entry['published_date']
print(entry)
print("----------------------------------------------------------------------------------------------")

'''
@it serialize the data structure using data format called "pickle protcol"
@pickle protcol is no cross language comptablity cannot use in other languages 
@not every data can serialize
@no guarantee compatiblity different version of python
@older version of python does not support new format
@latest version of pickle protcol is binary format
'''
import pickle,os
os.chdir("c:\\Users\\LENOVO\\Documents\\PythonConcepts\\PythonLearning\\DiveInPython\\SerializingConcept")

with open('entry.pickle','wb') as f:
    pickle.dump(entry,f) #dump used to serialize into binary store in pickle file

with open('entry.pickle','rb') as r:
    entryRead=pickle.load(r)

print(entryRead)

print("-----------------------------------------------------------------------------------------")

'''Without using file'''

#it is serialization
b=pickle.dumps(entry)
print(type(b))

#it is deserialization
entry1=pickle.loads(b)
print(type(entry1))

print("------------------------------------------------------------------------------------------------------------")
import pickletools
''' 
It is used to inscpect the content and stucture if piece of object
usefull for debugging pickle format represent various python object 

'''
with open('entry.pickle', 'rb') as f:
    pickletools.dis(f)

print("-------------------------------------------------------------------------------------------")

