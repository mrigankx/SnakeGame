# About Snake-Game
Snake is the common name for a video game concept where the player maneuvers a line which grows in length, with the line itself being a primary obstacle. The concept originated in the 1976 arcade game Blockade, and the ease of implementing Snake has led to hundreds of versions (some of which have the word snake or worm in the title) for many platforms. After a variant was preloaded on Nokia mobile phones in 1998, there was a resurgence of interest in the snake concept as it found a larger audience.

APA - Wikipedia contributors. (2020, March 30). Snake (video game genre). In Wikipedia, The Free Encyclopedia. Retrieved 11:00, May 2, 2020

, from https://en.wikipedia.org/w/index.php?title=Snake_(video_game_genre)&oldid=948244431

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pygame.

```bash
pip install pygame
```

## Built with
* [Python](https://python.com)

## How to run this project
1) Clone the Repository.
2) Switch to master branch.
3) To run the project, enter and run
```bash
python app.py
```
# Project Tree
1) `config.py` - Contains all the constant variables declaration which are used by all the files. 
  
2) `apple.py` - Contains definitions of functions of `Apple`.It calculates the new position of the apple.

3) `snake.py` - Contains the functionality of the snake; like, the size, control and movement of the snake.

4) `game.py` - Contains the functionality of the whole game. It will draw the whole game board, snake, apple and the score. 

5) `app.py` - It will call the class Game from `game.py`. It will run the whole game.
 
---

