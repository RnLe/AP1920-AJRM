from os import listdir
import sys

if len(sys.argv) == 1:
    print("Please specify a folder as argument (e.g. data or plots)")
    sys.exit()

with open(f"../data/filenames_of_{sys.argv[1]}.txt", 'w') as f:
    for file in listdir(f"../{sys.argv[1]}/"):
        f.write(f'{sys.argv[1]}/{file} ')