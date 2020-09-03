# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
#https://thispointer.com/python-map-function-explained-with-examples/
#https://openbookproject.net/thinkcs/python/english3e/lists.html

alphabet = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
             'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']


def letter_frequency(words, letters= alphabet):
    cache = {}
    for letter in words:
        if letter not in letters:
            continue
        if letter not in cache:
            cache[letter] = 1
        else:
            cache[letter] += 1
    return sorted(cache.items(), key=lambda x: x[1], reverse=True) #sort by value

def crack_ceasar(words):
    period = letter_frequency(words)
    match = {period[i][0]:alphabet[i]  #Dictionary
                for i in range (len(period))}
    emission = ''.join(map(lambda x: match[x] if x in match else x, words)) ## Reverse each string in the list using lambda function & map()
    print(emission)

if __name__ == "__main__":
    # access data cyphertext 
    with open('applications/crack_caesar/ciphertext.txt') as file:
        ciphertext = file.read()   
    print(crack_ceasar(ciphertext))