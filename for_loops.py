# Die Counter
import random

# Initialize counters
count_6 = 0
count_1 = 0
count_two_6s_in_a_row = 0

# Number of times to roll the die
num_rolls = 20

# Previous roll (to check for two 6s in a row)
previous_roll = None

# Simulate rolling the die
for _ in range(num_rolls):
    roll = random.randint(1, 6)  # Roll the die (random number between 1 and 6)
    
    if roll == 6:
        count_6 += 1
        if previous_roll == 6:
            count_two_6s_in_a_row += 1
    if roll == 1:
        count_1 += 1
    
    # Update previous roll
    previous_roll = roll

# Print statistics
print(f"Number of times rolled a 6: {count_6}")
print(f"Number of times rolled a 1: {count_1}")
print(f"Number of times rolled two 6s in a row: {count_two_6s_in_a_row}")


# Jamping Jacks 

# Initialize Jumps
num_jumps = 0
total_jumps = 100
stopped_early = False

input('Press Enter to Start.')
for jumps in range(1, 101):
    #print(jumps % 10)
    if jumps % 10 == 0:
        num_jumps += 10
        #print(num_jumps)
        check_tiredness = input('Are you tired? ').lower()
        if check_tiredness == 'yes':
            stop_jumps = input('Do you want to skip the remaining sets? ').lower()
            if stop_jumps == 'yes':
                stopped_early = True
                break
            else:
                print(f'{100 - num_jumps} jamping jacks are remaining')
                
# Check if loop was stopped early
if stopped_early:
    print(f'You completed a total of {num_jumps} jumping jacks')    

else:
    print('Congratulations! You completed the workout')    