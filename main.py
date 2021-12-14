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
today = 14
days = [i for i in range(1,today+1)]
print(banner)
print("\nCalendar: ", *("["+(str(i).rjust(2, "0") if i<=today else "  ")+"]" for i in range(1,14)), sep="")
print("          ", *("["+(str(i).rjust(2, "0") if i<=today else "  ")+"]" for i in range(today, 25+1)), sep="")

def selector():
    day = 0
    try:
        while day <= 0 or day > today:
            day = int(input("\nChoose day [1-{}]: ".format(today)))
            if day > today and day <= 25:
                print("Day not implemented yet.")
        print()
    except:
        exit("\nExiting. Goodbye!")
    
    path = "advent"+str(day)
    cd = os.chdir(path)
    module = SourceFileLoader(path, path+".py").load_module()
    cd = os.chdir("../")

while True:
    selector()
