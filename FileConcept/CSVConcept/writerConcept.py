import csv,os

os.chdir("C:\\Users\\Dell\\Documents\\PythonConcepts\\FileConcept\\CSVConcept")
with open('detail.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["names","rollno"])
    writer.writerow(["harish",30])
    writer.writerow(["guru",27])

row_list = [
    ["SN", "Name", "Quotes"],
    [1, "Buddha", "What we think we become"],
    [2, "Mark Twain", "Never regret anything that made you smile"],
    [3, "Oscar Wilde", "Be yourself everyone else is already taken"]
]
with open('quotes.csv', 'w', newline='') as file:
    writer = csv.writer(file
                        # , quoting=csv.QUOTE_NONNUMERIC
                        ,delimiter='|'
                        # ,quotechar='*'
                        )
    writer.writerows(row_list)

import csv
row_list = [
    ["ID", "Name", "Email"],
    ["A878", "Alfonso K. Hamby", "alfonsokhamby@rhyta.com"],
    ["F854", "Susanne Briard", "susannebriard@armyspy.com"],
    ["E833", "Katja Mauer", "kmauer@jadoop.com"]
]
csv.register_dialect('myDialect',
                     delimiter=':',
                     quoting=csv.QUOTE_ALL)
with open('office.csv', 'w', newline='') as file:
    writer = csv.writer(file, dialect='myDialect')
    writer.writerows(row_list)

with open('detail.csv','w',newline='') as file:
    fieldnames=["name","rollno"]
    writer=csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"name":"deepak","rollno":30})
    writer.writerow({"name":"guru","rollno":27})


import csv
row_list = [
    ['Book', 'Quote'],
    ['Lord of the Rings',
        '"All we have to decide is what to do with the time that is given us."'],
    ['Harry Potter', '"It matters not what someone is born, but what they grow to be."']
]
with open('book.csv', 'w', newline='') as file:
    writer = csv.writer(file, escapechar=':'
                        , quoting=csv.QUOTE_NONE,
                        # ,doublequote="*"
                        )
    writer.writerows(row_list)