import string

class Enigma: #tworzenie klasy enigmy, wraz z konstruktorem oraz przypisuje pozycje i ustawienia rotorow i reflektory
    def __init__(self, rotor_positions, rotor_settings, reflector):
        self.alphabet = string.ascii_uppercase
        self.rotor_positions = rotor_positions
        self.rotor_settings = rotor_settings
        self.reflector = reflector

    def encrypt_letter(self, letter): #kodowanie słowa, szyfrowana jest każda pojedyncza litera
        letter_index = self.alphabet.index(letter)
        for i in range(len(self.rotor_positions)): #pętla która iteruje przez wszystkie rotory
            letter_index = (letter_index + self.rotor_positions[i]) % 26
            letter_index = (letter_index + self.rotor_settings[i]) % 26
            letter_index = self.alphabet.index(self.reflector[letter_index])
            letter_index = (letter_index - self.rotor_settings[i]) % 26
            letter_index = (letter_index - self.rotor_positions[i]) % 26
        return self.alphabet[letter_index]   #zwraca literke która jest juz zaszyfrowana

    def encrypt_message(self, message): #kodowanie całej wiadomości
        encrypted_message = "" #zapisywana tu będzie zaszyfrowana wiadomość
        for letter in message.upper():
            if letter in self.alphabet:
                encrypted_message += self.encrypt_letter(letter)
                self.rotate_rotors()
            else:
                encrypted_message += letter #dodaje "przemielona" literke do zaszyfrowanego kodu
        return encrypted_message #zwraca zaszyfrowaną wiadomość

    def rotate_rotors(self):  #symuluje rotacje rotorów
        self.rotor_positions[0] = (self.rotor_positions[0] + 1) % 26
        for i in range(len(self.rotor_positions) - 1):
            if self.rotor_positions[i] == 0:
                self.rotor_positions[i + 1] = (self.rotor_positions[i + 1] + 1) % 26

x=True

while x==True:
    rotor_positions = [0, 0, 0]  # poczatkowe pozycje rotorow
    rotor_settings = [1, 1, 1]  # poczatkowe ustawienia rotorow
    reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"  # poczatkowa konfiguroacja reflektora taki alfabet z innymi pozycjami literek

    enigma = Enigma(rotor_positions, rotor_settings, reflector)  # tworzy nowy obiekt z klasy Enigma

    message = input("Podaj jakieś słowo do szyfru: ")
    encrypted_message = enigma.encrypt_message(message)  # szyfruje wiadomość
    print("Encrypted message:", encrypted_message)  # wyświetlą tą wiadomość

    answ = input("Chcesz wykonać ponownie szyfr? T/N:").upper()
    if(answ =="T" ):
        print("---")
    else:
        x=False

#Patrk Kryger
#Olek Wasowicz