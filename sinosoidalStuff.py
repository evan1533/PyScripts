count = 0;
increasing = True;
amp = 10;
dc = 1;
graph = "";

while True:
    for i in range(0,count):
        if count==amp and i == count-1:
            graph = graph + "*";
        elif increasing:
            graph = graph + "\\";
        elif not increasing:
            graph = graph + "/";
    print(graph);
    graph = "";
    count = count + dc;
    if (count+dc) > amp:
        increasing = False;
        dc = -1;
    elif (count+dc) <= 0:
        increasing = True;
        dc = 1;
        
