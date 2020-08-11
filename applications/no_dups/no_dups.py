def no_dups(s):
    # Your code here
    words = s.split()
    #create set, only has items (no key.value pairs)
    visited = set()
    #empty array 
    res = []
    for word in words:
        if word not in visited:
            #add to array
            res.append(word)
            #add to set
            visited.add(word)
    return " ".join(res)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))