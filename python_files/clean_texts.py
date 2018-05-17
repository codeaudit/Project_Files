import xml.etree.ElementTree as ET
import os
import time
from collections import defaultdict, OrderedDict
import pdfminer
import re
import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
def string_beautify(string):
	stopwords =['what','this', 'This','that','work','best','without','who','vice','versa','is','a','at','is','he','ourselves','hers','between','yourself','but','again','there','about','once','during','out','very','having','with','they','own','an','be','some','for','do','its','yours','such','into','of','most','itself','other','off','is','s','am','or','who','as','from','him','each','the','themselves','until','below','are','we','these','your','his','through','don','nor','me','were','her','more','himself','this','down','should','our','their','while','above','both','up','to','ours','had','she','all','no','when','at','any','before','them','same','and','been','have','in','will','on','does','yourselves','then','that','because','what','over','why','so','can','did', 'not','now','Dear','under','he','you','herself','has','just','where','too','only','myself','which','those','i','after','few','whom','t','being','if','theirs','my','against','a','by','doing','it','how','further','was','here','than']
	for stopword in stopwords:
		string=string.replace((' '+stopword+' '), ' ')
		string= re.sub(r'\W+', ' ', string)
	return string.replace('\n', ' ')

def find_key_concepts(string):
    concepts=["Abduction","Action","Affordances" ,"Anatomy",
    "Art",
    "Auto",
    "Autonomy",
    "Behavior",
    "Being",
    "Belief",
    "Biology",
    "Cause" ,
    "effect",
    "Chaos",
    "Cognition",
    "Concept",
    "Consciousness",
    "Construction",
    "Control",
    "Theory",
    "Conversation",
    "Culture",
    "Description",
    "Design",
    "Domain",
    "Doubt",
    "Dream",
    "Ecology",
    "Engineering",
    "Environment",
    "Epistemology",
    "Error",
    "Ethics",
    "Evolution",
    "Experiment",
    "Experimental",
    "Fiction",
    "Flow",
    "Freedom",
    "Future",
    "Human",
    "Hypothesis",
    "Identity",
    "Illusion",
    "Imagination",
    "Methods",
    "World",
    "Nature",
    "Interdisciplinary",
"Intelligence",
"Intelligent",
"Information",
"Institution",
"Knowledge",
"Laboratory",
"Law",
"Learning",
"Magic",
"Man",
"Manuscript",
"Mathematics",
"Mechanism",
"Meaning",
"Memory",
"Metaphysics",
"Mind",
"Model",
"Nervous",
"System",
"Neurology",
"Observation",
"Observing",
"Order",
"Organism",
"Organization",
"Paradox",
"Pedagogy",
"Perception",
"Physics",
"Physiology",
"Process",
"Control",
"Reality",
"Reductionism",
"Representation",
"Science",
"Scientific",
"Space",
"Structure",
"Syntax",
"Synthesis",
"System",
"Systems",
"Thinking",
"Time",
"Theory",
"Theoretical",
"Truth",
"Understanding",
"Uncertainty",
"Value",
"Variety",
"Woman",
"Adaptive",
"Adaptation",
"Allo",
"Artificial",
"intelligence",
"Auto",
"Autonomy",
"Automata",
"Automaton",
"Autopoiesis",
"Biometrics",
"Circular / -ity",
"Coevolution",
"Communication",
"Complexity",
"Control",
"Cybernetics",
"Distinction",
"Eigen",
"Eigenvalue",
"Eigenbehavior",
"Electrolyte",
"Electrolytic",
"Emergence",
"Entropy",
"Feedback",
"Goal",
"Heterarchy",
"Heuristic",
"Homeostasis",
"Information",
"Neural",
"Visual",
"Laboratory",
"Engineering",
"Open",
"Order",
"Disorder",
"Self organization",
"Perturb / -ation",
"Purpose",
"Recursion / -ive",
"Regulation / -ator",
"Requisite",
"variety",
"Reticulum",
"Stability",
"State",
"Trivial",
"Ultrastability",
"Algorithm",
"Animal",
"Brain",
"Cat",
"Circuit",
"Code",
"Component",
"Computer",
"Ear",
"Earth",
"Eye",
"Frog",
"Function",
"Game",
"Hand",
"Hear",
"Machine",
"Map",
"Moon",
"Nerve",
"Network",
"Neural",
"network",
"Noise",
"Program",
"Reflex",
"See / -ing",
"Signal",
"Stimulus / response",
"Sun",
"Technology",
"Tool",
"Vision",
"American",
"Society",
"Biological",
    "Computer",
    "Laboratory",
"Aristotle",
"Ashby",
"Bateson",
"Beer",
"Bergson",
"Günther",
"Lettvin",
"Macy",
"Maturana",
"McCulloch",
"Mead",
"Newton",
"Pask",
"Pitts",
"Plato",
"Rosenblueth",
"Shannon",
"Turing",
"Varela",
"Von Foerster",
"Von Neumann",
"Walter",
"Wenner",
"Wiener",
"Wittgenstein"]
    newString=""
    for concept in concepts:
        if ((concept.lower() in string.lower())):
            newString+=concept+" "
    return newString


def convert(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    file_path = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(file_path, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    file_path.close()
    device.close()
    retstr.close()
    return text
if __name__ == '__main__':
    start_time = time.time()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    pdf_path=dir_path+"/PDFS"
    logfile_path=dir_path+"/Logfiles"
    features = dir_path + "/Features"
    new_text_path=dir_path+"/New_Text"
    if not os.path.exists(logfile_path):
        os.makedirs(logfile_path)
    if not os.path.exists(new_text_path):
        os.makedirs(new_text_path)
    if not os.path.exists(pdf_path):
        os.makedirs(pdf_path)
    if not os.path.exists(features):
        os.makedirs(features)

    for file in os.listdir(pdf_path):

        if file.endswith('.aa'):
            print(file)
            originPath= pdf_path+"/"+file
            filename_short= file[:-4]


            text_result=convert(originPath)
            count=[]
            count.append(0)
            count.append(1)

            for char in text_result:
                if not (char.isalpha() or " " or "\t" or "\n"):
                    count[0] += 1
                else:
                    count[1]+=1

            average_length= sum(map(len, text_result.split())) / (len(text_result.split())+.1)
            beautified= string_beautify(text_result)


            if(count[0]/count[1]>.1 or average_length<3 or average_length>9):

                open(logfile_path + "/" + filename_short + '_error.txt', 'w').close()
                f3=open(logfile_path + "/" + filename_short + '_error.txt', 'w')
                f3.write(file+" has a low readability score, and should be checked for accuracy")
                f3.close()
                print("ERROR WITH"+file)
                print(count[0]/count[1])
                print(average_length)
            else:
                "ADD FEATURES"
                open(features + "/" + filename_short + '_features.txt', 'w').close()
                f2 = open(features + "/" + filename_short + '_features.txt', 'w')
                f2.write(find_key_concepts(beautified))
                f2.close()

            open(new_text_path+"/"+filename_short+'_extracted.txt', 'w').close()
            f = open(new_text_path + "/" + filename_short + '_extracted.txt', 'w', errors='ignore')
            f.write(beautified)
            f.close()
    for file in os.listdir(features):
        filename_short_second = file[:-13]
        ffile = open(features+"/"+file, 'r')
        ffile2 = open(new_text_path + "/" + filename_short_second + "_extracted.txt", 'r')
        print("{\""+(ffile.read())+"\", \""+ffile2.read()+"\"}-> \"DOG\",")



