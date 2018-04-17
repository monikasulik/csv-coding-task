import os

from csv_parser import Parser


CSV_FILE_DIR = os.path.join(
    os.path.dirname(__file__), 'csv_parser', 'data')


print('----------------------------------------------------')
print('Results of parsing 1.csv:')
with open(os.path.join(CSV_FILE_DIR, '1.csv')) as csv_file:
    print(Parser(csv_file).parse())

print('----------------------------------------------------')
print('Results of parsing 2.csv:')
with open(os.path.join(CSV_FILE_DIR, '2.csv')) as csv_file:
    print(Parser(csv_file).parse())

print('----------------------------------------------------')
print('Results of parsing 3.csv:')
with open(os.path.join(CSV_FILE_DIR, '3.csv')) as csv_file:
    print(Parser(csv_file).parse())
print('----------------------------------------------------')
