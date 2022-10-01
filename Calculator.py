
def addition():
    x = int(input("Please enter Number 1"))
    y = int(input("Please enter Number 2"))
    result = x+y
    print(result)
    c = input("Run again?")
    if c in('yes', 'Again'):
        addition()
    if c in ('end', 'no', 'stop'):
        quit()
    else:
        print("invalid input")

p = input("Please choose an operation: ")
if p in ('add', 'plus'):
    addition()
else:
    print("invalid input")