import re
import sys
def string_beautify(string):
	stopwords =['what','this', 'This','that','work','best','without','who','vice','versa','is','a','at','is','he','ourselves','hers','between','yourself','but','again','there','about','once','during','out','very','having','with','they','own','an','be','some','for','do','its','yours','such','into','of','most','itself','other','off','is','s','am','or','who','as','from','him','each','the','themselves','until','below','are','we','these','your','his','through','don','nor','me','were','her','more','himself','this','down','should','our','their','while','above','both','up','to','ours','had','she','all','no','when','at','any','before','them','same','and','been','have','in','will','on','does','yourselves','then','that','because','what','over','why','so','can','did', 'not','now','Dear','under','he','you','herself','has','just','where','too','only','myself','which','those','i','after','few','whom','t','being','if','theirs','my','against','a','by','doing','it','how','further','was','here','than'] 
	for stopword in stopwords:
		string=string.replace((' '+stopword+' '), ' ')
		string= re.sub(r'\W+', '', string)
	return string.replace('\n', ' ')
	
