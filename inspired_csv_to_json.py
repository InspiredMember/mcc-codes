import csv
import json
#import rapidjson as json

#jsonfile = open('mcc_codes.json', 'w')

with open('inspired_mcc_codes.csv', 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    out = json.dumps([ row for row in reader ], indent=4)
    with open('mcc_codes.json', 'w') as jsonfile:
        jsonfile.write(out)
