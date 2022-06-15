from time import sleep  # time module
import database

# Main section
#<---------------------------------------------------------------------------------------------------
def decorator(func):
    def wrapper(*args, **kwargs):
        print("------------------Please wait-------------------")
        sleep(1.5)
        func(*args, **kwargs)
        print("---------------------Done-----------------------")
    return wrapper

#<---------------------------------------------------------------------------------------------------


def getshops(item):
    return database.eval(item)
# function adds anything we want to write in the database...
# the "new" parameter is the information we want to add to the database
def update(new):
    file = open("database.py", "a")
    file.write(new)
    file.close()
    return "Done"


# this function gets the infomation about the shop from the database
def get_shop(shop_name):
    return eval(f'database.{shop_name}')

#this function is for changing details 
@decorator
def change_detail(shop_name, detail, prev, new_detail):
    change = "\n%s['%s'] = '%s'" % (shop_name, detail, new_detail)
    update(change)
    if detail == "shop_name":
        new_list = "\nall_shops = [x for x in all_shops if x != '%s']" % prev
        add_to_list = "\nall_shops.append('%s')" % (new_detail)
        update(add_to_list)
        update(new_list)

@decorator
def add_shop():
    shop_name = input("Enter the shop's name NB. please no space: \n")
    shopid = input("Enter shop id: \n")
    shop_specialties = input('What are the specialties of the shop? \n')
    file = open("file", "a")
    if shop_name not in database.all_shops:
        add_shop_details = "\n%s = {'shop_name': \'%s\',  'shopId': \'%s\', 'shop_specialties': \'%s\'}" \
             % (shop_name, shop_name, shopid, shop_specialties)
        # this adds the shop to all_shops
        add_to_list = "\nall_shops.append('%s')" % (shop_name)
        update(add_to_list)
        update(add_shop_details)
        file.close()
    else:
        file.close()
        sleep(1.5)
        print("Shop already exists")


# this function removes shop
@decorator
def remove_shop(shop_name):
    # it first removes shop from the main list
    action = "\nall_shops = [x for x in all_shops if x != '%s']" % shop_name
    update(action)


