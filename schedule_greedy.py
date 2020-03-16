from io_help import read_input
from sortedcontainers import SortedList


def schedule_greedy(file, avg_score):
    #Parse input
    B,L,D,scores,libraries = read_input(file)
    
    #Initialize variables
    visited, total_signup = [False] * B, 0
    output = []
    total_score = 0

    #Greedy scheduling
    #Schedule libraries based on precieved possible value for library
    for library in sorted(libraries, key = lambda x: x[0]/x[1]):
        #Init variables
        current_score = 0
        visited_set = set()
        
        #No more days, finished
        if total_signup >= D: break
    
        #Init more variables
        output.append([library[3], []])
        total_signup += library[0]
        books = library[2]
        days = D - total_signup - 1
        counter, pos = 0, 0
        
        #Looping through the books of library
        while counter <= library[1] * days and pos < len(books):
            #Checkout if book has not ben sen
            if not visited[books[pos][1]]:
                visited[books[pos][1]] = True
                visited_set.add(books[pos][1])
                output[-1][1].append(books[pos][1])
                counter += 1
                total_score += books[pos][0]
                current_score += books[pos][0]
            pos += 1
            
        #Calculate precieved possible value for library
        if current_score < avg_score/2: 
            output.pop()
            total_signup -= library[0]
            
            #Ignore seen books in value calculation
            for book in visited_set:
                visited[book] = False
            
    return (output, total_score)
