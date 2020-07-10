import math
import urllib.request
import datetime
import time
import random
import hashlib

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


sorting
why are dictionaries not in order?  why the order is not guaranteed?
    everything hashes differently and you dont know what it will hash out to you
    you dont know what it will give you back (return)
my_list = []

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list = [5,3,4,2,6,7,8,1,9]

d  = {
    'Austin': 12,
    'Michael': 24,
    'Troy': 35,
    'Jorge':99,
    'David': 42
}
# how can we sort our dictionary?

#turn into a list
for pair in d.items():
    print(pair)

#d.items().sort()

print(sorted(d.items()))

sorted_list_of_items = list(d.items())

def anon_function(pair):
    return pair[1]

sorted_list_of_items.sort(reverse=True, key = lambda pair: pair[1])

print(sorted_list_of_items)


# sort by value not by key
# tuple - interate over d.items
# sort with list comprehension
# sorted([(v, k) for k, v in d.items()])





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
# def print_letter_count(s):
#     tally = {}

#     s = s.lower()
#     # s.split()
#     for character in s:
#         #if not char.isspace():
#         #if char!= " ":
#         if character >= 'a' and character <= 'z':
#             if character not in tally:
#                 tally[character] = 1
#             else:
#                 tally[character] += 1
#     #print(sorted(tally.items(), key=lambda x: x[1], reverse=True))
#     #sorted gives back a new function
#     tally_list = list(tally.items())
#     tally_list.sort(key = lambda x: x[1], reverse=True)

#     #tally_list.sort(key = lambda x: (-(x[1])))

#     for pair in tally_list:
#         print(f'Count: {pair[1]}, letter: {pair[0]}')

# print_letter_count("bunny hop")
# print_letter_count("the quick brown fox jumps over the lazy dog")


#indexing
records = [
    ('Tim', 'Texas'),
    ('Adam','Florida'),
    ('Austin', 'Florida'),
    ('Kai','South Carolina'),
]
#     Understand
#given a list of records, build an index
#so we can quickly find everyone in a given state

#     plan
#iterate through the tuples in our list
##Build a dictionary as we go
##use states as keys, names as values

##if a state isnt in dictionary, add it as key
##value: [name1, name2, name3]

##possible value data structures: list, set, nest hastable
###{state: {name:lastname}}

##if we have good pseudocode, then we're done planning

'''for name, state in records:
    value = index.setdefault(state, [])
    value.append(name)'''

def build_index(records):
    index = {}
    ##iterate through list
    for name, state in records:
    ##for reach pair, check if the state is in the dictionary 
        if state in index:
    ###if so, append the name to the list
            index[state].append(name)
    ##if not, add the key and list (with name in it)
        else:
            index[state] = [name]
    return index

idx = build_index(records)

print(idx['Florida'])


##cipher

##suppose we have a bunch of data, and you want to transform it
## you know what it should transform to

##substituting one letter for another

## goal: write an encode() function


##need to change one char to another char (for every char in string, sub with another char)
###map from one char to another
##use that to change an entire string into another

encode_table = {
"A": "M",
"B": "N",
"C": "B",
"D": "V",
"E": "C",
"F": "X",
"G": "Z",
"H": "L",
"I": "K",
"J": "J",
"K": "H",
"L": "G",
"M": "F",
"N": "D",
"O": "S",
"P": "A",
"Q": "P",
"R": "O",
"S": "I",
"T": "U",
"U": "Y",
"V": "T",
"W": "R",
"X": "E",
"Y": "W",
"Z": "Q"}

decode_table = {}
##decode_table = {v:k for k, v in encode_table.items()}
def build_decode(encoding_table):
    for key, value in encoding_table.items():
        decode_table[value] = key


def decode(s):
    decoded_string = ""
    ##iterate over the given string
    s= s.upper()
    for character in s:
        if character not in decode_table:
            decoded_string += character
        else:
    ##for each char, look up its mapping
            unscrambled_character = decode_table[character]
    ##build our return string
            decoded_string += unscrambled_character
    ##return the return string
    return decoded_string

def encode(s):
    encoded_string = ""
    ##iterate over the given string
    s= s.upper()
    for character in s:
        if character not in encode_table:
            encoded_string += character
        else:
    ##for each char, look up its mapping
            scrambled_character = encode_table[character]
    ##build our return string
            encoded_string += scrambled_character
    ##return the return string
    return encoded_string

print(encode("Hail Caesar"))





###client caching
##   Understand

##let's a make a web client
##it will fetch URLs
##but it will cache the web page thats returned

##  Plan
#how to use hashtable to make a web cache?
## key:url
#value: webpage data

##could make the value store more info
##webpage data when we looked it up

#    Execute

# import urllib.request

# class CacheEntry:
#     def __init__(self, url, data):
#         self.data = data
#         self.url = url
#         self.time_fetched = datatime.datatime.now()

# cache = {}

# url = "https://www.google.com"

# TIMEOUT = 10
# def get_page(url):
#     time_now = datetime.datetime.now().timestamp()
#     #given a url, check to see if its in the cache
#     if url in cache and time_now - cache[url].time_fetched <TIMEOUT:
#         #if less than 10 seconds since our last request
#     #if so, return that
#         return cache[url]
#     #if not, go get it
#     else:
#         print("going out into the webs to get the page")
#         resp = urllib.request.urlopen(url)
#         data = resp.read()
#         resp.close()

#     #put in cache
#         cache[url] = CacheEntry(url, data)
#     return cache[url]

# page = get_page(url)
# print("now we wait!")
# time.sleep(10)
# page = get_page(url)

#   Review

##we are catcing, like we want
##but assumes that the page will not change

### how to solve this 'will not change' issue?
#### timeout

##and cache will get readlly large


## birthday paradox

#make a bunch of random keys
#hash them
#track them as we go
#stop when we get a collision

def hash_func(key):
    return int(hashlib.sha256(f'{key}'.encode()).hexdigest(), 16)

def how_many_before_collision(array_size):

    previous_keys = set()

    successful_hashes = 0

    while True:
        random_key = random.random()
        hashed_key = hash_func(random_key) % array_size

        if hashed_key not in previous_keys:
            previous_keys.add(hashed_key)

            successful_hashes += 1
        else: # collision
            break

    print(f'buckets {array_size}, tries {successful_hashes} before collision, {successful_hashes / array_size * 100}% full')

how_many_before_collision(8)