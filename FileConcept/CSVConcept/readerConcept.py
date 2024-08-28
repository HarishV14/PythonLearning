import csv,os

os.chdir("C:\\Users\\Dell\\Documents\\PythonConcepts\\FileConcept\\CSVConcept")

with open('people.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

print("------------------------------------")
with open('people.csv','r') as file:
    reader=csv.reader(file,skipinitialspace=True)
    for row in reader:
        print(row)
print("------------------------------------")

with open('people2.csv','r') as file:
    reader=csv.reader(file,skipinitialspace=True,quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row)

print("------------------------------------")

#using dialect

csv.register_dialect('myDialect',
                     delimiter='|',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_NONE)

with open('people2.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='myDialect')
    for row in reader:
        print(row)

print("------------------------------------")

with open('people.csv','r') as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row)


print("---------------------------------------")
import csv

#first reads and detect the dialect
with open('people2.csv', 'r') as csvfile:
    sample = csvfile.read(64)
    has_header = csv.Sniffer().has_header(sample)
    print(has_header)

    deduced_dialect = csv.Sniffer().sniff(sample)
    print(deduced_dialect.delimiter)
    print(deduced_dialect.skipinitialspace)
    print(deduced_dialect.doublequote)


#then we use the dialect in the reader
with open('people2.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, deduced_dialect)

    for row in reader:
        print(row)
