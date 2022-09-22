''' Restaurant app
 1. Create menu price dictionray and define tax value
 1. Design module of menu select ( use recursion if invalid menu selected until correct menu select)-> menu option
 2. Design module of tip select ( use recursion if invalid menu selected until correct tip option/value select)-> tip percentage/ custom tip ($)
 3. Loop for menu selection until customer finish-> create a selected menu list
 4. Loop through selected menu list and accumulate total prices from menu price dictionary
 5. Calculate total price after tax
 6. Calculate total price after tip
'''
# Author: Cuong Bui - Cloud Big Data Innovation
menu_price_dict = {'1': 25, '2': 7, '3': 12, '4':13, '5':23}
tax = 0.13
def menu_select():
    menu_no = input(f"Enter menu[1-5] or 0 to finish: \n" \
                     f"- Menu 1: $25\n" \
                     f"- Menu 2: $7\n" \
                     f"- Menu 3: $12\n" \
                     f"- Menu 4: $13\n" \
                     f"- Menu 5: $23\nMenu:")
    try:
        if 5< int(menu_no) or  int(menu_no)<0:
            print("Invalid menu, please re input menu")
            menu_no = menu_select()
    except:
        print("Invalid menu, please re input menu")
        menu_no = menu_select()
     
    return menu_no

def custom_tip():
    val = input("Input custom tip ($):")
    try:
        if int(val) and int(val) <0:
            print("Invalid tip value input, please re input tip value")
            val = custom_tip()
         
    except:
        print("Invalid tip value input , please re input tip vaue")
        val = custom_tip()
    return int(val)

def tip_select():
    tip_percent = tip_value = 0
    tip_opt_dict = {'1': 0.05, '2': 0.1, '3': 0.15, '4': 0.20}
    tip_opt = input("Menu tip:\n [1. 5%, 2. 10%, 3. 15%, 4. 20%, 5. custom tip]\nTip Option:")
    try:
        if int(tip_opt) <1 or 5< int(tip_opt):
            print("Invalid tip option {}, please re input menu".format(tip_opt))
            val = tip_select()
        if int(tip_opt) == 5:
            tip_value = custom_tip()
            print("You input tip ${}".format(tip_value))
        else:
            tip_percent = tip_opt_dict[tip_opt]
            print("You selected tip option {}({}%)".format(tip_opt, tip_opt_dict[tip_opt]*100))
        
        
    except:
        print("Invalid tip option {}, please re input tip".format(tip_opt))
        tip_opt = tip_select()

    return tip_percent, tip_value
ord_no = 0
menu_list = []
print('Welcome to Restaurant ABC. Hope you have a greate day.....')
print('-'*30)
while (True):
    ord_no +=1
    print("- Order # {}:".format(ord_no))
    menu_no = menu_select()
    print('-'*20)
    if int(menu_no) == 0:
        break
    menu_list.append(menu_no)
tip_percent = tip_value  = 0
print('-'*30)
print('Billing.....')
if menu_list:
    tip_percent, tip_value  = tip_select()
    
    print('-'*20)
price = total_price = 0
for i, menu in enumerate(menu_list):
    price = menu_price_dict[menu]
    print('Order # {} - Menu # {}, price: ${}'.format(i, menu, price))
    total_price += price
print('-'*20)
print('Number Orders # {}, Total price: ${}'.format(len(menu_list), total_price))
print('-'*30)

print("Tax: {}* {}%={}".format(total_price, tax*100, total_price*tax))
print('-'*30)
print("Total price after Tax: ${}".format(total_price + total_price*tax))
if tip_percent > 0:
    print("Tip: {}*{} % = ${}".format(total_price, tip_percent*100, total_price*tip_percent ))
else:
    print("Custom Tip: ${}".format(tip_value))
print("Total price after Tip: ${}".format(total_price + total_price*tax + total_price*tip_percent + tip_value))
print("Thank you and See you again!")


