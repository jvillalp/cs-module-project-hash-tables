# Your code here

def count_words():
    ignore_char = '\":;,.-+=/\|[]{}()*^&'

    wordmap = {}

    with open("./applications/histo/robin.txt") as f:
        words = f.read().lower()
        for char in ignore_char:
            words = words.replace(char, "")
        words = words.split()

    for word in words:
        if word in wordmap:
            wordmap[word] += 1
        else:
            wordmap[word] = 1
    return wordmap

def render_word_count(dic):
    counts = [(dic[word], word) for word in dic]
    counts.sort(key = lambda e: (-e[0], e[1]))

    maxlength = 0

    for word in counts:
        if len(word[1]) > maxlength:
            maxlength = len(word[1])

    for word in counts:
        print(f'{word[1]}\t' .expandtabs(maxlength +2) + "#" * word[0])

render_word_count(count_words())
