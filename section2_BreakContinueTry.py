

# try...except...finally

a = 0
b = 15


def a_over_b(a, b):
    try:
        a/b
    except ZeroDivisionError:
        print("ERROR: Div 0")
    finally:
        print("Finally Always Runs")

    return a/b


print("Try Statement")
while a < 4:
    print("-------")
    a += 1
    b -= 1
    try:
        print("a = {0}, b = {1}, result = {2}".format(a, b, a_over_b(a,b)))
    except:
        print("Exception in while")
        # continue # finally will always run
        break
    finally:
        print("Finally ALWAYS Executes event with a continue")

    # If the except continue is executed this print will not be run.
    print(a,b," =")
else:
    print("While loop completed without any break")