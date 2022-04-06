import csv
import os
import sys


# Check to see if a file exists
inputFile = "./data/richathletes.csv"

if not os.path.exists(inputFile):
    sys.exit("File not found")

# # read one line - long version
# data = open(inputFile, "r")
# print('\n##### Readline - long version #####')
# header = data.readline()
# print(header)
# header = header.rstrip('\n ')
# arr = header.split(',')
# print(arr)
# print(arr[4])

# data.close()

#read one line short version - method chaining
# data = open("./data/richathletes.csv", "r")
# # print('\n##### Readline - short version #####')
# header = data.readline().rstrip('\n ').split(',')
# print(header)
# print(f'\nColumn 4 is: { header[4] }')


# # read one more line
# info = data.readline().rstrip('\n ').split(',')
# print(info)

# # Close the file
# data.close()


# Use csv Reader to read a whole file
# print('%%%%% csv.reader %%%%%')
data = []

# open the file and then auto close it when done
with open('./data/richathletes.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    counter = 0
    for row in reader:
        # do stuff here
        if (counter == 0):
            header = row        
        else:
            data.append(row)
    
        counter += 1

athletes = len(data)

print(f"There are {counter} rows")
print(f"There are {athletes} data rows")
print(header)
print(data[34])
