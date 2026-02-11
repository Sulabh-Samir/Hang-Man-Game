import random
import os

class Hang_Man():
    def __init__(self):
        self.word_meaning = [
            {"Word": "cobbling",
             "Meaning": "The work of a cobbler; shoemaking."},
            {"Word": "venatoril",
             "Meaning": "Of, pertaining to or involved in hunting or the chase."},
            {"Word": "phobism",
             "Meaning": "A phobia"},
            {"Word": "polymorphis",
             "Meaning": "The ability to assume different forms or shapes"},
            {"Word": "quinquedented",
             "Meaning": "Having a pattern of five teeth"},
            {"Word": "raked",
             "Meaning": "sloping"}    
             
        ]
        self.user_choice()
    
    def display_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\t----HANG-MAN----")
        print("1. START")
        print("2. WORD LIST")
        print("3. EXIT")
    
    def user_choice(self):
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1, 2, or 3):")
            if choice == '1':
                self.game_architecture()
            elif choice == '2':
                self.list_of_words()
            elif choice == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You've existed the game...")
                break

    def word_bank(self):
        self.target_word = random.choice(self.word_meaning)
    
    def game_architecture(self):
        self.word_bank()
        self.game_word = self.target_word['Word']
        self.game_word_meaning = self.target_word['Meaning']
        self.let_no_game_word = len(self.game_word)
        self.dash_for_game_word = list("_" * self.let_no_game_word)
        self.all_guesses = []
        self.message = ""
        self.error_count = 6

        while True:
            os.system("cls" if os.name == 'nt' else "clear")
            print("\t----HANG-MAN----")

            #Show the users their game-status
            print(f"Lives: {'❤️  ' * self.error_count}({self.error_count}/6)")

            if self.message:
                print(f"NOTIFICATION: {self.message}")
                self.message = ''
            print(f"\nWord: {' '.join(self.dash_for_game_word)}")
            print(f"Hint: {self.game_word_meaning}")
            
            #Checking for WIN
            if "_" not in self.dash_for_game_word:
                print("\nYOU WON!")
                input("Press Enter to return to menu...")
                break

            #Checking for LOSS
            if self.error_count <= 0:
                print(f"\n\t==GAME OVER!==")
                print(f"The word was: {self.game_word}")
                input("Press Enter to return to menu...")
                break

            self.guess_letter = input("\nGuess a letter: ").lower()

            #1. Validation
            if len(self.guess_letter) != 1 or not self.guess_letter.isalpha():
                self.message = "Invalid input. Please enter a single letter."
                continue

            #2. Duplicate Check
            if self.guess_letter in self.all_guesses:
                self.message = f"You've already guessed'{self.guess_letter}'!"
                continue

            self.all_guesses.append(self.guess_letter)

            #3. Hit or Miss Logic
            if self.guess_letter in self.game_word.lower():
                #Loop through and reveal all instances of the letter
                for i in range(self.let_no_game_word):
                    if self.guess_letter == self.game_word[i].lower():
                        self.dash_for_game_word[i] = self.game_word[i]
                
            else:
                self.message = f"Bad luck!'{self.guess_letter}' is not in there."
                self.error_count -= 1

    def list_of_words(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("---WORD LIST---")
        for i in self.word_meaning:
            print(f"-{i['Word']}")
        input("\nPress enter to return...")
    
Hang_Man()

