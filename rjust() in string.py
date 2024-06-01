# rjust() is used to right align strings

first_case = True
while True:
    n = int(input())
    if n == 0:
        break

    if not first_case:
        print()  # Add an empty line between test cases
    first_case = False

    lis = []
    for i in range(n):
        s = input()
        lis.append(s)
    
    max_len = len(max(lis, key=len))
    
    for i in lis:
        print(i.rjust(max_len))
