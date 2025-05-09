import random
def play():
    user=input("'r' for rock,'p' for paper and 's' for scissors:" )
    computer=random.choice(['r','p','s'])
    print(f"Computer Choice {computer}")
    if user==computer:
        return "it's a tie"
    if is_win(user,computer):
        return 'User Win'
    else:
        return 'Computer Win'
        
def is_win(player1,player2):
    if(player1=='r' and player2=='s') or (player1=='s' and player2=='p') or (player1=='p' and player2=='r'):
        return True
winner=play()
print(winner)
