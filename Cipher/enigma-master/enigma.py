#Copyright (c) 2018 Thomas Norell
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
class rotor:
    #map describes rotos, machine is a reference to an enigma machine
    def __init__(self, map):
        self.rmap = map
        self.invMap = {v: k for k, v in self.rmap.items()} #We invert the mapping for the return trip
        self.index = 0 #index descrives the rotor's position relative to the machines
        self.rotateCount = 0 #keeps track of how man times we have moved
    def setIndex(self, index):
        if (index >= 26):
            raise Exception("A rotor position must not be more than 25!")
        self.index = index
    def rotate(self):
        #Rotate our index relative to Enigma Machine
        self.index = (self.index + 1) % 26 #rotate
        self.rotateCount += 1
        #https://en.wikipedia.org/wiki/Enigma_machine#Turnover
        if not self.left is None and (self == rotors[0] and self.index == letters.index('R') or (self == rotors[1] and self.index == letters.index('F')) or (self == rotors[2] and self.index == letters.index('W')) or (self == rotors[3] and self.index == letters.index('K')) or (self == rotors[4] and self.index == letters.index('A'))):
            self.left.rotate() #Turnover

    #Passes signal to through me and to rotor to left
    def passLeft(self, input):
        out = letters.index(self.rmap[letters[(input - self.index) % 26]])
        if self.left is None:
            return self.passRight(self.reflector.reflect((out + self.index) % 26))
        return self.left.passLeft((out + self.index) % 26) #recursive call
    #Passes signal through me and to rotor to right
    def passRight(self, input):
        out = letters.index(self.invMap[letters[(input - self.index) % 26]])
        if self.right is None:
            return letters[(out + self.index) % 26]
        return self.right.passRight((out + self.index)% 26) #recursive call
    def setNeighbors(self, left, right):
        self.left = left
        self.right = right
    def setReflector(self, reflector):
        self.reflector = reflector
    #Perform reflection
    def reflect(self, input):
        return letters.index(self.rmap[letters[input]])
    def setPosition(self, num):
        self.index = num
        self.rotateCount = num #Does this get set to zero or to num? A specific engima rotor design question
one = {}
two = {}
three = {}
four = {}
five = {}
a = {}
b = {}
c = {}
#https://en.wikipedia.org/wiki/Enigma_rotor_details#Rotor_wiring_tables
for l in range(len(letters)):
    one[letters[l]] = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'[l]
    two[letters[l]] = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'[l]
    three[letters[l]] = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'[l]
    four[letters[l]] = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'[l]
    five[letters[l]] = 'VZBRGITYUPSDNHLXAWMJQOFECK'[l]
    a[letters[l]] = 'EJMZALYXVBWFCRQUONTSPIKHGD'[l]
    b[letters[l]] = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'[l]
    c[letters[l]] = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'[l]

rotorOne = rotor(one)
rotorTwo = rotor(two)
rotorThree = rotor(three)
rotorFour = rotor(four)
rotorFive = rotor(five)

reflectorA = rotor(a)
reflectorB = rotor(b)
reflectorC = rotor(c)
rotors = [rotorOne, rotorTwo, rotorThree, rotorFour, rotorFive]
reflectors = [reflectorA, reflectorB, reflectorC]


class enigma:
    def __init__(self):
        self.left = None
        self.middle = None
        self.right = None
        self.reflector = None
        self.plugboard = None
        self.invPlugboard = None
    def setLeft(self, rotor, position):
        self.left = rotor
        rotor.setPosition(position)
    def setMiddle(self, rotor, position):
        self.middle = rotor
        rotor.setPosition(position)
    def setRight(self, rotor, position):
        self.right = rotor
        rotor.setPosition(position)
    def setReflector(self, reflector):
        self.reflector = reflector
    def setPlugboard(self, plug):
        self.plugboard = plug
    def encodeChar(self, char):
        if (self.left == None or self.middle == None or self.right == None):
            raise Exception("You must specify left, middle, and right rotors!")
        if (self.plugboard == None):
            raise Exception("You must specify a plugboard configuration!")
        if len([self.left, self.middle, self.right]) != len(set([self.left, self.middle, self.right])):
            raise Exception("You cannot use two rotors twice!")
        char = char.upper()
        self.left.setNeighbors(None, self.middle)
        self.left.setReflector(self.reflector)
        self.middle.setNeighbors(self.left, self.right)
        self.right.setNeighbors(self.middle, None)

        plug = self.plugboard.mapping[char] #Send through plugboard

        out = self.right.passLeft(letters.index(plug)) #Kickoff rotor recursion
        out = self.plugboard.mapping[out] #Send back through plugboard
        self.right.rotate() #Rotate rightmost rotor once
        return out
    def operate(self, message):
        m = ''
        for c in message:
            m += self.encodeChar(c)
        return m
class plugboard:
    def __init__(self):
        self.mapping = {}
        for l in letters:
            self.mapping[l] = l
    def connect(self, a, b):
        a = a.upper()
        b = b.upper()
        if (self.mapping[a] != a or self.mapping[b] != b):
            raise Exception("Cannot connect to a letter that is already in a connection, disconnect first!")
        self.mapping[a] = b
        self.mapping[b] = a
    def disconnect(self, a, b):
        a = a.upper()
        b = b.upper()
        if self.mapping[a] != b or self.mapping[b] != a:
            raise Exception("Cannot disconnect a connection that doesn't exist!")
        self.mapping[a] = a
        self.mapping[b] = b
