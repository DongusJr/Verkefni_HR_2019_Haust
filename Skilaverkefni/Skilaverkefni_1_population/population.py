
#Breytur frá verkefninu
population_int = 307357870
birth_rate_int = 7
death_rate_int = 13
immigration_rate_int = 35

#Hér ætti notandinn að slá inn ár
years_str = input("Years: ")
years_int = int(years_str)


if(years_int < 0):  #athuga hvort að talan fyllir skilyrðin
    print("Invalid input!")
else:
    years_to_seconds = (years_int*365*24*60*60) #fáum sekúndur fyrir reikninga
    estimated_population_float = float((population_int + (years_to_seconds/birth_rate_int) + (years_to_seconds/immigration_rate_int) - (years_to_seconds/death_rate_int))) #Hér er reiknað út (estimated pop = original pop + birth + immigration - death) sem rauntala
    estimated_population_int = int(estimated_population_float) #parse frá float í int
    print("New population after {} years is {}".format(years_str, estimated_population_int))
              
    
