#Copyright (c) 2018 Thomas Norell
############
# Breaking #
############

import enigma
import random
import time
#We need to get all size 3 subsets from our list of rotors
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
import itertools
def findsubsets(S,m):
    mylist = []
    for l in itertools.combinations(S, m):
        mylist.append(list(l))
    return mylist

def freq(text):
    counts = [0.0] * 26
    text = text.upper().replace(' ', '')
    for i in text:
        counts[letters.index(i)] += 1
    return counts


def IOC(text):
    total = 0.0
    counts = freq(text)
    for l in letters:
        total += counts[letters.index(l)]/len(text) * (counts[letters.index(l)] - 1)/(len(text) - 1)
    return total


letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
machine = enigma.enigma() #Enigma Machine Constructors
config = findsubsets([0,1,2,3,4], 3)[random.randint(0,len(findsubsets([0,1,2,3,4], 3)))]
machine.setLeft(enigma.rotors[config[0]], random.randint(0, 25)) #Set Left Rotor as Rotor I, Enigma object comes with a list of rotor objects
machine.setMiddle(enigma.rotors[config[1]], random.randint(0, 25)) #Set Middle Rotor as Rotor II
machine.setRight(enigma.rotors[config[2]], random.randint(0, 25)) #Set Right Rotor as Rotor III
machine.setReflector(enigma.reflectors[random.randint(0, 1)]) #Set Reflector as reflector C (We only have B & C) (object comes with list of reflectors) (reflectors are implemented as just a special case of rotors)
machine.setPlugboard(enigma.plugboard())
#text = 'MYNAMEISTHOMASNORELL'.upper().replace(' ', '') #create text to encrypt
text = open("book.txt").read().upper().replace(' ', '')[:100]
clean = ''
for l in text:
    if l in letters:
        clean += l

text = clean

cipher = machine.operate(text) #The operate method encrypts a string. Keep in mind that Enigma's are mutable, so after encryption the rotors are no longer in the initial configuration
print('Ciphertext:' + cipher[:100])
print(IOC(text))
count = 0
rotorConfigs = []
for conf in findsubsets([0,1,2,3,4], 3):
    permutes = itertools.permutations(conf)
    for p in permutes:
        rotorConfigs.append(list(p))

cipher="MYPMCBHAHJTAFVUXOIDRWLMCGSRAPWQJUVSWLEJTJAYRMHISCOCNSVIEMOQIPNSCGSXHLKEDJIPQELIULJTSBCJOTTZHVQRVNRMEGECQAMBAANVLAFTDSEAMHXUKAMDUTLYNMMTFKVCIHJFIKCQBUPCWYZNNWPXYMCRONFMRYXJINVJHSQROKIXEPAJGFRKQQYGWOWFAQFYUXLUDKSVBXSLJAIFPVFYLXMHUUHXZYRSMRCPZWDISWJFJKXRKDCEGGMOMSJEPCRXFJEPBQHYEQFGPLWZKMOHZCONFOGAYSXHJRGCRUYCBTRDHGQZUSZMBLBKNKIDKQBHRTZQGYYRVYOXEZCOZDOFJEFPXJQXPUMGISRRSQCQYWTYDNECPWMXPVKIMRYLTXGIVRUFZGZGGLJWTNROPPLDSAJJRUHWMFZISYAQKNXKCZQKWNMGEZDTNXBLBJIGUVEBZGPVTISHNWVQFAFQARKSAFCMJCDTWXATNYVADIG"
start_time = time.time()
for rotorConfig in rotorConfigs:
    for reflector in enigma.reflectors:
        for pos0 in range(26):
            for pos1 in range(26):
                for pos2 in range(26):
                    machine = enigma.enigma()
                    machine.setLeft(enigma.rotors[rotorConfig[0]],pos0)
                    machine.setMiddle(enigma.rotors[rotorConfig[1]], pos1)
                    machine.setRight(enigma.rotors[rotorConfig[2]], pos2)
                    machine.setReflector(reflector)
                    plug = enigma.plugboard()
                    machine.setPlugboard(plug)
                    plain = machine.operate(cipher[:100])
                    if IOC(plain > .06):
                        print(plain, rotorConfig, pos0, pos1, pos2, reflector)
                        print("--- %s seconds ---" % (time.time() - start_time))
                    if count % 10000 == 0:
                        print(count)
                    count += 1
