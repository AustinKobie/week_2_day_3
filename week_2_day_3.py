# 1) Build a Shopping Cart
# You can use either lists or dictionaries. The program should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list

shopping_cart = {}


def store_shopping_cart(section, things):
    shopping_cart[section] = things


def build_shopping_cart():
    while True:
        section = input('What section would you like to go?')
        things = input('What would you like to add to your shopping cart?')

        store_shopping_cart(section, things)

        dele = input(
            'Do you want to delete anything from this shopping cart (y/n)?')

        if dele == 'y':
            dele_item = input('What item would you like to delete?')
            del shopping_cart[dele_item]

        cont = input('Would you like to continue (y/n)?')

        if cont == 'n':
            break
        print(shopping_cart)
    print(shopping_cart)


build_shopping_cart()

