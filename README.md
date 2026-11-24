# Final Project: Personal Mini-Toolkit

## Project Description

The Personal Mini-Toolkit is a Python program that provides three useful tools through one menu.

### Tools
1. **Simple Calculator** - performs addition, subtraction, multiplication and division.
2. **To-Do List** - allows users to add, view and remove tasks. Tasks remain in the list while the program is running, even after returning to the main menu.
3. **Number Guessing Game** - challenges users to guess a randomly generated number between 1 and 10.

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run the program:

   ```bash
   python toolkit.py
   ```

5. Follow the menu instructions. Choose option 4 to quit.

## Python Concepts Used

- Variables and data types
- Input and output
- Lists
- For and while loops
- If, elif and else statements
- Functions
- Try and except error handling
- The random module
- F-strings

## Screenshots

Add your own screenshots to the `screenshots/` folder. Include the main menu (including an invalid menu choice) and evidence of each of the three tools running.

## Reflection

The hardest part of this project was organizing three different tools so that they work correctly inside one menu. I had to make sure the program returns to the main menu after each tool finishes. The to-do list was challenging because I wanted tasks to remain available when I returned to it. The longest debugging challenge was handling invalid number input and preventing division by zero. I learned how functions, lists, loops and conditionals can work together in a useful program. I also learned that try and except can prevent common input errors from stopping the program. If I had one more week, I would add a feature to save tasks in a file so they remain available after the program closes.
