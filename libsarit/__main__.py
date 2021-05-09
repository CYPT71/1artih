import sys
import argparse
from libsarit import TextCypher
def mod_help():
    print("""

    enter in this order 

        text string 

        key string

        numner int

        cypher true or false 
    """)


def parser():
    args = sys.argv[1:]
    print(args)
    print(not args[2].isdigit(), (args[3].lower() != "true" and args[3].lower() != "false"))
    if not args[2].isdigit() or (args[3].lower() != "true" and args[3].lower() != "false"):
        return mod_help()
    
    
    print(TextCypher(args[0], args[1], int(args[3]), args[3]=="true"))


if __name__ == "__main__":
    parser()
    
