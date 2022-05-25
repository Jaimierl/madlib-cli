# Welcoming the user

from ast import parse
from os import removedirs
import re


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
       raise FileNotFoundError("This path leads to a dead end and cannot be followed") 
        #We need to except this error based on what we did in class but we needed to raise this as an exception based on the test :/

def parse_template(template_string):
    # We want to take in a template_string and return
    # - a string with the language parts removed
    # - a list of the language parts
    fun_word = r"{(.*?)}"
    #This will find everything between the parenthesis using regex
    words = tuple(re.findall(fun_word, template_string))
    #This will make a tuple called words that cuts all of the words in parenthesis out of the template string and puts it into a tuple list
    gutted_string = re.sub(fun_word, "{}",template_string)
    #This is a regex substitution that will take out the words in parenthesis (including the parenthesis) and replace it with just the bare parenthesis in the template string like the test is looking for.

    return gutted_string, words
    # Note here that by getting this to work with regex, you do NOT need to look at every character in the string to check for the open or close characters. 


def merge(bare_template, entered_parts):
    # We want to take in a bare_template and a list of user entered language parts and return a string of the language parts inserted into the template.
    
    funny_string = bare_template.format(*entered_parts)
    #The * for the args pretty much lets us move between the curly brackets and iterate through those. This is because the things in the tuple don't have keys for implicit matching
    #A tuple is iterable - you don't need to make a list.
    return funny_string


if __name__ == '__main__':
    welcome()
    # read_template()
    # parse_template()
    # merge()
    # print (merge("It was a {} and {} {}.", ("dark", "stormy", "night")))


#You need to "control the flow" of your script (or file) by calling all of your functions this dunder main gate (not mifflin)


