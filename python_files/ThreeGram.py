from collections import Counter
import stringUtils

userNumber = input('Enter the number of 3-Grams you would like displayed: ')
fileLocation= input('Enter the *full* path of the text file you would like to have analyzed: \n')
	
with open(fileLocation, 'r') as all_text:
	rawdata= string_beautify(all_text.read())
	shortword = re.compile(r'\W*\b\w{1,3}\b')
	cleandata=shortword.sub('', rawdata)
	

words=re.findall(r'[A-Za-z]+', cleandata)
trigrams=zip(words, words[1:], words[2:])
TrigramCount = Counter(trigrams)


times=int(userNumber)
print TrigramCount.most_common(times)

# "/home/achndrs4/Python_test/allText.txt"
