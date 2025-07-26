from together import Together
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

class HangmanBot:
    def __init__(self):
        self.client = Together(api_key=API_KEY)

    def predict_letter(self, word_state, guessed_letters, word_length):
        while True:
            prompt = (
                f"Hangman game: Word is {word_length} letters long.\n"
                f"Current state: {' '.join(word_state)}\n"
                f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}\n"
                f"What letter should I guess next? Answer with just one lowercase letter."
            )

            response = self.client.chat.completions.create(
                model="arcee-ai/AFM-4.5B-Preview",
                messages=[{"role": "user", "content": prompt}],
            )
            reply = response.choices[0].message.content.strip()

            for char in reply:
                if char.isalpha() and char.lower() not in guessed_letters:
                    return char.lower()
    
    def play_game(self, target_word):
        word = target_word.lower()
        word_length = len(word)
        max_attempts = word_length * 2 - 1
        
        word_state = ['_'] * word_length
        guessed_letters = set()
        attempts = 0
        
        print(f"\n🎯 Target word: {word}")
        print(f"📏 Word length: {word_length}")
        print(f"🎲 Max attempts: {max_attempts}")
        print(f"📝 Word state: {' '.join(word_state)}")
        
        while attempts < max_attempts and '_' in word_state:
            predicted_letter = self.predict_letter(word_state, guessed_letters, word_length)
            guessed_letters.add(predicted_letter)
            attempts += 1
            
            print(f"\n🤖 Model predicts: '{predicted_letter}' (Attempt {attempts}/{max_attempts})")
            
            response = input("✅ Is this letter in the word? (y/n): ").strip().lower()
            if response in ['y', 'yes']:
                positions = [i for i, char in enumerate(word) if char == predicted_letter]
                for pos in positions:
                    if word_state[pos] == '_':
                        word_state[pos] = predicted_letter
                print(f"✅ Letter '{predicted_letter}' found at positions: {[p+1 for p in positions]}")
            else:
                print(f"❌ Letter '{predicted_letter}' is not in the word.")
            
            print(f"📝 Word state: {' '.join(word_state)}")
            print(f"🔤 Guessed letters: {', '.join(sorted(guessed_letters))}")
        
        print("\n" + "="*50)
        if '_' not in word_state:
            print(f"🎉 SUCCESS! Model guessed '{word}' in {attempts} attempts!")
            return True
        else:
            print(f"💀 FAILED! Model couldn't guess '{word}' in {max_attempts} attempts.")
            return False

def main():
    bot = HangmanBot()
    print("🎮 Welcome to AI Hangman Bot!")
    print("=" * 50)
    print("🤖 I'll use a language model to predict your words!")
    
    while True:
        target_word = input("\n📝 Enter a word 3 letters long for the model to guess: ").strip()
        if not target_word or not target_word.isalpha() or len(target_word) != 3:
            print("❌ Please enter a valid word 3 letters long, letters only)!")
            continue
        
        bot.play_game(target_word)
        
        continue_choice = input("\n🔄 Play another game? (y/n): ").strip().lower()
        if continue_choice in ['n', 'no']:
            print("\n👋 Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main() 
