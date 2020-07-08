import math

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def find(self, value):
#       #start at the head
#       #loop through the list
#       #find value
#       #return the node
#         cur = self.head

#         while cur is not None:
#             if cur.value == value:
#                 return cur
#             cur = cur.next
#         return None

#     def delete(self, value):
#         cur = self.head

#         if cur.value == value:
#             self.head = cur.next
#             return cur

#         prev = cur
#         cur = cur.next

#         while cur is not None:
#             if cur.value == value:
#                 prev.next = cur.next
#                 return cur
#             else:
#                 prev = cur
#                 cur = cur.next

#             return None


#     def insert_at_head(self, node):
#         node.next = self.head
#         self.head = node



#recursion

#finds the n-th number in the fibonacci sequence
 #recursive:
    # needs base case, calls itself, move in direction of base case

# cache= {}
# #how do we use cache? need to store to use it again and decrease run time
# def fib(n):
#     if n <= 1:
#         return n

#     if n not in cache:
#         cache[n] = fib(n-1) + fib(n-2)
        
#     return cache[n]
# print(fib(3))
# print(fib(5))
# print(fib(6))
# print(fib(50))



#lookup Table
# lookup_table = {}

# def inverse_root(n):
#     return 1 / math.sqrt(n)

# def build_lookup_table():

#     for i in range(1, 1000):
#         lookup_table[i] = inverse_root(i)

# build_lookup_table()

# print(lookup_table[556])


#sorting
#why are dictionaries not in order?  why the order is not guaranteed?
    # everything hashes differently and you dont know what it will hash out to you
    # you dont know what it will give you back (return)
# my_list = []

# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append(4)

# my_list = [5,3,4,2,6,7,8,1,9]

# d  = {
#     'Austin': 12,
#     'Michael': 24,
#     'Troy': 35,
#     'Jorge':99,
#     'David': 42
# }
# # how can we sort our dictionary?

# #turn into a list
# for pair in d.items():
#     print(pair)

# #d.items().sort()

# print(sorted(d.items()))

# sorted_list_of_items = list(d.items())

# def anon_function(pair):
#     return pair[1]

# sorted_list_of_items.sort(reverse=True, key = lambda pair: pair[1])

# print(sorted_list_of_items)


#sort by value not by key
#tuple - interate over d.items
#sort with list comprehension
#sorted([(v, k) for k, v in d.items()])





#letter_count
#given a string
#return every letter and how many times it occurs in this string
#sorted by frequence of occurence


#iterate through our string
#tally the count using a dictionary
#sort our dictionary by the value (i.e. the count of each letter)

#upper or lower case everything
#handle spaces

#should we turn string into a list first?
def print_letter_count(s):
    tally = {}

    s = s.lower()
    # s.split()
    for character in s:
        #if not char.isspace():
        #if char!= " ":
        if character >= 'a' and character <= 'z':
            if character not in tally:
                tally[character] = 1
            else:
                tally[character] += 1
    #print(sorted(tally.items(), key=lambda x: x[1], reverse=True))
    #sorted gives back a new function
    tally_list = list(tally.items())
    tally_list.sort(key = lambda x: x[1], reverse=True)

    #tally_list.sort(key = lambda x: (-(x[1])))

    for pair in tally_list:
        print(f'Count: {pair[1]}, letter: {pair[0]}')

print_letter_count("bunny hop")
print_letter_count("the quick brown fox jumps over the lazy dog")