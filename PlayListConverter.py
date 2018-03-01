import io
from io import BytesIO

androidPath = "/storage/3F6F-536E/Android/Music"
pcPath = "C:/Users/Basketlord/Desktop/Music"

#fileName = input("Name of playlist to convert\n")
fileName = "BeatlesFavorites"
f = open(fileName+".m3u","rb")
conv = open(fileName+"Convert.m3u","wb")
for line in f:
	line = (line).decode("utf-8");
	print(line)
	line = line.replace("\\","/")
	line = line.replace("C:/Users/Basketlord/Desktop/Music","/storage/3F6F-536E/Android/Music");
	line = line.encode("utf-8");
	conv.write(line)
f.close();
conv.close();