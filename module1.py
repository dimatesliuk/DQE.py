import random

# create list of 100 random numbers from 0 to 1000
lst = [random.randrange(1,1000,1) for i in range(100)] #creating list using random module and list comprehension
print('Random list: ', lst)

# sort list from min to max (without using sort())
def sort_list(lst):
    sorted_lst = []
    while lst:
        list_min = lst[0]
        for i in lst:
            if i < list_min:
                list_min = i
        sorted_lst.append(list_min)
        lst.remove(list_min)
    return sorted_lst

lst = sort_list(lst)
print('Sorted list: ', lst)

# calculate average for even and odd numbers
# print both average result in console
def odd_even_list(lst):
    odd = []
    even = []
    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return odd, even

odd, even = odd_even_list(lst)
print("Odd list: ", odd)
print("Even list: ", even)

odd_avg = sum(odd) / 2
even_avg = sum(even) / 2
print('Odd average: ', odd_avg)
print('Even average: ', even_avg)