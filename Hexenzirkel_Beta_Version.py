import random

rnd = 0
mx_rnd = 8
mx_pnt = 5
cards = 6

# Cards for players
ph = [1, 1, 1, 1, 1, 1, 0]
pc = [1, 1, 1, 1, 1, 1, 0]

print("\n\t\t\t\t\t\t     START GAME  \t\t\t\n")
print("\t\t\t\t===================  Hexenzirkel  ====================\n")


# Function to evaluate the score of the curent state
def print_cards(ph, pc):
    print("---------")

    print("Your Cards: ", end="")
    for i in range(cards):
        if ph[i] == 1:
            print(chr(65 + i), end=" ")
        else:
            print(" ", end=" ")

    print("\nAI's Cards: ", end="")
    for i in range(cards):
        if pc[i] == 1:
            print(chr(65 + i), end=" ")
        else:
            print(" ", end=" ")
    print("\n---------")


# Function to check if the game is over
def game_over(ph, pc, rnd):
    return rnd == mx_rnd or ph[cards] == mx_pnt or pc[cards] == mx_pnt


def minimax(ph, pc, rnd, max_mode, alpha, beta):
    if (rnd == mx_rnd) or game_over(ph, pc, rnd):
        return (pc[cards] - ph[cards])

    if max_mode:
        best = -10

        for i in range(cards):
            if ph[i] == 0:
                continue
            else:
                flag = False
                for j in range(cards):
                    if pc[j] == 0:
                        continue

                    elif (((j + 1) % cards) == i) or (((j + 2) % cards) == i):

                        pc[cards] += 1
                        pc[j] = 0

                        val = minimax(ph, pc, rnd + 1, False, alpha, beta)

                        pc[cards] -= 1
                        pc[j] = 1

                    else:
                        continue

                    best = max(best, val)
                    alpha = max(alpha, best)

                    # Alpha Beta Pruning
                    if beta <= alpha:
                        flag = True
                        break

            if flag:
                break

        return best


    else:
        best = 10

        for i in range(cards):
            if ph[i] == 0:
                continue
            else:
                flag = False
                for j in range(cards):
                    if pc[j] == 0:
                        continue

                    elif (((i + 1) % cards) == j) or (((i + 2) % cards) == j):

                        ph[cards] += 1
                        ph[i] = 0

                        val = minimax(ph, pc, rnd + 1, True, alpha, beta)

                        ph[cards] -= 1
                        ph[i] = 1

                        best = min(best, val)
                        beta = min(beta, best)

                        # Alpha Beta Pruning
                        if beta <= alpha:
                            flag = True
                            break

            if flag:
                break

        return best


# Function to make the computer's move using the minimax algorithm
def make_AI_move(ph, pc, rnd):
    best_score = -10
    best_move = None

    for i in range(cards):
        if ph[i] == 0:
            continue
        else:
            for j in range(cards):
                if pc[j] == 0:
                    continue

                elif (((j + 1) % cards) == i) or (((j + 2) % cards) == i):
                    pc[cards] += 1
                    pc[j] = 0

                    val = minimax(ph, pc, rnd + 1, False, -10, 10)

                    pc[cards] -= 1
                    pc[j] = 1

                    if val > best_score:
                        best_score = val
                        best_move = j

    return best_move


# Function to make the player's move
def make_player_move(ph):
    inp = input("\nEnter your move: ")

    if (inp >= 'G') or (inp < 'A'):
        print("Invalid Card Choice")
        return make_player_move(ph)

    mv = ord(inp) - 65

    if ph[mv] == 1:
        return mv
    else:
        print("Invalid Move")
        return make_player_move(ph)


while not game_over(ph, pc, rnd):

    print_cards(ph, pc)

    h_move = make_player_move(ph)
    ai_move = make_AI_move(ph, pc, rnd)

    if ai_move == None:

        rmv = []
        for i in range(cards):
            if pc[i] == 1:
                rmv.append(i)
        ai_move = rmv[random.randint(0, len(rmv))]

    print("AI move: ", chr(65 + ai_move))

    if (h_move == ai_move) or (((h_move + 3) % cards) == ai_move):
        print("Its a draw. Retake")
        continue

    elif (((h_move + 1) % cards) == ai_move) or (((h_move + 2) % cards) == ai_move):
        ph[cards] += 1
        ph[h_move] = 0

    else:
        pc[cards] += 1
        pc[ai_move] = 0

    rnd += 1
    print("\nYour score: ", ph[cards])
    print("AI's score: ", pc[cards])

print_cards(ph, pc)

# Determine the winner
if ph[cards] > pc[cards]:
    print("\n\nYou win!")
elif ph[cards] < pc[cards]:
    print("\n\nAI wins!")
else:
    print("\n\nIt's a draw!")

print("\n\n\n\nThe End\n\n\n\n")

import hex_restart_close
