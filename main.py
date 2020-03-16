#Google Hashcode 2020 Qualifier Round
#Team: Average Joe's
#Members: David Zhou, Luka Filipovic, Ted Clancy, Viktor Zhou
#Date: February 20th, 2020
#Question: Library sign up, book sign out, maximize book scores

from monte_carlo import monte_caro
from schedule_greedy import schedule_greedy
from io_help import outputFile

#Converting file names for output
def conv(num):
    return chr(ord('a')+num)

#Hardcoded averages for tinkering
avg_scores = [10.5, 64698.88, 4153.32, 276.674, 28451.94, 137191.7]

#Main loop
for i in range(6):
    max_score = 0
    
    #Loop through each test case
    for step in range(1):
        #mc = monte_carlo(files[i])
        mc = schedule_greedy(files[i], avg_scores[i])
        arr = mc[0]
        score = mc[1]
        
        #Output if better
        if score > max_score:
            max_score = score
            outputFile(arr, conv(i) + ".out")
            
        #Output for debug
        print(i, step, max_score, max_score / len(arr))
        total_score += max_score
        
print(total_score)
