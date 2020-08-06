import random
import re

# Read in all the words in one go
# TODO: analyze which words can follow other words
# Your code here
# TODO: construct 5 random sentences
# Your code here

d = {}

with open('applications/markov/input.txt') as f:
    words = f.read()
split_words = words.split()
print(words)

dataset = {}

for i in range(len(split_words) -1): #pass dataset into dictionary
    word = split_words[i]
    next_word = split_words[i + 1]
    if word not in dataset:
        dataset[word] = [next_word]
    else:
        dataset[word].append(next_word)
print(dataset)

start_words = []

for key in dataset.keys(): # words list
    if key[0].isupper() or len(key) >1 and key[1].isupper():
        start_words.append(key)
word = random.choice(start_words)

stopped = False
stop_signs = "?.!"
while not stopped:
    print(word)
    if word[-1] in stop_signs or len(word) > 1 and word[-2] in stop_signs:
        stopped = True
    following_words = dataset[word]
    word = random.choice(following_words)


# TODO: analyze which words can follow other words
word_dic = {}

words = words.split()

for i, word in enumerate(words[:-1]):
    if word in word_dic:
        word_dic[word] = word_dic[word] + [words[i+1]]
    else:
        word_dic[word] = [words[i+1]]

# TODO: construct 5 random sentences

start_words = []
stop_words = []
pattern_1 = '[A-Z]+[a-z]'
pattern_2 = '["]+[A-Z]+[a-z]'
pattern_3 = '[.?!]$'
pattern_4 = '[.?!]+["]$'
for key in word_dic:
    if re.search(pattern_1, key) or re.search(pattern_2, key):
        start_words.append(key)
    if re.search(pattern_3, key) or re.search(pattern_4, key):
        stop_words.append(key)

def make_sentence():
   
    stop_word = False
    word = random.choice(start_words)
    sentence = word
    if word in stop_words:
        return sentence
    
    while stop_word is False:
        word = random.choice(word_dic[word])
        
        sentence = sentence + " " + word
        
        if word in stop_words:
            stop_word = True
    
    return sentence

print(make_sentence())
print(make_sentence())
print(make_sentence())
print(make_sentence())
print(make_sentence())