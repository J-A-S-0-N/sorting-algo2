import random

global astpos
global bndpos
global tempnum1
global tempnum2

astpos = 0
bndpos = 1
tempnum1 = 0
tempnum2 = 0

def randnum():
    global list1
    global list2
    list1 = []
    for i in range(0, amo):
        num = random.randint(0,50)
        list1.append(num)
        
def ui():
    global amo
    amo = input("how many number >>> ")
    amo = int(amo)

def main():
    ui()
    randnum()
    for i in range(0,amo):
        for i in range(0,amo):
            if list1[astpos] > list1[bndpos]:
                list1[astpos] = tempnum1
                list1[bndpos] = tempnum2
                list1[astpos] = tempnum2
                list1[bndpos] = tempnum1
            else:
               astpos += 1
               bndpos += 1
            
        astpos = 0
        bndpos = 1
    for i in range(0, amo):
        print(str(list1[astpos]) + "\n" + str(list1[bndpos]) + "\n")
        astpos += 1
        bndpos += 1
        

if __name__ == "__main__":
    main()