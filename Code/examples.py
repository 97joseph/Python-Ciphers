#Copyright (c) 2018 Thomas Norell
import enigma
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
machine = enigma.enigma() #Enigma Machine Constructors
machine.setLeft(enigma.rotors[0], 0) #Set Left Rotor as Rotor I, Enigma object comes with a list of rotor objects
machine.setMiddle(enigma.rotors[1], 0) #Set Middle Rotor as Rotor II
machine.setRight(enigma.rotors[2], 0) #Set Right Rotor as Rotor III
machine.setReflector(enigma.reflectors[0]) #Set Reflector as reflector C (We only have B & C) (object comes with list of reflectors) (reflectors are implemented as just a special case of rotors)
machine.setPlugboard(enigma.plugboard())
text = 'Hello this is an example message to see if my program works properly'.upper().replace(' ', '') #create text to encrypt
cipher = machine.operate(text) #The operate method encrypts a string. Keep in mind that Enigma's are mutable, so after encryption the rotors are no longer in the initial configuration
print('Ciphertext: ' + cipher[:100])

#Let's reset the machine and send our ciphertext back through
machine.setLeft(enigma.rotors[0], 0)
machine.setMiddle(enigma.rotors[1], 0)
machine.setRight(enigma.rotors[2], 0)
machine.setReflector(enigma.reflectors[0])
machine.setPlugboard(enigma.plugboard())
b = machine.operate(cipher)
print('Decoded Plaintext: ' + b[:100])
print('Verified: ' + str(b == text)) #Validate successful decryption

######################################
# Now an example using the plugboard #
######################################

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
machine = enigma.enigma()
machine.setLeft(enigma.rotors[3], 13)
machine.setMiddle(enigma.rotors[1], 15)
machine.setRight(enigma.rotors[4], 2)
machine.setReflector(enigma.reflectors[1])
plug = enigma.plugboard() #the class comes with a default (no connections) plugboard
plug.connect('A', 'B') #We can connect two letters like this. We can disconnect them as plug.disconnect('A', 'B')
plug.connect('D', 'F')
machine.setPlugboard(plug)
text = 'Hi this is another example to see if enigma properly encodes and decodes messages'.upper().replace(' ', '')
cipher = machine.operate(text)
print('Ciphertext: ' + cipher[:100])
#resetting machine and verifying successful decryption
machine.setLeft(enigma.rotors[3], 13)
machine.setMiddle(enigma.rotors[1], 15)
machine.setRight(enigma.rotors[4], 2)
machine.setReflector(enigma.reflectors[1])
machine.setPlugboard(plug)
b = machine.operate(cipher)
print('Decoded Plaintext: ' + b[:100])
print('Verified: ' + str(b == text))
