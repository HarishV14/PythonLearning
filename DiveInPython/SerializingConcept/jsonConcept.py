import os
import json
import time

# Change directory (assuming this is your working directory)
os.chdir("c:\\Users\\LENOVO\\Documents\\PythonConcepts\\PythonLearning\\DiveInPython\\SerializingConcept")

# Example of a basic JSON serialization
basic_entry = {} 
basic_entry['id'] = 256
basic_entry['title'] = 'Dive into history, 2009 edition'
basic_entry['tags'] = ('diveintopython', 'docbook', 'html')
basic_entry['published'] = True
basic_entry['comments_link'] = None

with open('basic.json', mode='w', encoding='utf-8') as f: 
    json.dump(basic_entry, f, indent=3)  # Using indentation for better readability

# Custom JSON serialization function
def to_json(python_object):
    if isinstance(python_object, time.struct_time):
        return {'__class__': 'time.asctime', '__value__': time.asctime(python_object)}
    if isinstance(python_object, bytes):
        return {'__class__': 'bytes', '__value__': list(python_object)}
    raise TypeError(repr(python_object) + ' is not JSON serializable')

# Create a time.struct_time object using time.struct_time() from a function
published_date = time.struct_time((2009, 3, 27, 22, 20, 42, 4, 86, -1))

entry = {
    'comments_link': None,
    'internal_id': b'\xDE\xD5\xB4\xF8',
    'title': 'Dive into history, 2009 edition',
    'tags': ('diveintopython', 'docbook', 'html'),
    'article_link': 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition',
    'published_date': published_date,
    'published': True
}

with open('entry.json', 'w', encoding='utf-8') as f:
    json.dump(entry, f, default=to_json,indent=2)  #to_json function needs to handle types not supported by JSON natively
