# sha256generator
clone the repository
```bash
  git clone  https://github.com/Judekennywise/sha256generator.git
```


1. After you have downloaded the csv file. Save in your diretory where you easily access it. It might be in your 'C\:' directory.

2. Create a folder where you will be saving the NFT json file for each row in your CSV. Take note of this path , as it will needed later.

3. To convert the CSV file(each line) into json files
open the makejsonfile.py

4. Run the file; it will prompt for your csv file path.

5. Make sure to copy the path where your CSV file is located. Example is C:\Mechanic Team boot_CSV.csv. make sure it has the '.csv' extention. inthis case 'Mechanic Team boot_CSV.csv' is the file we want to open, while 'C:\' is the path.

6. Hit enter; it will also prompt the for the path where you want to save the json files. Enter the path of the folder you created in step 2. example; C:\Users\jude kennywise\NftJSON

7. Hit enter and it prints the name of NFTs. That tells you that json file has been created. If not, repeat the steps and try again until it outputs the name of the NFts. Now check into the folder for the json files, You will find all json files for each row.

8. To calculate sha256 for each json file. Open the sha256hash.py file.

9. Run the file; it will prompt for the path of the json file.

10. Copy the path and enter one at a time to generate a sha256 of each file. Example of the path of your json file is 
C:\Users\jude kennywise\NftJSON\nftname.json

11. Copy the sha256 and append to your CSV file.

P.S: Incase of an error, make the the name column on your CSV is titled "Filename". The script searches for this key to fetch the names of the NFT in order to name the json file.
