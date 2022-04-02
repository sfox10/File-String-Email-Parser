# File/String Email Extractor v0.2

#   Currently only takes 1 or 2 before exiting. Would later
#   make it so that any # thats != 1 or != 2 will loop back to
#   line #8 print statement

import re

print('Please enter 1 (File) or 2 (String)')
definetype = input()

# File Searcher (Option 1)
if definetype == '1':
    try:
        print('Enter a file name to search:')
        # Need to close file after done with reading
        openfile = open(input())
        readfile = openfile.read()
        parsedfile = re.findall('\S+@\S+', readfile)
        print('Emails have been parsed.\nWould you like to output them to a file or simply view them?\n'
              'Type: F (file) or V (view)')
        outcome = str(input())
        # Output to File
        if outcome.startswith(('F', 'f')):
            with open('parsed.txt', 'w') as output:
                output.write(str(parsedfile))
                print('Emails have successfully been parsed to: parsed.txt')
                parsedfile.close() # BUG > 'Error: File does not exist!' after completion
        else:
            print(parsedfile)
    except:
        print('Error: File does not exist!')

# String Searcher (Option 2)
# Needs work. Doesn't work if large block of text is pasted
elif definetype == '2':
    print('Copy and paste your string:')
    userstring = input()
    readstring = userstring
    readstring_parsed = re.findall('\S+@\S+', readstring)
    print(readstring_parsed)
