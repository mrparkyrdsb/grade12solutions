# Q9) Project Euler (Q24) - Lexicographic permutations

# The Answer: 2783915460

# generate random numbers from 1 to 9 for each digit of the number

# find all the iterations, put them in a list, sort it, list[1000001]

digits = '012'
permutations = set(digits)
length = len(digits)
pattern_length = 0

while pattern_length != length:
    new_set = set()
    for current_pattern in permutations:
        for i in digits:
            if i not in current_pattern:
                new_pattern = current_pattern + i
                new_set.add(new_pattern)
                pattern_length = len(new_pattern)
                
    permutations = new_set

permutations = sorted(permutations)
print(permutations)

