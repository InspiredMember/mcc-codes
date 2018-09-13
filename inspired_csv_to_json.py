import csv
import rapidjson as json

with open('inspired_linked_fi_codes.csv', 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    out = json.dumps([ row for row in reader ], indent=4)
    with open('inspired_linked_fi_codes.json', 'w') as jsonfile:
        jsonfile.write(out)

with open('inspired_mcc_codes.csv', 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    out = json.dumps([ row for row in reader ], indent=4)
    with open('inspired_mcc_codes.json', 'w') as jsonfile:
        jsonfile.write(out)
