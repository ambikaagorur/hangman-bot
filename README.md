# AI Hangman Bot

A hangman game where you input a word and an AI language model tries to predict it by understanding the hangman game context.

## Features

- 🤖 **Real Language Model**: Uses Hugging Face's open-source language models (GPT-2)
- 🧠 **Context Understanding**: Model understands hangman game state and predicts accordingly
- 📝 **User Input**: You input a word, the AI model tries to guess it
- 🎯 **2x Attempts**: Model gets 2x the word length as maximum attempts
- 🔄 **Continue/Quit**: Play multiple games with y/n prompts
- 💰 **Free API**: Uses Hugging Face's free inference API

## How to Play

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the game:
   ```bash
   python hangman_bot.py
   ```

3. Get a free API key from Hugging Face (optional):
   - Visit: https://huggingface.co/settings/tokens
   - Create a free account and generate an API key

4. Enter your API key when prompted (or press Enter for fallback mode)

5. Enter a word for the model to guess

6. Watch the AI model analyze and predict your word!

## How the AI Model Works

The bot uses a real language model that:

- **Understands Context**: Receives prompts like "Hangman game: Word is 6 letters. Current state: _ _ _ t _ _. Letters guessed: e, t. What letter should I guess next?"
- **Makes Intelligent Predictions**: Uses GPT-2 to understand word patterns and predict likely letters
- **Learns from Game State**: Adapts predictions based on revealed letters and previous guesses
- **Fallback System**: Uses letter frequency analysis if API is unavailable

## Example Game

```
🎮 Welcome to AI Hangman Bot!
==================================================
🤖 I'll use a language model to predict your words!
🧠 Using Hugging Face's open-source language models

🤖 Setting up language model for word prediction...
📝 You'll need a Hugging Face API key for the model to work.
💡 Get a free API key at: https://huggingface.co/settings/tokens
🔑 Enter your Hugging Face API key (or press Enter to use fallback): 

📝 Enter a word for the model to guess: python

🎯 Target word: python
📏 Word length: 6
🎲 Max attempts allowed: 12
📝 Word state: _ _ _ _ _ _

🤖 Language model is analyzing the word...

🤖 Model predicts: 'e' (Attempt 1/12)
❌ Wrong! Letter 'e' is not in the word.
📝 Word state: _ _ _ _ _ _
🔤 Guessed letters: e
🎯 Correct letters found: 0/6

🤖 Model predicts: 't' (Attempt 2/12)
✅ Correct! Letter 't' found at positions: [4]
📝 Word state: _ _ _ t _ _
🔤 Guessed letters: e, t
🎯 Correct letters found: 1/6

... (continues until success or failure)
```

## Technical Details

- **Model**: GPT-2 (open-source, free to use)
- **API**: Hugging Face Inference API
- **Prompt Engineering**: Context-aware prompts for hangman game state
- **Fallback**: Letter frequency analysis if API unavailable
- **Response Parsing**: Extracts predictions from model responses

## Requirements

- Python 3.6 or higher
- requests library
- Internet connection (for API calls)
- Optional: Hugging Face API key for full functionality

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the game:
   ```bash
   python hangman_bot.py
   ```

## API Key Setup

For the best experience, get a free Hugging Face API key:

1. Visit https://huggingface.co/settings/tokens
2. Create a free account
3. Generate an API key
4. Enter it when prompted in the game

**Note**: The game works without an API key using fallback prediction, but the language model provides much better predictions!

## How It Differs from Simple Word Lists

Unlike simple word list approaches, this bot:
- **Understands Context**: The model comprehends the hangman game state
- **Makes Intelligent Decisions**: Uses language understanding to predict letters
- **Learns from Patterns**: Recognizes word structures and common combinations
- **Adapts to Game State**: Changes strategy based on revealed letters

Enjoy watching the AI model think and predict your words! 🎮 