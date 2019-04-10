import csv
import json

csvFilePath = 'global_dataset.csv'
jsonFilePath = 'global_dataset.json'

data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        hmid = csvRow["case_id"]
        data[hmid] = csvRow

with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))