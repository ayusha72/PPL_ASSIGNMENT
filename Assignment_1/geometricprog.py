
a = int(input("Enter the first term :"))
r = int(input("Enter the ratio :"))
n = 10
def printgp(a, r, n):
    for i in range(0, n):
        curr_term = a * pow(r, i)
        print(curr_term, end =" ")

printgp(a, r, n)
