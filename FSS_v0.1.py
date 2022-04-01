# File/String Searcher v0.1

# Currently only takes 1 or 2 before exiting. Would like to
#   make it so that any # thats != 1 or != 2 will loop back to
#   line #8 print statement in next version(s) as well as changing cwd.

print('Please enter 1 (File) or 2 (String)')
definetype = input()

# File Searcher (Option 1)
if definetype == '1':
    try:
        print('Enter a file name to search:')
        # Need to close file after done with reading
        openfile = open(input())
        readfile = openfile.read()
        # Splits the file to search it in the for loop
        # Trouble understanding the dataflow. For loop should
        # be after the except block but still in the if (option 1)
        # statement, right?
        readfile_split = readfile.split()

    # Error handling for non-existent file
    # Issues: Needs to be restructed to continue to elif below (condition '2')
    except:
        print('Error: File does not exist!')
        definetype == 2

# String Searcher (Option 2)
# Does this need error handling? Couldn't trigger a traceback so seems OK
elif definetype == '2':
    print('Copy and paste your string:')
    userstring = input()
    readstring = str(userstring.split())
    wordcount = dict()
    for word in readstring:
        wordcount[word] = wordcount.get(word, 0) + 1
    print('Counts', wordcount)


