# The Cybernetics Thought Collective

The University of Illinois Archives has been awarded a grant from the National Endowment for the Humanities (NEH) to develop a prototype web-portal and analysis-engine to provide access to archival material related to the development of the iconic, multi-disciplinary field of cybernetics. The grant is part of the NEH’s Humanities Collections and Reference Resources Foundations program. The project, entitled “The Cybernetics Thought Collective: A History of Science and Technology Portal Project,” is a collaborative effort among several academic units at the University of Illinois (U of I) and three other institutions that also maintain archival records vital to the exploration of cybernetic history: the British Library, the American Philosophical Society, and the Massachusetts Institute of Technology. In addition to supporting the development of a web-portal and analysis-engine, the award will enable the multi-institutional team to begin digitizing some of the archival records related to the pioneering work of U of I Electrical Engineering Professor Heinz von Foerster and his fellow cyberneticians W. Ross Ashby (also a former U of I Electrical Engineering faculty member), Warren S. McCulloch, and Norbert Wiener.
## Author/Programmer 

* **Anirudh Chandrashekhar** (https://github.com/achndrs4)


## 1.Getting Started

All the tools used in this project are free to use, with the exception of Wolfram Desktop and Wolfram Cloud access. Below are recommended specifications to run this project smoothly . You *will* need administrative rights to install and run these programs.
<br />
**HARDWARE SPECIFICATIONS:** <br />
Processor: Intel Core i5 or equivalent AMD <br />
Processor (cont): 64 bit Address <br />
Disk Space: 50 GB <br />
System Memory (RAM): 8 GB+ recommended <br />
GPU: External GPU not required, but can be optimized by Wolfram <br />
Internet Access: Required in order to use online data sources from the Wolfram Knowledgebase. A wired connection is highly preferred<br />
<br />
### 2.Prerequisites
 
You will need the following tools (below) to execute this code. For best results, run in either a Virtual Box running Ubuntu or a full GNU/Linux environment<br />
```
Git
Python 3
Pip 3
```

### 3.Installing Git

The first tool we will need to clone this application and run it on out machines is git. Windows users can have access to Git using the [Git Standalone Installer](https://git-for-windows.github.io) as an exe file.

Mac users can enter the following command in the Mac Terminal to install git:

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install openssl
```

To use git on a Linux machine running Ubuntu run the following command
```
sudo apt-get install git
```
If you are on a Linux machine running CentOS, you will instead have to run the following command
```
sudo yum install git
```
### 4.Installing Python
*All Python files thus far are Python 2.7+ compatible as of 10/18/2017, but will soon also be upgraded and ported to run on Python 3*
Guide to [installing](https://docs.python.org/3/using/windows.html) Python on Windows
**remember to change the [path](http://docs.python-guide.org/en/latest/starting/install3/win/) of your variables***

Macs come Python 2 installed already, but if you have an older version of MacOS either download and execute the [standalone installer](http://www.python.org/ftp/python/3.1.1/python-3.1.1.dmg) or type the following into the terminal:

```
sudo brew install python3 && cp /usr/local/bin/python3 /usr/local/bin/python
```

For Linux Machines running Ubuntu, you either run the following command:
```
sudo apt-get install python
sudo apt-get install python3
```
or, for Linux builds running CentOs
```
sudo yum install python
sudo apt-get install python3
```


## 5.Installing Pip

Python 3.4 (released March 2014) and Python 2.7.9 (released December 2014) ship with Pip. To test if pip is working, open python to the command line and simply type in 
```
pip
```
If you get the following error:
```
NameError: Module 'pip' is not defined
```
you need to reinstall python to a version(+3.4) that has pip already.


## 6.Installing Pip Libraries
You will need 2 external libraries Installed in order for the script to work, mainly:

PDFMiner3k
Pandas

Once you have pip installed, you can run the following command:

On Windows: 
Open the command line(cmd) or Powershell (Python 3.4+) ONCE YOU ARE IN THE PROJECT DIRECTORY and then type:
```
 pip3 install pdfminer3k
 pip3 install pandas
```
For Linux and OSX, type in the same command, just on the terminal. Be sure to run pip when you are in the same directory as the project otherwise the libraries will not import!

## 7. Prepping Python Code

We are almost ready to run our Python code on the files. First, we run the preprocessing. This code will take all txt and PDF files, extract useful people and features from them, clean them, and produce minimal bag-of-words files to be used in the machine learning part of the code.

1) If your PDFs and Text files have already been sorted into folders with different class names(if they have been classified), then move them en masse to the folder called "Classes". If they have NOT been classified, then put all the text and PDF files into a folder called "Unknown". IT IS IMPERATIVE THAT THE GENERAL DIRECTORY STRUCTURE REMAINS:
PDF_Pipeline->Classes->(some folder(s))-> filenames.txt/pdf

2) Run clean_texts.py. This automatically creates features, people, filenames, extracted PDF text(in the folder New_Text), and a final cleaned and ML ready folder in the folder ML_Ready. Depending on the size of the PDFs, this may take a while.

3) This next step depends on whether or not you are planning to use your files to add to the training set (already classified), or if you want to benchmark for accuracy in the testing set. 
If you have classified these different files, then copy and paste the folders in the Machine_Learning/learn folder, so that Naive Bayes bag-of-words approach can be run on it. 
On the other hand, if you want to see how the files you have would be classified in the current system(AKA no human classification), then copy all of the files in the ML_Ready folder to the Machine_Learning/test folder.

4) Run Runner.py (python3 Runner.py, or on windows, simply "RUN/F5"). This will produce an HTML page and a CSV with the formatted information about the certainty of a file being in any given class (.95 means a 95% certainty of a file being in a certain class based on the current data avaliable)

## Deployment

Run individually. May eventually add SpringBoot to automate file building/running






