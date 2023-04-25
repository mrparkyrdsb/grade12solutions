''' Input Handling
target = int(input())
amount = input() # number of clubs
clubs = []
for _ in range(amount):
    clubs.append(int(input()))

# clubs = [int(input()) for _ in range(amount)] # short form
'''

target = 10 # Set Target Distance
clubs = [3,6,1] # List of Available Clubs

max_stroke = 0 # Variable for the worst possible answer
possible_solution = True # Checking for impossible solutions

if target % min(clubs) == 0:
    max_stroke = target // min(clubs) + 1
    # maximum swing amount is calculated by dividing the target distance by the smallest club
else:
    max_stroke = int(target/min(clubs)) + 1
    possible_solution = False 
    # when the smallest club cannot reach the target distance, there is a potential for impossible solution

# Handling Base Cases
if target in clubs:
    # if the target distance can be fully reached by a single swing
    print('Roberta wins in 1 stroke.')
elif min(clubs) > target:
    # if the smallest club hits further than the target distance
    print("Roberta Acknowledges Defeat.")
else:
    # All other scenarios
    distance_table = [0] + [max_stroke for _ in range(target)]
    ''' # Long Form:
    distance_table = [0]
    for _ in range(target):
        distance_table.append(max_stroke)
    ''' 
    # Explanation: 
    # We are to determine that each distance from 1 to target can be reached by swinging the maximum amount of strokes.
    # We are to then traverse to each distance from zero and update the minimum number of swings to get there.
    # By starting at distance of 1, we can build up towards the target
    
    for location in range(len(distance_table)): # look at each distance of 0, to target
        for club in clubs: # we grab each club
            new_location = location + club # we look at the new distance we land at from the current location by swinging the club
            if new_location < len(distance_table):
                # Some things we need to consider
                # 1. the new_location cannot go over our target distance
                # 2a. we either maintain the number of swing the new_location currently has OR
                # 2b. we update it with swing number of current location and add 1
                distance_table[new_location] = min(distance_table[new_location], distance_table[location] + 1)
    
    if not possible_solution and distance_table[-1] == max_stroke:
        print("Roberta Acknowledges Defeat.")
    else:
        print(f'Roberta wins in {distance_table[-1]} strokes.')
