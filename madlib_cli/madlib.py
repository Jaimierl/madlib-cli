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
    words = template_string.split()
    gutted_string = []
    new_string = template_string

    for fun_word in words:
        if fun_word.startswith('{'):
            stripped_fun_word = fun_word.strip('{}')
            gutted_string.append(stripped_fun_word)
            #Here we are taking any word that is surrounded by brackets (or starts with a curly bracket), removing or stripping the curly braclet, and pushing it into the gutted_string list.

            new_string = new_string.replace(fun_word, '{}')
            #Here we take the starting string we are given, and remove any words with brackets as we go through the for loop and we replace the words with brackets with just brackets because that is what the test is looking for.

            print (new_string, tuple(gutted_string))
            # Here we return the string without the fun_words and the list of fun words as a TUPLE because that is what the TEST is looking for, NOT what the directions asked for.
           

    return (new_string, gutted_string)
    #This is not working because it is not returning the final punctuation of the string and I'm not sure how to resolve it aside from rewriting this entire code block that I just got working with regex.
 


def merge(bare_template):
    # We want to take in a bare_template and a list of user entered language parts and return a string of the language parts inserted into the template.
    pass


if __name__ == '__main__':
    welcome()
    #read_template(assets/dark_and_stormy_night_template.txt)
    print (parse_template("Life is {just} so good {rn}!"))
    


#You need to "control the flow" of your script (or file) by calling all of your functions this dunder main gate (not mifflin)
# When this runs, it will call the functions listed under it.

# # Questions
# Running the test file
# How to locally test if it is working