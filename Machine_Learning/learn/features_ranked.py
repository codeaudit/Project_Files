import re
import os
from collections import Counter
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
if(len(sys.argv)<2):
    print("ERROR! PLEASE PROVIDE LENGTH ARGUMENT")
    exit(22)
for direc in os.listdir(dir_path):
    if os.path.isdir(dir_path+"/"+direc):
        print(direc)
        passage=""
        for file in os.listdir(direc):
            if file.endswith('.txt'):
                f3=open(dir_path + "/" + direc + '/'+file, 'r')    
                passage=passage+" "+f3.read()
        words = re.findall(r'\w+', passage)
        cap_words = [word.upper() for word in words]
        word_counts = Counter(cap_words)     
        print(word_counts.most_common(int(sys.argv[1])))


