#Breytur
cumulative_total = 0    #Summa allra talna sem fram koma
largest_number = 0      #Stærsta tala allra talna sem fram koma
odd_count = 0           #Heldur utan um fjölda oddatalna
even_count = 0          #Heldur utan um fjölda sléttra talna
x = int(input("Enter an integer: "))  #Fáum tölu frá notanda

while(x > 0):   #Lykkjan keyrir svo lengi sem innsláttna talan er jákvæð
    cumulative_total += x
    print("Cumulative total: {}".format(cumulative_total))

    if x%2:  #Athugum hvort talan er slétt eða oddatala og bætum við tilsvarandi count
        odd_count += 1
    else:
        even_count += 1

    if x > largest_number: #Athugum hvort gefin tala er stærst, ef svo geymum við hana
        largest_number = x
    x = int(input("Enter an integer: " ))
    if x <= 0:   #Athugum hvort nýja gildi x er jákvæð tala, annars prentum við út heildar útkomu
        print("Largest number: {}".format(largest_number))
        print("Count of even numbers: {}".format(even_count))
        print("Count of odd numbers: {}".format(odd_count))
