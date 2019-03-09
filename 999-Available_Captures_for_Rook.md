### 999 Available Captures for Rook

Easy

On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2019/02/20/1253_example_1_improved.PNG)

```
Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
In this example the rook is able to capture all the pawns.
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2019/02/19/1253_example_2_improved.PNG)

```
Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation: 
Bishops are blocking the rook to capture any pawn.
```

**Example 3:**

![img](https://assets.leetcode.com/uploads/2019/02/20/1253_example_3_improved.PNG)

```
Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
The rook can capture the pawns at positions b5, d6 and f5.
```

 

**Note:**

1. `board.length == board[i].length == 8`
2. `board[i][j]` is either `'R'`, `'.'`, `'B'`, or `'p'`
3. There is exactly one cell with `board[i][j] == 'R'`



#### Solution

This problem is very simple, find the rook first, than try four different directions

* If encounter pawn, result ++ and break
* If encounter bishop, break

```python
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook = [-1, -1]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    rook[0] = i
                    rook[1] = j
                    break
        
        result = 0
        # left
        x = rook[0]
        y = rook[1]
        
        while(x >= 0):
            if board[x][y] == 'B':
                break
            elif board[x][y] == 'p':
                result += 1
                break
            x -= 1
                
        # right
        x = rook[0]
        y = rook[1]
        
        while(x < 8):
            if board[x][y] == 'B':
                break
            elif board[x][y] == 'p':
                result += 1
                break
            x += 1
            
        # up
        x = rook[0]
        y = rook[1]
        
        while(y >= 0):
            if board[x][y] == 'B':
                break
            elif board[x][y] == 'p':
                result += 1
                break
            y -= 1
            
        # down 
        x = rook[0]
        y = rook[1]
        
        while(y < 8):
            if board[x][y] == 'B':
                break
            elif board[x][y] == 'p':
                result += 1
                break
            y += 1
            
        return result
```

