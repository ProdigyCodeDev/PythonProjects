#databbase list
brands = [ 'Toyota', 'Tesla', 'Nisan']
models = ['Camry', 'Model 3', 'Rogue']

access = [ 'Access', 'access']
add = ['Add', 'add']
remove = ['Remove', 'remove']

# adding inventory
# certified working
def adding():
    added_brand = input("Please enter brand to add: ")
    brands.append(added_brand)
    added_model = input("Please enter model to add: ")
    models.append(added_model)
    print("Updated brands: ")
    u = brands.copy()
    print(u)
    print("Updated models: ")
    y = models.copy()
    print(y)


# removing inventory
# certified working
def removing():
    removed_brand = input("Please enter brand to remove: ")
    brands.remove(removed_brand)
    removed_model = input("Please enter model to remove: ")
    models.remove(removed_model)
    print("Updated brands: ")
    p = brands.copy()
    print(p)
    print("Updated models: ")
    o = models.copy()
    print(o)

#accessing inventory
#certified working
def accessing():
    brand_choice = input("Please enter brand of car:  ")
    if brand_choice in brands:
        print("Available")
    else:
        print("unavailable")

    model_choice = input("Please enter model of car:  ")
    if model_choice in models:
        print(brand_choice + "  " + model_choice + " is available")

#starting program
#certified working
def dealership():
    action = input("Access inventory, add car, or remove car")

    if action in add:
        adding()
    if action in remove:
        removing()
    if action in access:
        accessing()
    repeat = input("Run again?")
    if repeat in ('yes', 'again', 'repeat'):
        dealership()
dealership()

