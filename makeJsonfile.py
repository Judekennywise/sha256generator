import csv
import json

csv_path = input(r'Enter CSV path: ') #where the downloaded csv file is located, example C:\Users\jude kennywise\
jsonfile_path = input(r'Enter path where your json files will be saved: ') # example C:\Users\jude kennywise\NFTjson
csv_file = open(csv_path, 'r')
csv_reader = csv.DictReader(csv_file)
data = {}
format_ = 'CHIP-007'
for row in csv_reader:
    out = json.dumps(row, indent=4)
    n = json.loads(out)
    print(n['Filename'])
    data['format'] = format_
    data['name'] = str(n['Filename'])
    data['description'] = str(n['Description'])
    data['minting_tool'] = ""
    data['sensitive_content'] = False
    data['series_number'] = int(n['Series Number'])
    data['series_total'] = 380
    data['atrributes']= [
        {
            'trait_type':'gender',
            'value':str(n['Gender'])
        }
    ]
    data['collection'] = {
        'id' : 'b774f676-c1d5-422e-beed-00ef5510c64d',
        'name' : 'Zuri NFT Tickets for Free Lunch',
        'attribute' : [
        {
            'type':'description',
            'value':'Rewards for accomplishments during HNG9'

        }
    ]}
    data['data']= [
        {
            'uuid':str(n['UUID']),
            'hash' : str(n['Hash'])
        }
    ]
    

    
    jsonout = open(jsonfile_path + '\\' + str(n['Filename']) + '.json', 'w')
    jsonout.write(json.dumps(data, indent=6))
jsonout.close()
csv_file.close()


#create the sha of the json files
import os
import hashlib
#loop through the directory where the json files are located

directory = jsonfile_path
sha256_list = []
count = 1
for filename in os.listdir(jsonfile_path):
    sha256_hash = hashlib.sha256()
    with open(r'C:\NFTs' + '\\' + str(filename),"rb") as f:
    # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
            output =(sha256_hash.hexdigest())
            print('This is the SHA256 for row number ' + str(count)  + ' ====>' + str(output) )
            print('\n')
            count += 1

            


    
    
