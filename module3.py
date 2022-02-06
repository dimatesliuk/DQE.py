primary_string = '''tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

divider = '-----------------------------------------------------------'

print(primary_string)
print(divider)

def whitespace_counter(string):         # function calculates the number of whitespaces in given string
    count = 0
    for i in range(0,len(string)):
        if string[i] == ' ':
            count += 1  
    return count

def iz_func(lst):                       # function changes incorrectly spelled 'iz' to 'is' 
    return_list = []
    for sent in lst:
        fixed_sentence = []
        sent = sent.split(' ')
        for word in sent:
            if 'iz' in word and len('iz') == len(word):
                #sent[sent.index('iz')] = 'is'
                #print(sent)
                fixed_sentence.append('is')
            else:
                fixed_sentence.append(word)
        return_list.append(fixed_sentence)
    return return_list

print('Number of whitespaces equals - ', whitespace_counter(primary_string))
print(divider)

string_to_list = primary_string.split('.')              # spliting string to separate sentences 

# cleaning sentences from extra symbols and making all letter lowercase 
new_str_list = []
for string in string_to_list:
    string = string.replace('\n', '')
    string = string.strip()
    string = string.lower()
    new_str_list.append(string)

new_str_list = iz_func(new_str_list)

# joining fixed words back to sentences 
fixed_sent = []
for words in new_str_list:
    new_sent = ' '.join(words)
    new_sent = new_sent.capitalize()
    fixed_sent.append(new_sent)

# rebuilding primary string with all issues fixed.
new_str = '. '.join(fixed_sent)
new_str = new_str[0:-1]
print(new_str)