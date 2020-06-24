import time

f = open("FibonacciOutput.txt", "w+")

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
    
    f.write(str(c) + "\n")


# Ends here
i = int(input("Type the index of Fibonacci Sequence desired: "))

inicial = int(time.strftime("%S", time.localtime())) + 60 * int(time.strftime("%M", time.localtime())) + 3600 * int(time.strftime("%H", time.localtime()))

# Just a test below
fibonacci(i)

print("End of program :D")

final = int(time.strftime("%S", time.localtime())) + 60 * int(time.strftime("%M", time.localtime())) + 3600 * int(time.strftime("%H", time.localtime())) - inicial

print("Elapsed time: " + str(final) + " second(s)")
