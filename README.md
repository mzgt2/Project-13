# Project-13

## Higher or Lower Game 📊

A command-line game where you guess which celebrity, brand, or public figure has more social media followers. Inspired by the Higher Lower game.

## Requirements
```bash
pip install art
```

**Required Files:**
- `game_data.py` - Contains the data dictionary with follower counts

## Data Structure

Your `game_data.py` should contain a list of dictionaries with this format:
```python
data = [
    {
        'name': 'Instagram',
        'follower_count': 600,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 500,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    # Add more entries...
]
```

## How to Run
```bash
python higher_lower.py
```

## How to Play

1. The game presents two options: **A** and **B**
2. Each option shows a name, description, and country
3. Guess which one has more followers by typing `A` or `B`
4. If correct, your score increases and you continue
5. Option B becomes the new A, and a new B is randomly selected
6. If wrong, game ends and displays your final score

## Game Rules

- Type `A` if you think option A has more followers
- Type `B` if you think option B has more followers
- Each correct guess adds 1 point to your score
- One wrong guess ends the game
- Try to get the highest score possible!

## Example Gameplay
```
  _   _ _       _                 
 | | | (_)     | |                
 | |_| |_  __ _| |__   ___ _ __   
 |  _  | |/ _` | '_ \ / _ \ '__|  
 | | | | | (_| | | | |  __/ |     
 \_| |_/_|\__, |_| |_|\___|_|     
           __/ |                  
          |___/                   

Compare A: Instagram, Social media platform, United States

 _    __    
| |  / /    
| | / / ___ 
| |/ / / __|
|   <  \__ \
|_|\_\ |___/

Against B: Cristiano Ronaldo, Footballer, Portugal

Who has more followers? Type 'A' or 'B': a

Correct answer! Your score is 1.

Compare A: Instagram, Social media platform, United States

 _    __    
| |  / /    
| | / / ___ 
| |/ / / __|
|   <  \__ \
|_|\_\ |___/

Against B: Selena Gomez, Musician and actress, United States

Who has more followers? Type 'A' or 'B': b

Wrong answer. Your final score is 1
```

## Features

- ASCII art logo and VS display
- Screen clear effect between rounds (`\n * 20`)
- Running score tracker
- Random selection prevents predictable patterns
- Winning option carries forward as next comparison

## Game Mechanics

- **Correct guess**: Score +1, winning option becomes new A, new random B generated
- **Wrong guess**: Game ends, final score displayed
- **Screen management**: Clears previous round for clean display

## What I Learned

Building this game taught me:

- **Data structure handling** - Working with lists of dictionaries
- **Comparison logic** - Implementing conditional comparisons between data points
- **Game state management** - Tracking score and game flow
- **Random selection** - Using `random.choice()` for unpredictable gameplay
- **Variable reassignment** - Carrying winning values forward (`A = B`)
- **User experience** - Screen clearing for better visual flow
- **Modular design** - Separating game data from game logic

This project reinforced working with external data and creating engaging comparative game mechanics.

Enjoy the challenge! 🎮
