def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

n = int(input())

list = list()
for i in range(n + 1):
    list.append(fib(i))

print(list[len(list)-1])
