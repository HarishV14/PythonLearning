import json,os,time

os.chdir("c:\\Users\\LENOVO\\Documents\\PythonConcepts\\PythonLearning\\DiveInPython\\SerializingConcept")

with open('entry.json', 'r', encoding='utf-8') as f:
    entry = json.load(f) 

print(entry)

print("---------------------------------------------------------------------------------------")

# it is used to convert the byes value in the json and converting 

def from_json(json_object):                                   
    if '__class__' in json_object:                            
        if json_object['__class__'] == 'time.asctime':
            return time.strptime(json_object['__value__'])    
        if json_object['__class__'] == 'bytes':
            return bytes(json_object['__value__'])            
    return json_object


with open('entry.json', 'r', encoding='utf-8') as f:
  entry = json.load(f, object_hook=from_json) 

print(entry)

print(entry['tags'])