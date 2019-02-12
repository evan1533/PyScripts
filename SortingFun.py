import random
import statistics as stat

def getMinIndex(list, start_index):
    smallest = -1;
    smallInd = -1;
    for i in range(start_index,len(list)):
        if smallest == -1 or list[i]<smallest:
            smallest = list[i]
            smallInd = i
    return smallInd

def sortMeList(list):
    for i in range(0,len(list)):
        cur_val = list[i]
        mindex = getMinIndex(list,i)
        list[i] = list[mindex]
        list[mindex] = cur_val;
    return list

def getFreqList(list,maxnum):
    freqs = [0]*(maxnum+1)
    for i in range(len(freqs)):
        freqs[i] = list.count(i);
    return freqs

def greaterHalf(list):
    half = (len(list)/2)
    tot = 0;
    for k in range(int(half)-int(half/2), int(half)+int(half/2)):
        tot += list[k]
    return tot

lenny = 0
while lenny is not -3:
    ransid_randoms = []
    lenny = int(input("List length: "))
    ran_length = 99
    for k in range(0,lenny):
        ransid_randoms.append(random.randint(0, ran_length))
    freq_rand = getFreqList(ransid_randoms,ran_length)

    prob = greaterHalf(freq_rand)/lenny
    #print(sortMeList(ransid_randoms))
    #print(freq_rand)

    print("Mean:\t",stat.mean(freq_rand))
    print("Median:\t",stat.median(freq_rand))
    print("σ:\t",stat.pstdev(freq_rand))
    print("s:\t",stat.stdev(freq_rand))
    print("p>μ:\t",prob);
    print("\n\n");
