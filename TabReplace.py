fileName = "dumbText.txt";
file = open(fileName,"r");
lines = file.readlines();
newFile = open("spaceText.txt","w");

for line in lines:
        print(line);
        line = line.replace("\t"," ");
        newFile.write(line);
        print("\n");
        print(line);

file.close();
newFile.close();
