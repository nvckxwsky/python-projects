#testowanie if ,else if -elif i takie tam

menu = "Latte \n" + "Mielona \n" + "Zielona Herbatka \n"
print(menu)

order = input("Co podać: \n")
#print (order)

if order == "Latte":
    pianka = input("Z pianką czy bez: \n")
    if pianka == "z pianką":
        price = 11
        print("Latte z pianką kosztuje $11")
    else:
        price = 8
        print("Latte bez pianki kosztuje $8 ")
elif order == "Mielona":
    price = 6
elif order == "Zielona Herbatka":
    price = 5
else:
    price = 0 
    print("Sorry ale nie ma tego w naszym menu :(")

print(price)
    
