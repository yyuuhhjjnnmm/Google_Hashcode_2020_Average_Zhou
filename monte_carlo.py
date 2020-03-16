import random
from collections import defaultdict
from io_help import read_input


def monte_carlo(file):
    #Parse input
    B,L,D,scores,libraries = read_input(file)
    
    #Initialize variables
    visited, total_signup = [False] * B, 0
    output = []
    total_score = 0
    
    # Randomize the libraries to sign up
    indices = list(range(L))
    random.shuffle(indices) 

    #Looping through libraries
    for index in indices:
        library = libraries[index]
        total_signup += library[0]
        
        #No more days, finish func
        if total_signup >= D: break
    
        #Sign up the library
        output.append([index, []])
        books = library[2]
        
        #Decrement days counter
        days = D - total_signup - 1
        
        #For each signed up library, check out books
        counter, pos = 0, 0
        while counter <= library[1] * days and pos < len(books):
            if not visited[books[pos][1]]:
                #A new book to sign out
                visited[books[pos][1]] = True
                output[-1][1].append(books[pos][1])
                counter += 1
                total_score += books[pos][0]
            pos += 1
        
        #Exit and return
        if len(output[-1][1]) == 0: output.pop()
    return (output, total_score)
