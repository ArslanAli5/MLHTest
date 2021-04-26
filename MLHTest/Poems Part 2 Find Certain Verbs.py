#You decide to figure out how to count all of the verbs in a particular literary passage.  In real life, you would most likely use a Python library to assist with this task (go read about NLTK if you want to learn more).  In this exercise, you will be provided with a list of verbs on which to base your search.

#You need to write a function that takes a Python string as input and returns a list of the verbs found inside that string.  Your function only needs to include a verb in the returned list if that verb is also found inside the list named major_verbs.  Leave the definition of major_verbs at the very beginning of your function, as shown in the code below.  Do not change the major_verbs list.  If you change that list, your code will not pass the autograder and will not receive a grade.

#The list your function returns should be sorted in alphabetical order and should contain strings in all lowercase.  If you find a particular verb more than once, your list should only include it once (that is, your list should not contain duplicates).


#Note! Your function must be named find_verbs

def find_verbs(passage):
    # leave line 3 as is. These are the verbs to look for in the passage.
    major_verbs = ['see', 'seeing', 'saw', 'notice', 'noticed', 'noticing', 'ignore', 'ignored', 'ignoring', 'ran', 'run', 'runs', 'running', 'think', 'thinks', 'thought', 'thinking', 'eat', 'ate', 'eats', 'eating', 'be', 'is', 'was', 'were', 'are', 'being']
    
    # write your code below this line
    new_list = []
    passage = passage.replace('"',' ').replace(',',' ')
    for word in passage.split():   
        for verbs in major_verbs:
            if word.lower() == verbs:
                new_list.append(word)


    new_list = list(set(new_list))
    new_list.sort()
    return new_list



text = """ "Surely," said I, "surely that is something at my window lattice;\n Let me see, then, what thereat is, and this mystery explore—\n Let my heart be still a moment and this mystery explore;—\n 'Tis the wind and nothing more!" """
print(find_verbs(text))  
