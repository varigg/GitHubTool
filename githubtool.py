import getopt
import sys
import requests
import json
from github import GitHub

metrics = ("forks","stars","pr", "contrib")

def usage():
    print("Usage:")
    print ("  "+sys.argv[0] + " [options] org")
    print ("Options:")
    print("  -n number\tNumber of repos to show [default: 10]")
    print("  -m metric\tA metric to rank by. Recognized metrics are:")        
    print("  \t\tforks - number of forks[default]") 
    print("  \t\tstars - number of stars") 
    print("  \t\tpr - number of pull requests") 
    print("  \t\tcontrib - contribution rate(pull requests/forks)")         
        
def main():
    org=""
    number=10
    metric="forks"
    try:
        opts, arg = getopt.getopt(sys.argv[1:], "n:m:")
    except getopt.GetoptError as err:
        print (str(err))
        usage()
        sys.exit(2)
    for o, a in opts:
        if o == "-n":
            number = a
            if not number.isnumeric():
                print(number+" is not a number.")
                sys.exit(2)
        elif o == "-m":
            metric = a
            if not metric in metrics:
                print(metric + " is not a valid metric.")
                print("Accepted metrics are: ")
                print("forks - number of forks")
                print("stars - number of stars")
                print("pr - number of pull requests")
                print("contrib - contribution rate (forks/pr)")
        else:
            assert False, "unhandled option"
    if arg==[]:
        print("org is a required parameter")
        usage()
        sys.exit(2)
    org=arg[0]
    gitHubOrg=GitHub(org)
    gitHubOrg.findTopRepos(int(number),metric)
if __name__ == "__main__":
    main()	
