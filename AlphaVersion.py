import math

# The game board is represented as a list of characters
#board = ['-'] * 9
rnd = 0
mx_rnd = 3
mx_pnt = 3
cards = 3

# Cards for players
ph = [1,1,1,0]
pc = [1,1,1,0]

# Function to evaluate the score of the curent state
def print_cards(ph,pc):
    print("---------")
    
    for i in range(cards):
        print(ph[i], end = " ")
    print("---------")
        
    for i in range(cards):
        print(pc[i],end = " ")
    print("---------")

# Function to check if a player has won
def evaluate(ph,pc):
   
    if ph[cards] > pc[cards]:
        return 1
    elif ph[cards] < pc[cards]:
        return -1
    else:
        return 0

# Function to check if the game is over (draw or win)
def game_over(ph,pc,rnd):
    return rnd == mx_rnd or ph[0] == mx_pnt or pc[0] == mx_pnt


# Function to evaluate the score of the current board position
"""def evaluate(board):
    if check_winner(board, PLAYER_X):
        return 1
    elif check_winner(board, PLAYER_O):
        return -1
    else:
        return 0"""

def minimax(ph, pc, rnd, maximizingPlayer, alpha, beta):
  
    # Terminating condition. i.e
    # leaf node is reached
    if (rnd == mx_rnd) or game_over(ph,pc,rnd):
        return evaluate(ph,pc)
 
    if maximizingPlayer:
      
        best = -2
 
        # Recur for left and right children
        for i in range(cards):
            if ph[i] == 0:
                continue
            else:
                for j in range(cards):
                    if pc[j] == 0:
                        continue
                        
                    elif ((i+1) % cards) == j:
                        ph[cards] += 1
                        ph[i] = 0
                        
                        #itet(ph, pc, dep+1)
                        val = minimax(ph, pc, rnd+1, False, alpha, beta)
                        
                        ph[cards] -= 1
                        ph[i] = 1
        
                    elif i == j:
                        #itet(ph, pc, dep+1)
                        continue
                    else:
                        pc[cards] += 1
                        pc[j] = 0
                        
                        #itet(ph, pc, dep+1)
                        val = minimax(ph, pc, rnd+1, False, alpha, beta)
                        
                        pc[cards] -= 1
                        pc[j] = 1
                    
                    best = max(best, val)
                    alpha = max(alpha, best)
                    
                    # Alpha Beta Pruning
                    if beta <= alpha:
                        break
          
        return best
      
    else:
        best = 2
 
        # Recur for left and
        # right children
        for i in range(cards):
            if ph[i] == 0:
                continue
            else:
                for j in range(cards):
                    if pc[j] == 0:
                        continue
                        
                    elif ((i+1) % cards) == j:
                        ph[cards] += 1
                        ph[i] = 0
                        
                        #itet(ph, pc, dep+1)
                        val = minimax(ph, pc, rnd+1, True, alpha, beta)
                        
                        ph[cards] -= 1
                        ph[i] = 1
                    elif i == j:
                        #itet(ph, pc, dep+1)
                        continue
                    else:
                        pc[cards] += 1
                        pc[j] = 0
                        
                        #itet(ph, pc, dep+1)
                        val = minimax(ph, pc, rnd+1, True, alpha, beta)
                        
                        pc[cards] -= 1
                        pc[j] = 1
        
                    best = min(best, val)
                    beta = min(alpha, best)
 
                    # Alpha Beta Pruning
                    if beta <= alpha:
                        break
          
        return best
        
        
      

# Minimax algorithm with alpha-beta pruning

"""def minimax(ph, pc, depth, maximizing_player, alpha, beta):
    if depth == 0 or game_over(board):
        return evaluate(board)

    if maximizing_player:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == EMPTY_CELL:
                board[i] = PLAYER_X
                eval = minimax(board, depth - 1, False, alpha, beta)
                board[i] = EMPTY_CELL
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval

    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == EMPTY_CELL:
                board[i] = PLAYER_O
                eval = minimax(board, depth - 1, True, alpha, beta)
                board[i] = EMPTY_CELL
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval
        """

# Function to make the computer's move using the minimax algorithm
def make_AI_move(ph,pc,rnd):
    
    best_score = -2
    best_move = None 
        # Recur for left and
        # right children
    for i in range(cards):
        if ph[i] == 0:  
            continue
        else:
            for j in range(cards):
                if pc[j] == 0:
                    continue
                        
                elif ((i+1) % cards) == j:
                    ph[cards] += 1
                    ph[i] = 0
                        
                    #itet(ph, pc, dep+1)
                    val = minimax(ph, pc, rnd+1, False, -2, 2)
                        
                    ph[cards] -= 1
                    ph[i] = 1
                elif i == j:
                        #itet(ph, pc, dep+1)
                        continue
                else:
                    pc[cards] += 1
                    pc[j] = 0
                        
                    #itet(ph, pc, dep+1)
                    val = minimax(ph, pc, rnd+1, False, -2, 2)
                        
                    pc[cards] -= 1
                    pc[j] = 1
        
                if val > best_score:
                    best_score = val
                    best_move = j
    
    return best_move
    

# Function to make the player's move
def make_player_move(ph):
    #valid_moves = [i for i in range(9) if board[i] == EMPTY_CELL]
    mv = int(input("Enter your move: "))
    
    if ph[mv] == 1:
        return mv
    else:
        print("Invalid Move")
        make_player_move(ph)


while not game_over(ph,pc,rnd):
    
    print_cards(ph,pc)
    
    h_move = make_player_move(ph)
    ai_move = make_AI_move(ph,pc,rnd)
    
    print("AI move: ",ai_move)
    
    if h_move == ai_move:
        print("Its a draw. Retake")
        continue
    
    elif ((h_move + 1) % cards) == ai_move:
        ph[cards] += 1
        ph[h_move] = 0
                        
    else:
        pc[cards] += 1
        pc[ai_move] = 0

    rnd += 1
    print("Your score: ",ph[cards])
    print("AI's score: ",pc[cards])


# Determine the winner
if ph[cards] > pc[cards]:
    print("Player wins!")
elif ph[cards] < pc[cards]:
    print("AI wins!")
else:
    print("It's a draw!")
   