import zipfile
import shutil
import os

extract_loc=r"F:\Wspace\archive cleaner\taste d" # your extraction location goes here 
zippath=r"F:\Wspace\archive cleaner\files.zip"# your actual zip file location goes here :)

#once thats done run this script and pray it doesnt nuke your whole drive 😭🙏

with zipfile.ZipFile(zippath, 'r') as zip_ref:
    file_list = zip_ref.namelist()

    for file in file_list:
        print(file)
        main_path=os.path.join(extract_loc, file)

        if os.path.exists(main_path):
            if os.path.isdir(main_path):
                shutil.rmtree(main_path)
                print(f"Removed Folder: {file}")
            else:
                os.remove(main_path)
                print(f"Removed: {file}")
        else:
            print(f"File not found (T_T) : {file}")

'''
    for file in file_list:
        print(file)

'''

## Code by C-J0hn24



    