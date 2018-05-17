#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os
import time
from collections import defaultdict, OrderedDict
import re
import sys
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
def string_beautify(string):
    string = ''.join([i for i in string if not i.isdigit()])
    shortword = re.compile(r'\W*\b\w{1,3}\b')
    stopwords =['what','this', 'This','that','work','best','without','who','vice','versa','is','a','at','is','he','ourselves','hers','between','yourself','but','again','there','about','once','during','out','very','having','with','they','own','an','be','some','for','do','its','yours','such','into','of','most','itself','other','off','is','s','am','or','who','as','from','him','each','the','themselves','until','below','are','we','these','your','his','through','don','nor','me','were','her','more','himself','this','down','should','our','their','while','above','both','up','to','ours','had','she','all','no','when','at','any','before','them','same','and','been','have','in','will','on','does','yourselves','then','that','because','what','over','why','so','can','did', 'not','now','Dear','under','he','you','herself','has','just','where','too','only','myself','which','those','i','after','few','whom','t','being','if','theirs','my','against','a','by','doing','it','how','further','was','here','than']
    for stopword in stopwords:
        string=string.replace((' '+stopword+' '), ' ')
        string= re.sub(r'\W+', ' ', string)
    return re.sub(r'\W+', ' ', shortword.sub('', string))
classes=[]
def find_key_people(string):        
    people=["Aristotle",
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
    for person in people:
        if ((' '+person.lower()+' ' in string.lower())):
            newString+=person+"||"
    return newString[:-2]

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
"Purpose",
"Recursion",
"Recursive",
"Regulation",
"Regulator",
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
    "Laboratory"]
    newString=""
    for concept in concepts:
        if ((' '+concept.lower()+' ' in string.lower())):
            newString+=concept+"||"
    return newString[:-2]


