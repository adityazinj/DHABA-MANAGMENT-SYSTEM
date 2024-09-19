
menu={'BUTTER CHICKEN':349
      ,'CHIKEN BIRYANI':149
      ,'PANIR ANGARA':249
      ,'PANIR TIKKA':299}
print("WELCOME TO ADITYA DA DHABA")
print("MENU"":-\n""BUTTER CHICKEN:Rs349\nCHICKEN BIRYANI:Rs149\nPANIR ANGARA:Rs249\nPANIR TIKKA:Rs299")

order_item=0

item_1=input("PLEASE ENTER THE ITEM NAME THAT YOU HAVE TO ORDER:")
if item_1 in menu:
    order_item += menu[item_1]
    print(f"YOUR ORDER OF {item_1} IS SELECTED!")
 
else:
    print("SORRY THE ITEM YOU ENTER IS NOT AVAILABLE NOW!")

order=input("DO YOU WANT TO ORDER ANOTHER ITEM ? (YES/NO):")
if order=="YES":
    item_2=input("PLEASE ENTER THE ITEM NAME THAT YOU HAVE TO ORDER:")
    if item_2 in menu:
        order_item+=menu[item_2]
        print(f"YOU HAVE TO PAY FOR {item_1} AND {item_2} IS :RS {order_item}")
         
        print("WAIT FOR 5-10MIN AFTER COMFIRMED THE ORDER")
        print("THANKS FOR VISIT")

    else:
        print(f"SORRY THE ITEM YOU ENTER IS NOT AVAILABLE NOW!\nSO YOU HAVE TO PAY FOR {item_1} IS :RS {order_item}")
    
else:
    print(f"SO YOU HAVE TO PAY FOR {item_1} IS :RS {order_item}")
     
    print("WAIT FOR 5-10MIN AFTER COMFIRMED THE ORDER")
    print("THANKS FOR VISIT")
