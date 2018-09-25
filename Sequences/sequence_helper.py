import decimal
import webbrowser
import time
import os

#This Program was made for educational purposes only!
#No hentai allowed!
#I had some trouble with homework, so i had to do it
#Don't you judge me!
# ( oh and for python practice of course)  <3

#just a gag
url = "https://www.youtube.com/watch?v=oHg5SJYRHA0"
#a tool for world domination
url1 = "https://www.desmos.com/calculator/ghh40zgna6"

#defines how many numbers after the decimal point
#the more the better approximation, but it slows the program
decimal.getcontext().prec = 30 #suggestion at first, but 100 works too

#huh.. every program needs a logo
def logo():
    print(
"""
#########################################################
                     WELCOME TO HELL
        HA KIDDING, WELCOME TO SEQUENCES HELPER
                          ENJOY!
                     Credit: xPinkie a.k.a Udi Shalev
#########################################################
    """);

#Please Define your Sequence Here:
def My_n_Place(a1,k):
    x=d(a1)#x=a1
    for i in range(1,k):
        x = (d(k)+1)/(k+2)
        #you can define x as an explicit sequence using k
        #for recusive function, use x
        #as default a1=1 but for a sequence, it dosen't matter.
    return x

def print_my_seq():
    f = open('sequence_helper.py','r')
    readline= f.readlines()
    seq=readline[36].strip(" ")
    if seq.count('x')>1:
        seq=seq.replace('x','a_(n+1)',1)
        seq=seq.replace('x','a_(n)')
        seq=seq.replace('d','')
    else:
        seq=seq.replace('x','a_(n)')
        seq=seq.replace('d','')
    print("Your a1 is: {}".format(My_n_Place(1,1)))
    print("The sequence you work with:\n{}".format(seq))
    f.close()
    
#Cosmetics
def line():
    print("_______________________________________________")
def d(l): #for making a number a decimal
    j=decimal.Decimal(l)
    return j
def iinput(string): # for py2/3
    try:
        output=raw_input(str(string))#py2
    except NameError:
        output=input(str(string))#py3
    return output

#Help Section
def my_help():
    print("""
    for starters you'll need to define your sequence inside the code itself,
    after that make sure to understand your doing,
    have fun!

    Commands:
      *  help - this help section
      *  limit - if you know your sequence converged,
                 it approxinates the limit.
      *  checkmon- checks for monotonic sub_suquences
      *  fun - RickRoll'D <3
      *  time - give the current time
      *  desmos - a tool for world domination
      *  theseq - displays the sequence you work with
      *  myseq %number% - prints your sequence to the %number% place.
      *  cls - clears and restart the menu
      *  quit - exits the program
    """);
    
#If you want to print serveral elements from the sequence
def mysequence(where):
    list1=[]
    for i in range(1,where+1):
        list1.append("a{}:{}".format(i,My_n_Place(1,i)))
    print("Here is your approximation of {} elements from your sequence".format(len(list1)))
    print("{}".format(list1))
    line()
    
def Monotonic_Checker():   
    ###Your sub sequence holder
    Increasing=[]
    Decreasing=[]
    #Checks Your Seuqnece Elements for its Monotonic Behavior
    #And adds to the sub sequences holder
    for i in range(1,100): #can be changed
        if My_n_Place(1,i)<My_n_Place(1,i+1):
            Increasing.append("a{}".format(i))
        else:
            Decreasing.append("a{}".format(i))
    line()
    #When Finsishes prints your sub sequence
    if len(Increasing)== 0 and len(Decreasing) == 0:
        print("There is a problem with your definded Sequence")
        #every sequence has a monotonic sub_sequence, math.. duhh...
    else:
        print("Here Is Your Increasing Sub_Sequence:\n{}".format(Increasing))
        line()
        print("Here Is Your Decreasing Sub_Sequence:\n{}".format(Decreasing))
    line()
    print("You evil! ");

#Cheks for the Limit, only for Converging Sequences 
def a_limit():       
    while True:
        Limit=iinput("""Would you like to check the limit?\n***Works only if your Sequence Converge***\n""")
        if Limit in ['yes','y','Y','Yes','YES']:
            print("\n Horray here is an approximation for the limit: \n")
            print(My_n_Place(1,1100)) # you can change here the estimation
            #the more the  better, but slows the program
            line()
            print("your lazy<3")
            break
        else:
            print("My Work here is Done.")
            line()
            break
        
##The program menu
def Menu():
    while True:
        myinput=iinput("What do you want to do?\n>")
        if myinput in ['help']:
            my_help()
        elif myinput in ['quit']:
            print("Ohh.. shame... Se'ya later then <3")
            time.sleep(1.5)
            exit()
        elif myinput in ['limit']:
            a_limit()
            line()
        elif myinput in ['checkmon']:
            Monotonic_Checker()
            line()
        elif myinput in ['fun']:
            webbrowser.open_new(url)
            line()
        elif myinput in ['desmos']:
            webbrowser.open_new(url1)
            line()
        elif myinput in ['time']:
            print(time.ctime())
            line()
        elif myinput in ['cls']:
            os.system('cls')
            continue
        elif 'myseq' in myinput:
            try:
                if len(myinput)>4:
                    myinput.strip(" ")
                    mysequence(int(myinput[5:]))
                    line()
            except:
                print("please write a number, see \'help\'")
                pass
        elif myinput in ['theseq'] :
            print_my_seq()
        else:
            print("I do not understand,\nwrite help for the commands.")
#start of the the program
logo()
Menu()
#end of program, WHAT SORCERY IS THAT?!
