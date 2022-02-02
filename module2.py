import random
import string

# function generates the list of dictionaries with random number of keys, 
# random keys and random values
def random_dict_generator():                        
    dct = {}
    for num in range(random.randint(1,26)):
        k = random.choice(string.ascii_lowercase)
        v = random.randint(0,100)
        dct[k] = v
    return dct

# function merge the list of dictionaries into one common dictionary
# with key/value pair for max value and key_index

def dict_merge(dict_list):
    alph = string.ascii_lowercase
    merged = {}
    for letter in alph:
        temp = []
        for dct in dict_list:
            if letter in dct.keys():
                temp.append(dct.get(letter))
            else:
                temp.append(-1)        
        v = max(temp)
        if v == -1:
            continue
        else:
            if temp.index(v) == 0:
                merged[letter] = v
            else:    
                merged[f'{letter}_{temp.index(v)}'] = v
    return merged

dict_list = []                                      # generates random list with random number of dictionaries 
for i in range(random.randint(2,10)):
    dict_list.append(random_dict_generator())
print("Random dictionaries list generated: ", dict_list)

common_dict = dict_merge(dict_list)
print("Dictionaries list merged: ", common_dict)