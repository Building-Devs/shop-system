
from database import *
from functions import change_detail, get_shop, remove_shop, add_shop, getshops


def main():
    print('Welcome to Group 8 mall system\n'
            '1.View current shops\n'
            '2.Delete a shop\n'
            '3.Add shop\n'
            '4.Update a shop detail\n'
            '5.Get shop details\n\n')
    try:
        selection = int(input('What would you like to do?\n'))
    except:
        print("Invalid Selection")

    #<---------------------------------------------------------------------------------------------------
    if selection == 1:
        print('Here are our current shops\n')
        print(*all_shops)

    elif selection == 2:
        print('Which shop would you like to delete?\n')
        print(*all_shops)
        print("--------------------------------------------------\n")
        shops = all_shops
        name = input('Enter the name of the shop you would like to delete:\n')
        if name in shops:
            remove_shop(name)
        else:
            print("Shop is not in the database")

    elif selection == 3:
        add_shop()

    elif selection == 4:
        print(*all_shops)
        print("------------------------------------------------------\n")
        name = input("Enter the name of the shop you'd like to update\n")
        if name in all_shops:
            try:
                print(*pres)
                action = input("What will you like to change:\n")
                detail = str(shop_details[str(action)])
                keys = str(eval(f'{name}'))
                prev_value = eval(name).get(detail)
                print("It previous value was  -----> " + prev_value)
                new_detail = input("Enter the new value: \n")
                try:
                    change_detail(name, detail,prev_value, new_detail)
                except:
                    print("Operation unsucessful!")
            except KeyError as err:
                print("Invalid Input!!!")
                exit()
        else:
            print("Shop does not exits in database")

    elif selection == 5:
        print(*all_shops)
        name = input("Enter the name of the shop: \n")
        try:
            print(get_shop(name))
        except:
            print("Shop does not exist in database")

    #<---------------------------------------------------------------------------------------------------

    else:
        print('Invalid Selection')



if __name__ == "__main__":
    password = "group8"
    passw = input("Enter password: \n")
    if passw == password:
        main()
    else:
        print("Wrong password")