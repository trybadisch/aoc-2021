from importlib.machinery import SourceFileLoader
import os, sys

sys.dont_write_bytecode = True

banner = '''\
   _      _             _          __    ___         _
  /_\  __| |_ _____ _ _| |_   ___ / _|  / __|___  __| |___
 / _ \/ _` \ V / -_) ' \  _| / _ \  _| | (__/ _ \/ _` / -_)
/_/ \_\__,_|\_/\___|_||_\__| \___/_|    \___\___/\__,_\___|
                        ___ __ ___ _
                       |_  )  \_  ) |
                        / / () / /| |
                       /___\__/___|_|\
'''
todo = [15,16,18,19,21,22,23,24,25]
days = [i for i in range(1,25+1)]
print(banner)
print("\nCalendar: ", *("["+(str(i).rjust(2, "0") if i not in todo else "  ")+"]" for i in range(1,14)), sep="")
print("          ", *("["+(str(i).rjust(2, "0") if i not in todo else "  ")+"]" for i in range(14, 25+1)), sep="")

def selector():
    day = 0
    try:
        while day <= 0 or day >= 25:
            day = int(input("\nChoose day [1-25]: "))
            if day in todo:
                print("\nDay not implemented yet.", end="")
        print()
    except:
        exit("\nExiting. Goodbye!")
    
    path = "advent"+str(day)
    cd = os.chdir(path)
    module = SourceFileLoader(path, path+".py").load_module()
    cd = os.chdir("../")

while True:
    selector()
