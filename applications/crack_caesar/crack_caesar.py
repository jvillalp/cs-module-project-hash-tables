
# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# #     Understand

# ## calculate frequency the amount of times each letter occurs
# ## create dic to count {letters, key value (letter count)}
# ## compare letter to percentage
# ## return decoded_text
# ## if letter shows up at a certain %, then it is prb the letter 'E'

tally_dic = {} #frequency of occurs of letters
decode_tble ={} #decoded letters

frequency_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

def get_message():
    with open("./applications/crack_caesar/ciphertext.txt") as f:
        inputfile = f.read()
        for char in inputfile:
            if char < 'A' or char > 'Z':
                continue
            if char in tally_dic:
                tally_dic[char] +=1
            else:
                tally_dic[char]= 1
        # print(tally_dic.items())
        #sort the items in asending order
        sorted_tally = sorted(tally_dic.items(), key= lambda x: x[1], reverse = True, )
        # print(sorted_tally)
        #time to assign each item to most frequently used word
        counter = 0
        for key, value in sorted_tally:
            decode_tble[key]= frequency_list[counter]
            counter += 1

        decoded_string = ''
        for char in inputfile:
            if char < 'A' or char > 'Z':
                decoded_string += char
                continue
            decoded_string += decode_tble[char]
        print(decoded_string)
        
get_message()

