# Begins here
def fibonacci(i):
    a = 1
    b = 1
    c = 2

    print(a)
    print(b)
    print(c)

    i -= 3

    while i > 0:
        a = b + c
        b = c
        c = a

        i -= 1

        print(c)


# Ends here
i = int(input("Type the index of Fibonacci Sequence desired: "))

# Just a test below
fibonacci(i)

print("End of program :D")
