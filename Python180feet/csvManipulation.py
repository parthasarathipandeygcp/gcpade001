import csv

projectpath='c:/Users/822024/myproject/gcpade001/'

#Read a csv file

with open(projectpath+'data/person.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#Read CSV file Having Tab Delimiter

with open(projectpath+'data/innovators.csv', 'r') as file:
    reader = csv.reader(file, delimiter = '\t')
    for row in reader:
        print(row)

#Read CSV files with initial spaces

with open(projectpath+'data/people.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    for row in reader:
        print(row)

#Read CSV files with quotes

import csv
with open(projectpath+'data/quotes.csv', 'r') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for row in reader:
        print(row)


#Read CSV files using dialect

import csv
csv.register_dialect('myDialect',
                     delimiter='|',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_ALL)

with open(projectpath+'data/office.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='myDialect')
    for row in reader:
        print(row)

#Read csv using a dict reader

with open(projectpath+'data/people.csv', 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))