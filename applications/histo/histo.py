# Your code here
#https://careerkarma.com/blog/python-sort-a-dictionary-by-value/#:~:text=To%20sort%20a%20dictionary%20by%20value%20in%20Python%20you%20can,Dictionaries%20are%20unordered%20data%20structures.
#https://pythonexamples.org/python-count-number-of-words-in-text-file/
#https://stackoverflow.com/questions/21107505/word-count-from-a-txt-file-program
#https://www.pythonforengineers.com/create-a-word-counter-in-python/

with open('applications/histo/robin.txt') as file:
    robin = file.read() 
print(robin)
words = robin.split()
print('number of words in text file:', len(words))

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


def count_words(robin):
    words = robin.split(' ')
    num_words = len(words)
    return num_words
print(count_words)


def count_lines(robin):
   lines = robin.split("\n")
   for l in lines:
      if not l:
         lines.remove(l)
 
   return len(lines)

if __name__=="__main__":
    num_words = count_words(robin)
    num_lines = count_lines(robin)
 
print("The number of words: ", num_words)
print("The number of lines: ", num_lines)


def main():
  for line in robin:
    robin_hist = int(line)
    robin.incCount(count_words(robin_hist))
    print(robin)


import pandas
from collections import Counter

letter_counts = Counter(robin)
df = pandas.DataFrame.from_dict(letter_counts, orient='index')
df.plot(kind='bar')


import matplotlib.pyplot as plt 
import numpy as np
labels, counts = np.unique(robin,return_counts=True)
ticks = range(len(counts))
plt.bar(ticks,counts, align='center')
plt.xticks(ticks, labels)

import matplotlib.pyplot as plt
import numpy as np

letters_hist = Counter(robin.lower().replace('\n', ''))
counts = letters_hist.values()
letters = letters_hist.keys()

# graph data
bar_x_locations = np.arange(len(counts))
plt.bar(bar_x_locations, counts, align = 'center')
plt.xticks(bar_x_locations, letters)
plt.grid()
plt.show()

# Creating histogram 
fig, ax = plt.subplots(figsize =(10, 7)) 
ax.hist(robin, bins = [0, 25, 50, 75, 100]) 
  
# Show plot 
plt.show()


plt.hist(robin,5, histtype='step', align='mid', color='g', label='Test Score Data')
plt.legend(loc=2)
plt.title('Histogram of score')
plt.show()