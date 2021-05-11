#Copyright (c) 2018 Thomas Norell
from subprocess import call
import smtplib
import time
from datetime import datetime
import pytz
import math
import enigma
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def composeGeneral(content, recipients):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("YOUR EMAILADDRESS HERE", "YOUR EMAIL PASSWORD HERE")
    server.sendmail("thomas.worker999@gmail.com", recipients, content)
    server.quit()


messages = ["""Here is my joke A Mathematician, Physicist, and an Engineer walking through a field come upon a farmer.
            The farmer asks what is the best way to construct a fence that will contain his livestock. The physicist does some calculus and concludes that the best way to do this is a square fence. The engineer looks at him and laughs. “No, the best way is a circle”. The physicist concedes and they start building the fence.The mathematician just sits there for a while and eventually stands up, puts a small piece around himself and says “I declare myself to be outside”.Hope you liked the joke. My secret code is sixseventwofour""",

            """Here is another joke A Mathematician, physicist, and an engineer are each sentenced to die by the guillotine. As the physicist is led to the guillotine, she decides that she'd like to observe the blade as it falls, perhaps to verify v=at, and she requests to be strapped in face up. The executioner agrees (why not? it all pays the same...), and straps her in. As the blade falls, it sticks about two thirds of the way down. Seeing this, the crowd cheers - the physicist must be innocent! So the exectuioner unstraps her and sets her free.
            The mathematician is next. Being well versed in matters statistical (perhaps she is an actuary), she quickly asks to be placed face up as well - after all, the odds of it happening again are pretty good, especially if the initial conditions are similar. So the excutioner obliges, and once again, the blade sticks about two thirds of the way down. Again the crowd cheers, and the mathematician is also set free.
            Finally, the engineer. Not willing to do anything in public that is different from her peers, she, too, requests to be placed face up. As the executioner is strapping her in, she's looking up at the blade and studying the track in which it slides. As she does so, she notices something. Do you see that?", she asks. "About one third the way up? If you fixed that there...My secret code is threeseventwothree""",

            """These jokes are getting repetitive A Mathematician, physicist, and an engineer are staying for the night in a hotel. Fortunately for this joke, a small fire breaks out in each room.
            The physicist awakes, sees the fire, makes some careful observations, and on the back of the hotel's wine list does some quick calculations. Grabbing the fire extinguisher, he puts out the fire with one, short, well placed burst, and then crawls back into bed and goes back to sleep.
            The engineer awakes, sees the fire, makes some careful observations, and on the back of the hotel's room service list (pizza menu) does some quick calculations. Grabbing the fire extinguisher (and adding a factor of safety of 5), he puts out the fire by hosing down the entire room several times over, and then crawls into his soggy bed and goes back to sleep.
            The mathematician awakes, sees the fire, makes some careful observations, and on a blackboard installed in the room, does some quick calculations. Jubliant, he exclaims "A solution exists!", and crawls into his dry bed and goes back to sleep.My secret code is sevensevenninethree""","""This joke is pretty boring A mathematician, physicist, and an engineer are at working in their offices. The engineer's cigarette falls off the desk into the wastebasket, causing the papers within to burst into flames. The engineer looks around, sees a fire extinguisher, grabs it, puts out the flames, and goes back to work.
            A physicist is working at his desk in another office and the same thing happens. He looks at the fire, looks at the fire extinguisher, and thinks "Fire requires fuel plus oxygen plus heat. The fire extinguisher will remove both the oxygen and the heat in the wastebasket. Ergo, no fire." He grabs the extinguisher, puts out the flames, and goes back to work.
            A mathematician is working at his desk in another office and the same thing happens. He looks at the fire, looks at the fire extinguisher, and thinks for a minute, says "Ah! A solution exists!" and goes back to work.Mysecretcodeissixfiveoneone""",

            """Here is my joke A Mathematician, Physicist, and an Engineer walking through a field come upon a farmer.
            The farmer asks what is the best way to construct a fence that will contain his livestock. The physicist does some calculus and concludes that the best way to do this is a square fence. The engineer looks at him and laughs. “No, the best way is a circle”. The physicist concedes and they start building the fence.The mathematician just sits there for a while and eventually stands up, puts a small piece around himself and says “I declare myself to be outside”.Hope you liked the joke. My secret code is oneseventwonine""",

            """Here is another joke A Mathematician, physicist, and an engineer are each sentenced to die by the guillotine. As the physicist is led to the guillotine, she decides that she'd like to observe the blade as it falls, perhaps to verify v=at, and she requests to be strapped in face up. The executioner agrees (why not? it all pays the same...), and straps her in. As the blade falls, it sticks about two thirds of the way down. Seeing this, the crowd cheers - the physicist must be innocent! So the exectuioner unstraps her and sets her free.
            The mathematician is next. Being well versed in matters statistical (perhaps she is an actuary), she quickly asks to be placed face up as well - after all, the odds of it happening again are pretty good, especially if the initial conditions are similar. So the excutioner obliges, and once again, the blade sticks about two thirds of the way down. Again the crowd cheers, and the mathematician is also set free.
            Finally, the engineer. Not willing to do anything in public that is different from her peers, she, too, requests to be placed face up. As the executioner is strapping her in, she's looking up at the blade and studying the track in which it slides. As she does so, she notices something. Do you see that?", she asks. "About one third the way up? If you fixed that there...My secret code is threethreetwothree""",

            """These jokes are getting repetitive A Mathematician, physicist, and an engineer are staying for the night in a hotel. Fortunately for this joke, a small fire breaks out in each room.
            The physicist awakes, sees the fire, makes some careful observations, and on the back of the hotel's wine list does some quick calculations. Grabbing the fire extinguisher, he puts out the fire with one, short, well placed burst, and then crawls back into bed and goes back to sleep.
            The engineer awakes, sees the fire, makes some careful observations, and on the back of the hotel's room service list (pizza menu) does some quick calculations. Grabbing the fire extinguisher (and adding a factor of safety of 5), he puts out the fire by hosing down the entire room several times over, and then crawls into his soggy bed and goes back to sleep.
            The mathematician awakes, sees the fire, makes some careful observations, and on a blackboard installed in the room, does some quick calculations. Jubliant, he exclaims "A solution exists!", and crawls into his dry bed and goes back to sleep.My secret code is sevensevenonefour""",

            """This joke is pretty boring A mathematician, physicist, and an engineer are at working in their offices. The engineer's cigarette falls off the desk into the wastebasket, causing the papers within to burst into flames. The engineer looks around, sees a fire extinguisher, grabs it, puts out the flames, and goes back to work.
            A physicist is working at his desk in another office and the same thing happens. He looks at the fire, looks at the fire extinguisher, and thinks "Fire requires fuel plus oxygen plus heat. The fire extinguisher will remove both the oxygen and the heat in the wastebasket. Ergo, no fire." He grabs the extinguisher, puts out the flames, and goes back to work.
            A mathematician is working at his desk in another office and the same thing happens. He looks at the fire, looks at the fire extinguisher, and thinks for a minute, says "Ah! A solution exists!" and goes back to work.Mysecretcodeistwozerooneone"""
]
clean = []
for m in messages:
    swap = m.upper().replace(' ', '')
    current = ''
    for c in swap:
        if c in letters:
            current += c
    clean.append(current)
messages = clean
settings = [[4,3,2,0,13,10,24], [1,3,0,1,7,10,20], [0,3,4,0,8,25,24], [1,2,4,1,2,20,12], [1,3,2,0,0,10, 18], [1,3,2,1,8,13,20], [0,1,4,0,8,25,19], [1,2,0,0,2,20,8]]

recipients = [] #Make this a list of strings of recipients email addresses
count = 0
for set in settings:
    machine = enigma.enigma()
    machine.setLeft(enigma.rotors[set[0]],set[4])
    machine.setMiddle(enigma.rotors[set[1]], set[5])
    machine.setRight(enigma.rotors[set[2]], set[6])
    machine.setReflector(enigma.reflectors[set[3]])
    plug = enigma.plugboard()
    machine.setPlugboard(plug)
    cipher = machine.operate(messages[count])
    composeGeneral(cipher, recipients)
    time.sleep(20 * 60)
    count += 1


    #print(enigma.reflectors[set[3]])
