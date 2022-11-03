import csv
import json
csv_path = input(r'Enter CSV path: ') #where the downloaded csv file is located, example C:\Users\jude kennywise\
jsonfile_path = input(r'Enter path where your json files will be saved: ') # example C:\Users\jude kennywise\NFTjson
csv_file = open(csv_path, 'r')
csv_reader = csv.DictReader(csv_file)

for row in csv_reader:
    out = json.dumps(row, indent=4)
    n = json.loads(out)
    print(n['Filename'])
    jsonout = open(jsonfile_path + '\\' + str(n['Filename']) + '.json', 'w')
    jsonout.write(out)
jsonout.close()
csv_file.close()