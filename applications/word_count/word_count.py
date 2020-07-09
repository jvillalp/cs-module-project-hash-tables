def word_count(s):
    # Your code here
    for char in "\":;,.-+=/\|[]{}()*^&":
        s = s.replace(char, "")
    
    words = s.split()
    res = {}
    for word in words:
        w = word.lower()
        if w in res:
            res[w] += 1
        else:
            res[w] = 1
    return res

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))