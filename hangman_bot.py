#imports the python libraries taken
from together import Together
import os
from dotenv import load_dotenv

#loads environment & declares it as a variable
load_dotenv()
API_KEY = os.getenv("API_KEY")

#class is the broad category
class HangmanBot:
    #configures the model
    def __init__(self):
        self.client = Together(api_key=API_KEY)

    def predict_letter(self, word_state, guessed_letters, word_length):
        while True:
            #text that goes to the AI model
            prompt = (
                f"Hangman game: Word is {word_length} letters long.\n"
                f"Current state: {' '.join(word_state)}\n"
                f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}\n"
                f"What letter should I guess next? Answer with just one lowercase letter."
            )

            response = self.client.chat.completions.create(
                #calling the model
                model="arcee-ai/AFM-4.5B",
                #use the prompt function to tell ai what to do
                messages=[{"role": "user", "content": prompt}],
            )
            #gets a letter from the ai
            reply = response.choices[0].message.content.strip()

            for char in reply:
                if char.isalpha() and char.lower() not in guessed_letters:
                    return char.lower()
    
    def play_game(self, target_word):
        word = target_word.lower()
        word_length = len(word)
        max_attempts = word_length * 2
        
        word_state = ['_'] * word_length
        guessed_letters = set()
        attempts = 0
        
        print(f"\n Target word: {word}")
        print(f" Word length: {word_length}")
        print(f" Max attempts: {max_attempts}")
        print(f" Word state: {' '.join(word_state)}")
        
        #code that runs the game
        while attempts < max_attempts and '_' in word_state:
            # the () are parameters, this is for the AI to guess letter
            predicted_letter = self.predict_letter(word_state, guessed_letters, word_length)
            guessed_letters.add(predicted_letter)
            attempts += 1
            
            print(f"\n Model predicts: '{predicted_letter}' (Attempt {attempts}/{max_attempts})")
            
            #model response only has one letter
            response = input("✅ Is this letter in the word? (y/n): ").strip().lower()
            #puts guessed letter in underscore if it's in the word
            if response in ['y', 'yes']:
                positions = [i for i, char in enumerate(word) if char == predicted_letter]
                for pos in positions:
                    if word_state[pos] == '_':
                        word_state[pos] = predicted_letter
                print(f"✅ Letter '{predicted_letter}' found at positions: {[p+1 for p in positions]}")
            #if letter isn't in word, this is the response
            else:
                print(f"❌ Letter '{predicted_letter}' is not in the word.")
            
            print(f" Word state: {' '.join(word_state)}")
            print(f" Guessed letters: {', '.join(sorted(guessed_letters))}")
        #text that shows end of game(win or lose)
        print("\n" + "="*50)
        if '_' not in word_state:
            print(f"Congrats! Model guessed '{word}' in {attempts} attempts!")
            return True
        else:
            print(f"FAILED! Model couldn't guess '{word}' in {max_attempts} attempts.")
            return False
#starting screen
def main():
    bot = HangmanBot()
    print(" Welcome to AI Hangman Bot!")

    
    while True:
        target_word = input("\n Enter a word 3 letters long for the model to guess: ").strip()
        if not target_word or not target_word.isalpha() or len(target_word) != 3:
            print(" Please enter a valid word 3 letters long, letters only)!")
            continue
        
        bot.play_game(target_word)
        #text shown asking if they want to play again
        continue_choice = input("\n Play another game? (y/n): ").strip().lower()
        if continue_choice in ['n', 'no']:
            print("\n Thanks for playing! Goodbye!")
            break
#runs the function
if __name__ == "__main__":
    main() 
