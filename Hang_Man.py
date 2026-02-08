import random
import os

class Hang_Man():
    def __init__(self):
        self.menu()

    def menu(self):
        print("\t\t----HANG-MAN----\n")
        print("1. START GAME")
        print("2. WORD LIST")
        print("3. QUIT")
        self.choice = input("")
        if self.choice == "1":
            self.game_structure()
        elif self.choice == "2":
            pass
        elif self.choice == "3":
            pass
        else:
            pass

    def game_structure(self):
        self.game_word = "apple"
        self.hint = "A red skinned juicy fruit."
        self.len_gw = len(self.game_word)
        self.dash_for_gw = list("_"*self.len_gw)
        self.list_gw = list(self.game_word)
        print("\t\t----HANG-MAN----\n")
        print(f"Your word has {self.len_gw} letters in it.", end= "\t")
        print(f"\t{"❤️" * 5}")
        print(f"\t{" ".join(self.dash_for_gw)}")
        print(f"HINT: {self.hint}")

        #The users guesses are taken from here
        self.guess_letter = input("Guess a letter in the word: ").lower()

        if len(self.guess_letter) == 1 and self.guess_letter.isalpha:
            if self.guess_letter in self.game_word:
                for i in range(self.len_gw):
                    if self.guess_letter == self.game_word[i]:
                        self.dash_for_gw[i] == self.game_word[i]
                        self.list_gw.pop(i)

                    


