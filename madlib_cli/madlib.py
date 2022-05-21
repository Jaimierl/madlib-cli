# Welcoming the user

from os import removedirs


def welcome ():
    print("""
Welcome to Mad Libs! 
Madlibs is a game that writes a story with your inputs!
Fill in answers that match the parts of speech you are presented with!
""")

def testing():
    #This function is to test reading a file in the console
    with open ("assets/dark_and_stormy_night_template.txt") as f:
        contents = f.read()
    print (f)
    #This shows file information
    print(contents)
    #This will print the contents of the file into the console when the function is run
    return (contents)
    #This will show the contents of the file in the console log when you CALL the function (like in the main gate)


def read_template(file_path):
    #This takes in a file_path which it uses to open the file, strip the contents, and returns the stripped contents. Stripping is just removing the leading and trailing characters, which are spaces unless otherwise specified. 
    try:
        with open(file_path) as f:
            contents = f.read()
            return contents.strip()
            print (contents)
    except FileNotFoundError:
        print("This path leads to a dead end and cannot be followed") 

def parse_template(template_string):
    
    # We want to take in a template_string and return
    # - a string with the language parts removed
    # - a list of the language parts
    pass

def merge(bare_template):
    # We want to take in a bare_template and a list of user entered language parts and return a string of the language parts inserted into the template.
    pass


if __name__ == '__main__':
    welcome()
    


#You need to "control the flow" of your script (or file) by calling all of your functions this dunder main gate (not mifflin)
# When this runs, it will call the functions listed under it.

# # Questions
# Running the test file
# How to locally test if it is working