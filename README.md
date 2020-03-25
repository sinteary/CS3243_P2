## CS3243 Project 2

### Task 1: Sudoku

**Approach 1:**
* Maintain assignable numbers for each empty cell on the board as constraints.
* Use backtracking to try all the assignable numbers for each cell in order.
	* If succeed, proceed to the next empty cell.
	* If failed, backtrack by resetting the current cell empty and go back to the previous assignment.
* After each valid assignment, update the constraints for all remaining empty cells on the board

**Results:**
* Input1: `24.9235s`
* Input2: `2.7022s`
* Input3: `2.1306s`
* Input4: `0.4958s`



### Task 2: The Pacman Game
