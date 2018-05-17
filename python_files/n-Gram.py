from collections import Counter
import re
import sys
from stringUtils import string_beautify

userNumber = input('Enter the number of n-Grams you would like displayed: ')
n= input('Enter the \'n\' to get the contiguous sequence of n items: ')

with open("/home/achndrs4/Python_test/allText.txt", 'r') as all_text:
	rawdata= string_beautify(all_text.read())
	shortword = re.compile(r'\W*\b\w{1,3}\b')
	cleandata=shortword.sub('', rawdata)
words=re.findall(r'[A-Za-z]+', cleandata)
nGrams= zip(*[words[i:] for i in range(int(n))])
nGramCount= Counter(nGrams)
times= int(userNumber)

print nGramCount.most_common(times)
