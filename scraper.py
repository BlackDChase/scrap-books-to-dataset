import os
import sys
#import threading  #later

fantasy="clean_fantasy"
lit="clean_literature"
res="clean_research_paper"

def make_text_file(threadName,folder,file_type):
    if file_type=="epub":
        bash_command = "./epub_to_text.sh " + folder
        os.system(bash_command)
    elif file_type=="pdf":
        bash_command = "./pdf_to_text.sh " + folder
        os.system(bash_command)
    else:
        print("Unknowntype file for "+threadName)
    threadName.exit()

def make_text_file(folder,file_type):
    if file_type=="epub":
        bash_command = "./epub_to_text.sh " + folder
        os.system(bash_command)
    elif file_type=="pdf":
        bash_command = "./pdf_to_text.sh " + folder
        os.system(bash_command)
    else:
        print("Unknowntype file for "+threadName)
    return

'''
class CreateThread (threading.Thread):
    arg = []
    def __init__(self, threadID, name, counter,folder,file_type):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.arg = [folder,file_type]
    def run(self):
        try:
            make_text_file(threadName,arg[0],arg[1])
        except:
            print("Error: unable to start "+threadName)
'''

args = sys.argv
args = args[1:] 
# First arg is the name of file itself

#threadList = []
for i in range(len(args)):
    if(str(args[i])=="fan"):
        args[i]=fantasy
    elif(str(args[i])=="lit"):
        args[i]=lit
    elif(str(args[i])=="res"):
        args[i]=res
    else:
        print(args[i]+" Not a proper argument")
        continue
    make_text_file(args[i],"pdf")
    make_text_file(args[i],"epub")
        
'''
    j=2*i
    k=2*i+1
    threadList.append(CreateThread(j, str(args[i])+" Thread "+str(j), j,args[i],"epub"))
    threadList.append(CreateThread(k, str(args[i])+" Thread "+str(k), k,args[i],"pdf" ))
    
for thread in threadList:
    thread.start()
'''
os.system("printf '%s%' `tput setaf 1` \" All Files Converted to text\" `tput sgr0`")
