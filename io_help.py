file1 = "a_example.txt"
file2 = "b_read_on.txt"
file3 = "c_incunabula.txt"
file4 = "d_tough_choices.txt"
file5 = "e_so_many_books.txt"
file6 = "f_libraries_of_the_world.txt"

files = [file1, file2, file3, file4, file5, file6] 
 
 
def read_input(file):
    with open(file, 'r') as f:
        B, L, D = [int(x) for x in f.readline().split()]
        scores = [int(x) for x in f.readline().split()]
        libraries = []
        for i in range(L):
            line = [int(x) for x in f.readline().split()]
            temp = [line[1], line[2]]
            temp.append(sorted([(scores[int(x)], int(x)) for x in f.readline().split()],key = lambda x: (-x[0], x[1])))
            libraries.append(temp)
        return (B,L,D,scores,libraries)

def outputFile(arr, filename):
    f = open(filename, "w")
    f.write(str(len(arr)) + "\n")
    for x in arr:
        f.write(str(x[0]) + " " + str(len(x[1])) + "\n")
        for y in x[1]:
            f.write(str(y) + " ")
        f.write("\n")
    print(arr)
    f.close()
