import os
import glob

path = '/Users/federico/Desktop/Data Science - FORMATEMP/Python'
print(path)

files = glob.glob(os.path.join(path, '*.py'))
files = sorted(files)
for file_path in files:
    if file_path.split(sep="_")[-1] == "day1.py":
        new_name = file_path.split(sep="_")[0] + ".py"
        print(new_name)
        os.rename(file_path, new_name)