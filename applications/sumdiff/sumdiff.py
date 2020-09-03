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
results = {}
sums = {}
rests = {}

for num in q:
    results[f'f({num})'] = f(num)
for results_1 in results:
    for results_2 in results:
        sums[f'{results_1} + {results_2}'] = ((results[results_1] + results[results_2]), 
            f'{results[results_1]} + {results[results_2]}')
        if results[results_1] >= results[results_2]:
            rests[f'{results_1} - {results_2}'] = ((results[results_1] - results[results_2]), 
            f'{results[results_1]} - {results[results_2]}')                 

for sum_ in sums:
    for rest in rests:
        if sums[sum_][0] == rests[rest][0]:
            print(f'{sum_} = {rest} {sums[sum_][1]} = {rests[rest][1]}')