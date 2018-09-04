#biðja notanda um tölu og á meða hún er stærri en núll á að halda áfram, þegar kemur mínustala á hæsta talan að skrifast út.
#(það varður því að búa til breytu til að halda utan um hæsta gildið í hverri keyrslu).
#biðja um tölu og setja inn upphafsgildi til að hafa til samanburðar við töluna x
num_int = int(input("Input a number: "))
max_int = 0
#á meðan innslegna talan er >= 0 á að tékka hvort núverandi tala sé lægri en ný innslegna talan
#og ef hún er það á hún að fara inn í max breytuna til að hægt sé að halda utan um hæsta gildið eftir hverja keyrslu.
#fá svo inn nýja tölu.
#þegar neikvæð tala kemur inn hættir while lykkjan og hæsta gildið prentast út.    
while num_int >= 0:  
    if max_int < num_int:
        max_int = num_int                                                                   
    num_int = int(input("input a number: "))        
print("The maximum is: ", max_int) 