#A literature scholar asks you to write Python code to analyze a set of poems.  To start, the scholar wants you to find out if the verb "to see" appears anywhere in the text.  Your program should return the value True or the value False based on whether or not the verb was found.

#Assume that you have a variable called see_tenses containing a list of all the tenses of "to see" which you should check for.  If the poem contains any of the words inside the see_tenses list regardless of capitalization, your function should return True.  Otherwise, your function should return False.


#Note! Your function must be named checker_function

def checker_function(poem_text):
    # leave this line in the code
    see_tenses = ['saw', 'see', 'sees', 'seeing', 'seen']

    # your code goes here
    flag = False
    poem_text = poem_text.replace('"',' ').replace(',',' ')
    for word in poem_text.split():   
        for tenses in see_tenses:
            if word.lower() == tenses:
                flag = True
                break
    return flag

text = """ "Surely," said I, "surely that is something at my window lattice;\n Let me see, then, what thereat is, and this mystery explore—\n Let my heart be still a moment and this mystery explore;—\n 'Tis the wind and nothing more!" """
print(checker_function(text))      



