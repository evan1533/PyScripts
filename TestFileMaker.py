import regex as re

# put Group 1 captures in a list
#matches = [group for group in re.findall(regex, subject) if group]

jFileName = input("What is the name of the file:\n");
jFile = open(jFileName+".java","r");
lines = jFile.readlines();
nameNoExt = (jFileName.split("."))[0];

index = 0
methodNames = [];
regex = re.compile(r'(public|private) [<-z]+ \K[<-z]+(?=[(]{1})')#"(?<=(public|private) [<-z]+ )[<-z]+(?=[(]{1})"#(public|private) [<-z]+ [<-z]+(?=[(]{1})"

for line in lines:
    res = re.search(regex, line);
    if(res):
        if res.group() not in methodNames:
            methodNames.append(res.group())

print(methodNames)

jFile.close();

testFileName = nameNoExt+"Test.java";
testFile = open(testFileName,'r+')
    
lines = testFile.readlines();

index = 0
begInd = -1
for line in lines:
    words = line.split(" ");
    if "class" in words and begInd == -1:
        begInd = index;
    index = index + 1

testFile.seek(0, 0)
for i, line in enumerate(testFile):
    if i is begInd-1:
        for meth in methodNames:
            comment = "\t/**\n\t * test %s()\n\t */\n" % meth
            methLine = "\tpublic void test" + meth[0].upper() + "" + meth[1:] + "() {\n\t  \n\t}\n\n";
            testFile.write(comment);
            testFile.write(methLine);
            
testFile.write("}")
testFile.close()
