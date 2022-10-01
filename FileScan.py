import random

# certified working
def search():
    with open(r'WordBank.txt', 'r') as file:
        content = file.read()
        word = input("Please enter desired word:    ")
        if word in content:
            print(word + " found")
        else:
            print(word + " not found")

# certified working
def random_word():
    with open(r'WordBank.txt', 'r') as file:
        words = file.readlines()
        word = random.choice(words).strip()
        print(word)

#  certified working
def edit():
    file = (r'WordBank.txt', 'a')
    with open(r'WordBank.txt', 'a') as file:
        file_changes = input("Please enter changes to add    :")
        file.write(file_changes)

# certified working
def retrieve():
    file = open(r'WordBank.txt')
    file_contents = file.read()
    print(file_contents)




# loop function
def repeat():
    x = input("Run again? y/n")
    yes = ["y"]
    no = ["n"]
    if x in yes:
        start()
    if x in no:
        exit()

# certified working
search_triggers = ["search", "Search", "scan", "Scan"]
random_triggers = ["random", "Random", "randomize", "Randomize"]
edit_triggers = ["edit"]
read_triggers = ["read"]
delete_trigger = ["delete", "remove"]

# certified working
def start():
    operation = input("Please choose to search or randomize word:    ")
    if operation in search_triggers:
        search()
        repeat()
    if operation in random_triggers:
        random_word()
        repeat()
    if operation in edit_triggers:
        edit()
        repeat()
    if operation in read_triggers:
        retrieve()
        repeat()
    if operation in delete_trigger:
        delete()
        repeat()
start()


