import random

# Read in all the words in one go
with open("./applications/markov/input.txt") as f:
    words = f.read().split()
    # print(words)

# TODO: analyze which words can follow other words
# Your code here
mark_storage = dict()
start_words = list()
stop_words = list()
capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '"']
ends = ['.', '?', '!', '"']

for i in range(len(words)- 1):
    if words[i][0] in capitals:
        start_words.append(words[i])
    if words[i][-1] in ends:
        stop_words.append(words[i])
        #.get: get key of value
        ##works if you dont have to compute to a string
    mark_storage[words[i]] = mark_storage.get(words[i], [])
    mark_storage[words[i]].append(words[i +1])

# print(start_words)


# TODO: construct 5 random sentences
# Your code here

for i in range(4):
    sentence = ""
    start = random.choice(start_words)
    sentence += start + " "
    #finding start value inside value of storage
    next_word = random.choice(mark_storage[start])
    
    while start not in stop_words:
        if next_word in stop_words:
            sentence += next_word
            break
        sentence += next_word + " "
        next_word = random.choice(mark_storage[next_word])
    print(sentence)