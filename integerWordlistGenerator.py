n = 0
m = 0
def num(n,m):
    #using "w" to write in to a new text file and to append to existing file use "a"
    with open("password1.txt", "w") as f:   
        for i in range(n, m+1):
            f.write(str(n) + "\n")
            n+=1

n = int(input("Enter the proceeding num: "))
m = int(input("Enter the ending num: "))

num(n,m)
