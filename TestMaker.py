import os
import regex as re
import datetime


honor_code = """/** 
 *  On my honor: 
 *
 *  - I have not used source code obtained from another student,
 *  or any other unauthorized source, either modified or
 *  unmodified. 
 *
 *  - All source code and documentation used in my program is
 *  either my original work, or was derived by me from the
 *  source code published in the textbook for this course. 
 *
 *  - I have not discussed coding details about this project with
 *  anyone other than my partner (in the case of a joint
 *  submission), instructor, ACM/UPE tutors or the TAs assigned
 *  to this course. I understand that I may discuss the concepts
 *  of this program with other students, and that another student
 *  may help me debug my program so long as neither of us writes
 *  anything during the discussion or modifies any computer file
 *  during the discussion. I have violated neither the spirit nor
 *  letter of this restriction.
 *
 *  @author %s (%s)
 *  @date %2d.%2d.%d
 */\n\n"""

def init():
	global fileNames;
	fileNames = [];
	for root, dirs, files in os.walk("."):  
		for filename in files:
			fileNames.append(filename);
			if ".java" in filename and "test" not in filename.lower():
				if (filename.split("."))[0] + "Test.java" not in files:
					createTestFile(filename)
				#else:
				#	appendTestFile(filename)



def find_author():
	global fileNames;
	regex = re.compile("(?<=@author )(.+)(?= [(]) [(](.+)[)]")
	java_files = [f for f in fileNames if ".java" in f and "test" not in f.lower()]
	author_name = ""
	author_PID = ""

	for jFileName in java_files:
		jFile = open(jFileName,"r")
		lines = jFile.readlines()
		for line in lines:
			res = re.search(regex, line);
			if(res):
				author_name = res.group(1)
				author_PID = res.group(2)
				jFile.close()
				return author_name, author_PID
		jFile.close()
	return None

def getMethodNames(jFileName) -> list:
	jFile = open(jFileName,"r");
	lines = jFile.readlines();

	index = 0
	methodNames = [];
	regex = re.compile(r'(public|private) [<-z]+ \K[<-z]+(?=[(]{1})')

	for line in lines:
		res = re.search(regex, line);
		if(res):
			if res.group() not in methodNames:
				methodNames.append(res.group())
	
	jFile.close();
	return methodNames

def createTestFile(jFileName: str):
	
	print(jFileName)
	nameNoExt = (jFileName.split("."))[0];
	testFileName = nameNoExt+"Test.java";
	testFile = open(testFileName,'w+')
	
	now = datetime.datetime.now()

	author_info = find_author()
	if(author_info is None):
		author_info[0] = "<Name>"
		author_info[1] = "<PID>"

	#Write honor code
	my_honor = honor_code % (author_info[0], author_info[1], now.month, now.day, now.year)
	testFile.seek(0,0)
	testFile.write(my_honor)

	#Write header
	cur_dir = os.getcwd();
	regex = re.compile(".*(?<=[\/])(.*)")
	res = re.search(regex, cur_dir)
	package = "<package>"
	if res:
		package = res.group(1)

	testFile.write(("package %s;\n\n" % (package)))
	testFile.write(("public class %s extends student.TestCase {\n\n" % (nameNoExt+"Test")))

	testFile.write("\t/**\n\t *\n\t */\n")
	testFile.write("\tpublic void setUp() {\n\t\t\n\t}\n\n")

	#Write the test methods
	methodNames = getMethodNames(jFileName);	
	for meth in methodNames:
		comment = "\t/**\n\t * test %s()\n\t */\n" % meth
		methLine = "\tpublic void test" + meth[0].upper() + "" + meth[1:] + "() {\n\t  \n\t}\n\n";
		testFile.write(comment);
		testFile.write(methLine);
				
	testFile.write("}")
	testFile.close()



def appendTestFile(jFileName: str):
	print(jFileName)
	nameNoExt = (jFileName.split("."))[0];
	testFileName = nameNoExt+"Test.java";
	testFile = open(testFileName,'a+')

	methodNames = getMethodNames(jFileName);	
	lines = testFile.readlines();
	testFile.seek(0, 0)
	for meth in methodNames:
		comment = "\t/**\n\t * test %s()\n\t */\n" % meth
		methLine = "\tpublic void test" + meth[0].upper() + "" + meth[1:] + "() {\n\t  \n\t}\n\n";
		testFile.write(comment);
		testFile.write(methLine);
				
	testFile.write("}")
	testFile.close()



if __name__ == "__main__":
	init();	
