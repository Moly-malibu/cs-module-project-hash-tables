"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))

q = (1,3,4,7,12)

def f(x):
    return x * 4 + 6

# Your code here

values = {}
sums = {}
diffs = {}

for num in q:
    values[f'f({num})'] = f(num)
for value1 in values:
    for value2 in values:
        sums[f'{value1} + {value2}'] = ((values[value1] + values[value2]), f'{values[value1]} + {values[value2]}')
        if values[value1] >= values[value2]:
            diffs[f'{value1} - {value2}'] = ((values[value1] - values[value2]), f'{values[value1]} - {values[value2]}')                 

for sum_ in sums:
    for diff in diffs:
        if sums[sum_][0] == diffs[diff][0]:
            print(f'{sum_} = {diff} {sums[sum_][1]} = {diffs[diff][1]}')