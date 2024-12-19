story_temp = '''On a (adj) day, I went to the (noun). 
I saw a (adj) (noun) swinging from the trees. 
Then, I (verb) a (adj) lion lounging in the (noun).  
What a wild and (adj) experience!'''


verb = input('Please enter a verb: ')
noun = input('Please enter a noun: ')
adj = input('Please enter an adjective: ')
# new_story = ''
words_list = []



for word in story_temp.split():
    if word.__contains__('(verb)'):
        word = verb
    elif word.__contains__('(noun)'):
        word = noun
    elif word.__contains__('(adj)'):
        word = adj
    
    # This is not efficient, because it creates a new string every iteration.
    # new_story += f'{word} '
    words_list.append(word)


new_story = ' '.join(words_list)
        

print(new_story)