def convert(path):
    text=""
    fp = open(path, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize('')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
# Process each page contained in the document.
    for page in doc.get_pages():
        interpreter.process_page(page)
        layout = device.get_result()
        for lt_obj in layout:
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                text += lt_obj.get_text()

    fp.close()
  
    return text
if __name__ == '__main__':
    start_time = time.time()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    classes_path=dir_path+"/Classes"
    logfile_path=dir_path+"/Logfiles"
    features = dir_path + "/Features"
    people=dir_path + "/People"
    new_text_path=dir_path+"/New_Text"
    ml_path= dir_path+"/ML_ready"
    ml_files=dir_path+"/ML_files"
    if not os.path.exists(logfile_path):
        os.makedirs(logfile_path)
    if not os.path.exists(new_text_path):
        os.makedirs(new_text_path)
    if not os.path.exists(classes_path):
        os.makedirs(classes_path)
    if not os.path.exists(features):
        os.makedirs(features)
    if not os.path.exists(people):
        os.makedirs(people)
    if not os.path.exists(ml_path):
        os.makedirs(ml_path)
    if not os.path.exists(ml_files):
        os.makedirs(ml_files)
    
    for dir in os.listdir(classes_path):
        path1 = os.path.join(classes_path, dir)
        if os.path.isdir(path1):
            print(dir)
            for file in os.listdir(path1):
                print(file)
                try:
                    if file.endswith('.pdf'):
                        originPath= path1+"/"+file
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

                        #average_length= sum(map(len, text_result.split())) / float(len(text_result.split())+.1)
                        beautified= string_beautify(text_result)


                       
                        #if(count[0]/count[1]>.5 or average_length<3 or average_length>9):

                        #    open(logfile_path + "/" + filename_short + '_error.txt', 'w').close()
                       #     f3=open(logfile_path + "/" + filename_short + '_error.txt', 'w')    
                     #       f3.write(file+" has a low readability score, and should be checked for accuracy\n Original File: \n")
                            #f3.write(beautified)
                           # f3.close()
                          #  print("ERROR WITH "+file)
                         #   print(count[0]/count[1])
                        #    print(average_length)
                            
                       #     open(new_text_path+"/"+filename_short+'_extracted.txt', 'w').close()
                      #      f = open(new_text_path + "/" + filename_short + '_extracted.txt', 'w', errors='ignore')
                     #       f.write(text_result)
                     #       f.close()
                      
                        final_string_c=find_key_concepts(beautified)
                        if(len(final_string_c)>0):
                            open(features + "/" + filename_short + '_features.txt', 'w').close()
                            f2 = open(features + "/" + filename_short + '_features.txt', 'w')
                            f2.write(final_string_c)
                            f2.close()
                        final_string_p=find_key_people(beautified)
                        if(len(final_string_p)>0):
                            open(people + "/" + filename_short + '_people.txt', 'w').close()
                            f2 = open(people + "/" + filename_short + '_people.txt', 'w')
                            f2.write(final_string_p)
                            f2.close()
                        open(new_text_path+"/"+filename_short+'_extracted.txt', 'w').close()
                        f = open(new_text_path + "/" + filename_short + '_extracted.txt', 'w', errors='ignore')
                        f.write(text_result)
                        f.close()
                        
                        
                        open(new_text_path+"/"+filename_short+'_extracted.txt', 'w').close()
                        f = open(new_text_path + "/" + filename_short + '_extracted.txt', 'w', errors='ignore')
                        f.write(text_result)
                        f.close()
     
                        
                        open(ml_path+"/"+filename_short+'.txt', 'w').close()
                        f = open(ml_path + "/" + filename_short + '.txt', 'w', errors='ignore')
                        f.write(beautified)
                        f.close()
                        
                        if not os.path.exists(ml_files+"/"+dir):
                            os.makedirs(ml_files+"/"+dir)
                        open(ml_files+"/"+dir+"/"+filename_short+'._ml_ready.txt', 'w').close()
                        f = open(ml_files+"/"+dir+"/"+filename_short+'._ml_ready.txt', 'w', errors='ignore')
                        f.write((final_string_c+final_string_p).replace("|"," "))
                        f.close()
                            
                    
                    

                    if file.endswith('.txt'):            

                        
                        originPath= classes_path+"/"+dir+"/"+file
                        filename_short= file[:-4]

                        with open(originPath, 'r') as myfile:
                            text_result = myfile.read()
                        count=[]
                        count.append(0)
                        count.append(1)

                        for char in text_result:
                            if not (char.isalpha() or " " or "\t" or "\n"):
                                count[0] += 1
                            else:
                                count[1]+=1

                        average_length= sum(map(len, text_result.split())) / float(len(text_result.split())+.1)
                        beautified= string_beautify(text_result)


                        #if(count[0]/count[1]>.5 or average_length<3 or average_length>9):

                         #   open(logfile_path + "/" + filename_short + '_error.txt', 'w').close()
                          #  f3=open(logfile_path + "/" + filename_short + '_error.txt', 'w')    
                           # f3.write(file+" has a low readability score, and should be checked for accuracy\n Original File: \n")
                           # f3.write(beautified)
                           # f3.close()
                           # print("ERROR WITH "+file)
                           # print(count[0]/count[1])
                           # print(average_length)

                            
                           # open(new_text_path+"/"+filename_short+'_extracted.txt', 'w').close()
                           # f = open(new_text_path + "/" + filename_short + '_extracted.txt', 'w', errors='ignore')
                           # f.write(text_result)
                           # f.close()
                   
                        final_string_c=find_key_concepts(beautified)
                        if(len(final_string_c)>0):
                            open(features + "/" + filename_short + '_features.txt', 'w').close()
                            f2 = open(features + "/" + filename_short + '_features.txt', 'w')
                            f2.write(final_string_c)
                            f2.close()
                        final_string_p=find_key_people(beautified)
                        if(len(final_string_p)>0):
                            open(people + "/" + filename_short + '_people.txt', 'w').close()
                            f2 = open(people + "/" + filename_short + '_people.txt', 'w')
                            f2.write(final_string_p)
                            f2.close()
                        open(new_text_path+"/"+filename_short+'_extracted.txt', 'w').close()
                        f = open(new_text_path + "/" + filename_short + '_extracted.txt', 'w', errors='ignore')
                        f.write(text_result)
                        f.close()
                        
                        
                        open(new_text_path+"/"+filename_short+'_extracted.txt', 'w').close()
                        f = open(new_text_path + "/" + filename_short + '_extracted.txt', 'w', errors='ignore')
                        f.write(text_result)

                        f.close()
     
                        open(ml_path+"/"+filename_short+'.txt', 'w').close()
                        f = open(ml_path + "/" + filename_short + '.txt', 'w', errors='ignore')
                        f.write(beautified)
                        f.close()
                        
                        if not os.path.exists(ml_files+"/"+dir):
                            os.makedirs(ml_files+"/"+dir)
                            

                        open(ml_files+"/"+dir+"/"+filename_short+'._ml_ready.txt', 'w').close()
                        f = open(ml_files+"/"+dir+"/"+filename_short+'._ml_ready.txt', 'w', errors='ignore')
                        f.write((final_string_c+"\n"+final_string_p).replace("|"," ").lower())
                        f.close()
                except:
                    continue

                        
                               


