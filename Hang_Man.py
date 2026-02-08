import random
import os

class Hang_Man():
    def __init__(self):
        self.menu()

    def menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\t\t----HANG-MAN----\n")
        print("1. START GAME")
        print("2. WORD LIST")
        print("3. QUIT")
        self.choice = input("")
        if self.choice == "1":
            self.game_structure()
        elif self.choice == "2":
            self.word_table()
        elif self.choice == "3":
            pass
        else:
            pass

    def word_bank(self):
        self.word_list = [
            {"Word":"apple",
             "Meaning":""
             },
            {"Word":"ball",
             "Meaning":""
             },
            {"Word":"cat",
             "Meaning":""
             },
            {"Word":"dog",
             "Meaning":""
             } 
        ]

    def chosen_word(self):
        self.word_bank()
        self.the_one = random.choice(self.word_list)
    def game_structure(self):
        self.chosen_word()
        self.game_word = self.the_one["Word"]
        self.hint = self.the_one["Meaning"]
        self.len_gw = len(self.game_word)
        self.dash_for_gw = list("_"*self.len_gw)
        self.list_gw = list(self.game_word)
        self.xp_left = 5
        self.guesses_made = []
        self.message = ""


        while True:  
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\t\t----HANG-MAN----\n")
            print(f"\t\tLives: {'❤️  ' * self.xp_left }")
            if self.message:
                print(f"NOTIFICATION: {self.message}")
                self.message = ""
            print(f"Word: {" ".join(self.dash_for_gw)}")
            print(f"Hint: {self.hint}")
            
            if "_" not in self.dash_for_gw:#message that needs to appear before taking the guess word
                print("\nYOU WON!")
                input("Press enter to return to menu...")
                break

            if self.xp_left == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"The word was {self.game_word}")
                print("You've lost the game.")
                input("Press enter to return to menue...")
                break
            
            #The users guesses are taken from here
            self.guess_letter = input("Guess a letter: ")
            if not (len(self.guess_letter)== 1 and self.guess_letter.isalpha()):#not(and) structure makes sure that all the inputs satiate the requirements
                self.message = "Invalid input. Enter a single letter."

            if self.guess_letter in self.guesses_made:
                self.message = f"You've already guessed '{self.guesses_made}'"
            
            if self.guess_letter in self.game_word:
                print(f"{self.guess_letter} is in word")
                for i in range(self.len_gw):
                    if self.guess_letter == self.game_word[i]:
                        self.dash_for_gw[i] = self.game_word[i]
                        self.guesses_made.append(self.guess_letter)
            else:
                self.message = f"Bad Luck!'{self.guess_letter}'is not there."
                self.xp_left -=1

    def word_table(self):
        self.word_bank()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\t----Word-List----")
        for i in self.word_list:
            print(i["Word"])
       

              

Hang_Man()        

                    


