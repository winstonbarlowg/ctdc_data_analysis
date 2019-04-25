import csv
import json

csvFilePath = 'female_typeOfExploit.csv'
jsonFilePath = 'female_typeOfExploit.json'

# data = {}
# with open(csvFilePath) as csvFile:
#     csvReader = csv.DictReader(csvFile)
#     for csvRow in csvReader:
#         hmid = csvRow["typeOfExploitConcatenated"]
#         data[hmid] = csvRow
#
# with open(jsonFilePath, "w") as jsonFile:
#     jsonFile.write(json.dumps(data, indent=4))

csvfile = open('female_typeOfExploit.csv', 'r')
jsonfile = open('female_typeOfExploit.json', 'w')

fieldnames = ("type","number")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
