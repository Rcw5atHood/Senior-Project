# Travel Adventure Game

## Team Information
Jack Carr

Email: Jac26@hood.edu

Title: Developer

Rich Williams

Email: rcw5@hood.edu

Title: Developer

## Repository
URL: [https://github.com/Rcw5atHood/Senior-Project/tree/main/Seminar](https://github.com/Rcw5atHood/Senior-Project/tree/main/Seminar)

## About The Project
This is a travel adventure game where the player has a chance to visit various places, play different games at each destination, and enjoy a selection of soundtracks during the journey. The game includes features like choosing from different games to play at each location (Connect 4, Tic Tac Toe, or Tetris), a list of visited locations, a variable volume soundtrack, and win/lose scenarios for each game. The player can also skip to the next track if they want a different soundtrack.

Games included in the project:
1. Tic Tac Toe: The `tictactoe.py` module includes all the functionalities for this game. The player competes against the computer, which makes its moves based on a random selection among the available cells.

2. Connect 4: The `connect4.py` script is a complete implementation of the Connect Four game. It features a graphical user interface, a computer opponent that makes moves randomly, and checks for the win or draw condition. The main loop of the script, `connect4_main()`, continues until the game is over. The game handles both user input (for the human player) and AI actions (for the computer player).

3. Tetris: The `tetris.py` module implements the Tetris game. It includes shape formats for different pieces, color codes for each shape, and screen settings such as width, height, and cell size.

4. Constants: The `constants.py` module defines various constants used in the game, such as color codes (BLACK, WHITE, RED, etc.), screen dimensions, font sizes, and button information for the user interface.

5. Main: The `main.py` script is the entry point of the game. It initializes the pygame library, loads destination images, sets up the game window, handles user input and events, and manages the game's main loop.

project/
├── main.py
├── connect4.py
├── tictactoe.py
├── tetris.py
├── constants.py
├── images/
│   ├── gameman1.jpeg
│   ├── gameman2.jpeg
│   ├── gameman3.jpeg
│   ├── gameman4.jpeg
│   ├── destination1.jpeg
│   ├── destination2.jpeg
│   ├── paris.jpeg
│   ├── newyork.jpeg
│   ├── Tokyo.jpeg
│   ├── Sydney.jpeg
│   ├── cairo.jpeg
│   ├── Agra.jpeg
│   ├── dubrovnik.jpeg
│   ├── Copenhagen.jpeg
│   ├── Santorini.jpeg
│   ├── reykjavik.jpeg
│   ├── cinque_terre.jpeg
│   ├── Rome.jpeg
│   ├── Petra.jpeg
│   ├── Oslo.jpeg
│   ├── Svalbard.jpeg
│   ├── Machu_Picchu.jpeg
│   ├── Lisbon.jpeg
│   ├── Moscow.jpeg
│   ├── Edinburgh.jpeg
│   ├── Singapore.jpeg
│   ├── Cape_Town.jpeg
│   ├── Seoul.jpeg
│   ├── Barcelona.jpeg
│   ├── Granada.jpeg
│   ├── Madrid.jpeg
│   └── Hanoi.jpeg
├── sounds/
│   ├── slowjam.mp3
│   ├── slowjam1.mp3
│   ├── slowjam2.mp3
│   ├── slowjam3.mp3
│   ├── slowjam5.mp3
│   └── ...
├── README.md
└── requirements.txt




## Tech Stack
- Python: 3.8
- Pygame

The Python script makes use of several Pygame functionalities such as:
- pygame.mixer to play different soundtracks.
- pygame.font to handle various text appearances.
- pygame.display to manage the game window.
- pygame.event to handle different user interactions (clicks, key presses, etc).
- pygame.image and pygame.Surface to manage various images and screens in the game.
- pygame.time to control the game's frame rate and add delays when necessary.

## Getting Started
Here are the instructions to set up and run the project:

### Prerequisites
- Python 3.8
- Pygame

### Installation
1. Clone the repo
git clone https://github.com/Rcw5atHood/Senior-Project.git
2. Navigate to the project directory
cd Senior-Project/Seminar
3. Run the Python script
python main.py

## Contact

Contact
Jack Carr

Email: Jac26@hood.edu
Title: Developer
Rich Williams

Email: rcw5@hood.edu
Title: Developer

## Acknowledgments
We would liket to take this opportunity to extend our deepest gratitude and appreciation.  Our esteemed professors, your wisdom and guidance have been the bedrock of our academic journey, providing clarity and sparking curiosity at every turn. To our unwavering families, your endless support and faith in our abilities have given us the strength to push our limits and aim for the stars. To our dedicated classmates, your collaboration and shared insights have created a dynamic and enriching learning environment that goes beyond the traditional classroom. Each one of you has played an invaluable role in our educational journey, and for that, we are profoundly thankful.

