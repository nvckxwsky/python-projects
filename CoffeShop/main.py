#no ogólnie coffeshop ziomeczku pijesz kawusie lub palisz zielone jak jesteś in holandia B)

#przywitanie
print("Siema siema kurwa witam")

name = input("Jak sie nazywasz szefie ? B) \n")

#if statement

if name == "Drakula" or name == "Impostor":
    check = input("ale ty prawdziwy? tak lub nie \n")
    good_shit = int(input("w skali od 1 do 10 jak kochasz lukiego oooo? \n"))

    if check == "tak" and good_shit < 9:
        print("Kawusia smakuwa,jebać " + name)
        exit()
    else:
        print("a no to gituwa B)")
else:
    print("\n\nnoo siema "+name+' witaj w najbardziej zajebistym coffeshopie B)\n')        

    


    

    


#print(name+"\nkozackie imie ziomuś B)")


#Menu
menu = "1. dobra kawusia \n"+"2.blancior gigancior \n"+"3.kawusia i blancior \n"+"4.specjał drakulsona\n"+"5.horny t h i c c baristka"
print("w dzisiejszym menu oferujemy\n"+menu+"\n\n ")

#składanie oferty
order = input("więc co podać szefie?\n")
if order == "5":
    print("mmm dobry wybór ale kosztuje ona $20")
    price = 20
    amount = input("na jak długo ma się zająć tobą nasza baristka? B) psst...czas oczywiście w godzinkach \n")
    result = int(amount) * price


else:
    print("smaczna kawusia u nas zawsze za piątaka B)")
    price = 5
    amount = input("a ile sobie tego życzysz?\n")
    result = int(amount) * price



#print("\n"+order+",dobry wybór "+name+" B)")





print("więc będzie "+order+" "+amount+" razy/godziny "+"\n\n więc razem to będzie $"+str(result)+"\n\ndzisiaj przyjmujemy płatność tylko ziom-kartą")










#Podstawa Zmiennych
#name = "ziomczek z pomoża"
#print(name)
#name = "ziomczek z pomoża v2"
#print(name)

