"""code to import patients from a .csv file and simply store them in a list"""
# pylint likes variables to be all caps
import csv
'''[0]: Emp ID, [1]: Empl Rcd, [2]: First Name, [3]: Middle Initial, [4]: Last Name, [5]:Home Facility, [6]:Department Code, [7]: Department Name, [8]: Location, [9]: Union
[10]:
[20]
[30] '''


CSV_IN = csv.reader(open('test.csv', 'r'))
CSV_OUT = csv.writer(open('output.csv', 'wb'))
for row in CSV_IN:
    ##---put in the stuff---##
    row[2] = row[2].upper()

    ##----------------------##
    CSV_OUT.writerow(row)
