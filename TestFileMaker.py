jFileName = input("What is the name of the file:\n");
jFile = open(jFileName+".java","r");
lines = jFile.readlines();
nameNoExt = (jFileName.split("."))[0];

index = 0
methodNames = [];

for line in lines:
    words = line.split(" ")
    if "public" in words and words.index("public")>0 and (nameNoExt + "()") not in words:
        if words[words.index("public")+2] is not " ":
            meth_name = words[words.index("public")+2]
            split_meth = meth_name.split("(");
            methodNames.append(split_meth[0]);
    index = index + 1

jFile.close();

testFileName = nameNoExt+"Test.java";
testFile = open(testFileName,'r+');
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
    if i == begInd-1:
        for meth in methodNames:
            comment = "/**\n * test %s()\n */\n" % meth
            methLine = "public void test" + meth[0].upper() + "" + meth[1:] + "() {\n  \n}\n\n\n";
            testFile.write(comment);
            testFile.write(methLine);

testFile.close()
