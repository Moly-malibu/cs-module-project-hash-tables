# Your code here
#https://careerkarma.com/blog/python-sort-a-dictionary-by-value/#:~:text=To%20sort%20a%20dictionary%20by%20value%20in%20Python%20you%20can,Dictionaries%20are%20unordered%20data%20structures.
#https://pythonexamples.org/python-count-number-of-words-in-text-file/
#https://stackoverflow.com/questions/21107505/word-count-from-a-txt-file-program
#https://www.pythonforengineers.com/create-a-word-counter-in-python/

# Implement me.
import re
import random

#Get data and cound words:
with open('applications/histo/robin.txt') as file:
    word = file.read() 
    split_words = word.split()
print(word)
print('number of words in text file:', len(split_words))

#Data into dictionary
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

#histogram
wordCounter = {}

with open('applications/histo/robin.txt','r') as fh:
  for line in fh:
    word_list = line.replace(',','').replace('\'','').replace('.','').lower().split() #split line into list
    for word in word_list:
      if word not in wordCounter: #add word into dictionary
        wordCounter[word] = 1
      else:
        wordCounter[word] = wordCounter[word] + 1 #update count

print('{:15}{:3}'.format('Word','Count'))
print('-' * 18)
for  (word,occurance)  in wordCounter.items(): #occurrence
  print('{:15}{:3}'.format(word,occurance))

def main():
  for line in word:
    robin_hist = int(line)
    robin.incCount(count_words(robin_hist))
    print(robin)
    
#Histogram
count = {}
f = open('applications/histo/robin.txt')
text = f.read().lower()
f.close()
text = re.sub('[^a-z\ \']+', " ", text)
words = list(text.split())
word_count = {}
word_set = set(words)
for word in word_set:
    word_count[word] = "#" * words.count(word)
items = list(word_count.items())
items.sort()
items.sort(key=lambda x: x[1], reverse= True)
for item in items:
    print(f'{item[0]:{17}}{item[1]}')
