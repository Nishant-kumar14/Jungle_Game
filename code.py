print("                                               Jungle Game                             ")
print("Once upon time a person is going to his friend's house in a car on the road.But his car's petrol is almost empty and in that road"
      "\nthere was a jungle so he think it might be shortcut. so he took a jungle's way after few distance he got two ways.Which road will he choose?")
print("press 1 for Left")
print("press 2 for Right")
road=int(input("choose a road"))
if(road==1):
    print("he choose to go to left and he got deep into the jungle and after sometime he found another two paths. which will you choose?")
    print("press 1 for Left")
    print("press 2 for Right")
    road=int(input("choose a road"))
    if(road==1):
        print("press 1 for Left")
        print("press 2 for Right")
        print("he choose to go to left and he hear a screaming of wild animals and after sometime his car stops and not start again because fuel is empty.After that he start walking in the jungle and after walking sometime he encounter a bear. he paniced and start running for his life. bear chasing him ""\nvery fast and he keep running then he fell from the cliff and died.")
        print("GAME OVER")
    elif(road==2):
        print("press 1 for Left")
        print("press 2 for Right")
        print("he choose to go to right and he hear a screaming of wild animals and after sometime his car stops and not start again because fuel is empty.After that he start walking in the jungle and after walking sometime he encounter a tiger. he panicked and start running for his life. tiger chasing him very fast and he keep running then a huge rock is blocking the road and he eaten by tiger and died.")
        print("GAME OVER")
    else:
        print("Invalid Number")
elif(road==2):
    print("he choose to go to right and he got deep into the jungle and after sometime he found another two paths. which will you choose?")
    print("press 1 for Left")
    print("press 2 for Right")
    road=int(input("choose a road"))
    if(road==1):
        print("press 1 for Left")
        print("press 2 for Right")
        print("he choose to go to left and he hear a screaming of wild animals and after sometime his car stops and not start again because fuel is empty.After that he start walking in the jungle after sometime he encounter a person with a gun he panicked and start running the opposit side but he shot by the gun man and died.")
        print("GAME OVER")
    elif(road==2):
        print("press 1 for Left")
        print("press 2 for Right")
        print("he choose to go to right and after some time  he encounter another two paths. which will you choose?")
        road=int(input("choose a road"))
        if(road==1):
            print("he choose to go to left and  he encounter a wild boar and chased by wild boar after that he will killed.")
            print("GAME OVER")
        elif(road==2):
            print("he choose to go to right and after some time he encounter a wounded man and he helps him. wounded man shows him a direction to get out of this""\njungle after go out of the jungle he go to hospital to help a wounded man and arrived his freind's home safely.")
            print("YOU WIN")
        else:
            print("Invalid Number")
    else:
        print("Invalid Number")
else:
        print("Invalid Number")

   
