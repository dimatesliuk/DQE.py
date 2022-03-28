def string_cleaner(string):             # function divides string into separate sentences and clean whitespaces and uppercases. Return list of sentences
    sentence_list = string.split('.')
    cleaned_sentence_list = []
    for sentence in sentence_list:
        sentence = sentence.replace('\n', '')
        sentence = sentence.strip()
        sentence = sentence.lower()
        sentence = sentence.capitalize()
        cleaned_sentence_list.append(sentence)
    
    new_text = '. '.join(cleaned_sentence_list)
    return new_text