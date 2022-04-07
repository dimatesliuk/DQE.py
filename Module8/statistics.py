import csv
from datetime import datetime
import re

def words_extract(filename):
    dirty_list = []
    with open('feed.txt') as file:
        for row in file:
            row = row.split(' ')
            for item in row:
                if re.search('[a-zA-Z]', item):
                    dirty_list.append(item)
    clear_list = []
    for word in dirty_list:
        word = re.sub(r"[^\w\s'-]",'',word)
        word = word.replace('\n', '')
        if len(word) < 1 or re.search('[0-9]', word):
            continue
        else:
            clear_list.append(word)
    return clear_list

def letters_stat(clear_list):
    upper_case_letter = ''
    mixed_letters = "".join(clear_list)
    for letter in mixed_letters:
        if re.search('[A-Z]', letter):
            upper_case_letter += letter

    upper_case_letter = sorted(upper_case_letter)
    letters = sorted(mixed_letters.lower())
    
    letters_count = {}
    for letter in letters:
        if re.search('[a-z]', letter) and letters_count.get(letter):
            letters_count[letter] += 1
        elif re.search('[a-z]', letter):
            letters_count[letter] = 1
            
    upper_count = {}
    for letter in upper_case_letter:
        if re.search('[A-Z]', letter) and upper_count.get(letter):
            upper_count[letter] += 1
        elif re.search('[A-Z]', letter):
            upper_count[letter] = 1
    table = []
    for key in letters_count:
        if upper_count.get(key.upper()):
            table.append([key, letters_count[key], upper_count.get(key.upper()), round(upper_count.get(key.upper())/letters_count[key] * 100, 0)])
        else:
            table.append([key, letters_count[key], 0, 0.0])
    return table

def words_stat(clear_list):
    clear_list_lower = list(map(lambda x: x.lower(), clear_list))
    words_count = {}
    for word in clear_list_lower:
        if words_count.get(word):
            words_count[word] += 1
        else:
            words_count[word] = 1
    return list(words_count.items())

def write_csv(headers, lst):
    with open(headers[0] + '_' + datetime.now().strftime("%d_%m_%Y_%H%M"), 'w', newline='\n') as file:
        file_writer = csv.writer(file, delimiter=',')
        file_writer.writerow(headers)
        for row in lst:
            file_writer.writerow(row)

def exectute_stat():
    letters_header = ['Letter', 'Total', 'UpperCase', 'Upper%']
    words_header = ['Word', 'Total']

    clear_list = words_extract('feed.txt')
    letters = letters_stat(clear_list)
    words = words_stat(clear_list)
    write_csv(words_header, words) #words csv
    write_csv(letters_header, letters) #letters csv
