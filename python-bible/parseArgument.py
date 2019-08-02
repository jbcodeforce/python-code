
'''
Parse argument in the form of --name value
'''
import sys


def parseArguments():
    version="0"
    arg2="default"
    if len(sys.argv) == 1:
        print("Usage: program --version v01 --arg2 val2 ")
        exit(1)
    else:
        for idx in range(1, len(sys.argv)):
            arg=sys.argv[idx]
            if arg == "--version":
                version=sys.argv[idx+1]
            elif arg == "--arg2":
                arg2=sys.argv[idx+1]
    return (version,arg2)
    




if __name__ == "__main__":
    (version, arg2)=parseArguments()
    print(version + " " + arg2)