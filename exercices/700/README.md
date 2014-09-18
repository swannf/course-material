# Make your own 2048 in python !

During this exercise you will build your own [2048](https://gabrielecirulli.github.io/2048/) game ! If you never played, have some fun [here](https://gabrielecirulli.github.io/2048/) for a moment :)

## Rules of the game

The board is a 4 by 4 matrice (ie. a list of 4 lists of length 4). When initialized, all positions are empty except 2 randomly chosen positions set to 2.

Then, the player interact with the game by entering a direction (up, down, right, left) and 3 things happens:
- All elements fall such as gravity whose pulling in that direction.
- If two positions are one under the other when "falling", they merge by adding their values into one single position.
- A new elements pops in a random empty position, set randomly either to 2 or 4.

The player looses if no empty position are available to add new elements.

The player wins if one position reach the value 2048.

## Step 1 :: Initiate the grid (*easy*)

Provide the function `init_grid()` that will return a random board for starting the game.


## Step 2 :: Add new element to the grid (*easy++*)

Provide the function `add_new(grid)` that will add either a 2 or a 4 somewhere empty in any board. If no empty position is available, `add_new` should return "Game Over !".

## Step 3 :: Moving the grid (*intermediate++*)

Provide the function `move_grid(grid, direction)` where `grid` is the grid to be moved and the direction to be taken, `l` (left), `r` (right), `u` (up) and `d` (down).

This implies making fall the elements in the given direction, merging elements when necessary and adding a new element.

If no new element can be added, `move_grid` return "Game Over !". If 2048 is present on the board, `move_grid` returns "You Won !".

## Step 4 :: Create an AI to solve the game (*hard++*)



## References
