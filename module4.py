primary_string = '''tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

divider = '-' * 100


def whitespace_counter(string):         # function calculates the number of whitespaces in given string
    count = 0
    for i in string:
        if i.isspace():
            count += 1  
    return count

def string_cleaner(string):             # function divides string into separate sentences and clean whitespaces and uppercases. Return list of sentences
    sentence_list = string.split('.')
    cleaned_sentence_list = []
    for sentence in sentence_list:
        sentence = sentence.replace('\n', '')
        sentence = sentence.strip()
        sentence = sentence.lower()
        cleaned_sentence_list.append(sentence)
    return cleaned_sentence_list

def iz_func(lst):                       # function changes incorrectly spelled 'iz' to 'is', and also divides sentences into separete words list 
    return_list = []
    for sent in lst:
        fixed_sentence = []
        sent = sent.split(' ')
        for word in sent:
            if 'iz' in word and len('iz') == len(word):
                fixed_sentence.append('is')
            else:
                fixed_sentence.append(word)
        return_list.append(fixed_sentence)
    return return_list

def string_builder(words_list):         # rebuild string from the words list. Add needed spaces, dots and Capital symbols.
    fixed_sentences = []
    for words in words_list:
        new_sentence = ' '.join(words)
        new_sentence = new_sentence.capitalize()
        fixed_sentences.append(new_sentence) 
    full_string = '. '.join(fixed_sentences)
    full_string = full_string[0:-1]
    return full_string

def new_string_builder(sentence_list):     # Build new string from the last words of all sentences
    new_words_list = []
    for sentence in sentence_list:
        sentence = sentence.split(' ')
        last_word = sentence[-1]
        new_words_list.append(last_word)
    new_sentense = ' '.join(new_words_list)
    new_sentense = new_sentense.capitalize()
    new_sentense = new_sentense[0:-1] + '.'
    return new_sentense

print(primary_string)
print(divider)

print('Number of whitespaces equals - ', whitespace_counter(primary_string))
print(divider)

cleaned_strings_list = string_cleaner(primary_string)
fixed_words_list = iz_func(cleaned_strings_list)
clean_string = string_builder(fixed_words_list)
new_string = new_string_builder(cleaned_strings_list)

print('Cleaned string: ', clean_string)
print(divider)
print('New string from last words: ', new_string)



