import requests
import string

class HangmanBot:
    def __init__(self):
        self.api_url = "https://router.huggingface.co/together/v1/completions"
        self.headers = {"Authorization": "Bearer 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"}
    
    def predict_letter(self, word_state, guessed_letters, word_length):
        prompt = f"In a hangman game, the word is {word_length} letters long. Current state: {' '.join(word_state)}. Letters already guessed: {', '.join(guessed_letters)}. Guess the next letter to try. Respond with only one letter:"
        
        response = requests.post(self.api_url, headers=self.headers, json={
            "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
            "prompt": prompt,
            "max_tokens": 3,
            "temperature": 0.3
        }).json()
        
        if response and 'choices' in response and len(response['choices']) > 0:
            generated_text = response['choices'][0]['text'].strip()
            for char in generated_text.lower():
                if char.isalpha() and char not in guessed_letters:
                    return char
        
        available_letters = [c for c in string.ascii_lowercase if c not in guessed_letters]
        return available_letters[0] if available_letters else 'e'
    
    def play_game(self, target_word):
        word = target_word.lower() # word length 3
        word_length = len(word)
        max_attempts = word_length * 2
        
        word_state = ['_'] * word_length
        guessed_letters = set()
        attempts = 0
        correct_guesses = 0
        
        print(f"\n🎯 Target word: {word}")
        print(f"📏 Word length: {word_length}")
        print(f"🎲 Max attempts: {max_attempts}")
        print(f"📝 Word state: {' '.join(word_state)}")
        
        while attempts < max_attempts and correct_guesses < word_length:
            predicted_letter = self.predict_letter(word_state, guessed_letters, word_length)
            guessed_letters.add(predicted_letter)
            attempts += 1
            
            print(f"\n🤖 Model predicts: '{predicted_letter}' (Attempt {attempts}/{max_attempts})")
            
            # fill the spaces with the predicted letter
            response = input("✅ Is this letter in the word? (y/n): ").strip().lower()
            if response in ['y', 'yes']:
                positions_input = input("📍 Enter positions (1-6) where letter appears (e.g., 1,3): ").strip()
                positions = [int(pos.strip()) - 1 for pos in positions_input.split(',')]
                for pos in positions:
                    if 0 <= pos < word_length and word_state[pos] == '_':
                        word_state[pos] = predicted_letter
                        correct_guesses += 1
                print(f"✅ Letter '{predicted_letter}' placed at positions: {[p+1 for p in positions]}")
            else:
                print(f"❌ Letter '{predicted_letter}' is not in the word.")
            
            print(f"📝 Word state: {' '.join(word_state)}")
            print(f"🔤 Guessed letters: {', '.join(sorted(guessed_letters))}")
            print(f"🎯 Correct letters: {correct_guesses}/{word_length}")
        
        print("\n" + "="*50)
        if correct_guesses == word_length:
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
        target_word = input("\n📝 Enter a word (max 6 letters) for the model to guess: ").strip()
        if not target_word or not target_word.isalpha() or len(target_word) < 2 or len(target_word) > 6:
            print("❌ Please enter a valid word (2-6 letters, letters only)!")
            continue
        
        success = bot.play_game(target_word)
        
        continue_choice = input("\n🔄 Play another game? (y/n): ").strip().lower()
        if continue_choice in ['n', 'no']:
            print("\n👋 Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main() 