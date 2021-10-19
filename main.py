#https://docs.python.org/3/library/datetime.html

from datetime import date
import os
import sys

# toordinal(date)=int
# fromordinal(int)=date


# an entry is a int (date) plus a string (event)

entries=[]

#####################
######UTILITIES######
#####################

def getdate(): return date.toordinal(date.today())

def read_entries():
    global entries
    entries=[]
    f = open("entries.txt","r")
    count=0
    for line in f:  
        count+=1
        if count%2==1: 
            if (str(line[:-1])==''): break
            else: entries.append([int(str(line[:-1]))])

        else: entries[count//2-1].append(str(line[:-1]))
    entries=sorted(entries)

def update_entries():
    global entries
    entries=sorted(entries)
    os.remove("entries.txt")
    f = open("entries.txt", "a")
    for entry in entries:
        f.write(str(entry[0]))
        f.write('\n')
        f.write(entry[1])
        f.write('\n')

def print_entry(entry):
    print(str(date.fromordinal(entry[0]))+' '+entry[1])

def add_entry(day,event):
    global entries
    entries.append([day,event])

def list_entries(l,r):
    global entries
    for entry in entries:
        if (l<=entry[0]<=r): print_entry(entry)

#####################
######COMMANDS#######
#####################

def add(args):
    if (len(args)!=2):
        print("Error: 'add' requieres exactly 1 argument")
        return

    event=input()
    day=-1

    # you can add it as the distance between the event and today

    if (args[1].isdigit()): 
        day=getdate()+int(args[1])

    # or you can just add it as a date

    else:
        day=date.toordinal(date.fromisoformat(args[1]))

    entries.append([day,event])

def ls(args):
    if (len(args)!=2):
        print("Error: 'ls' requieres exactly 1 argument")
        return

    if (not args[1].isdigit()): 
        print("Error: First argument of 'ls' must be a nonnegative integer")
        return
    
    list_entries(getdate(),getdate()+int(args[1]))



#####################
####### MAIN ########
#####################

args=sys.argv[1:]

read_entries()

if (len(args)==0): print("Error: No command called as argument")
elif (args[0]=='add'): add(args)
elif (args[0]=='ls'): ls(args)
else:
    print("Error: Command " +args[0]+ " doesn't exist")

update_entries()