import glob
import re
import os 


read_files = glob.glob("/home/achndrs4/Downloads/Extracted Texts/*.txt")

with open("allText.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(re.sub(r'\W+', '', infile.read()))
