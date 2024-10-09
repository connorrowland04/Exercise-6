import random 

# Driver: Connor Rowland
# Navigator: Gokul Mahendran
# Date: 10/02/2024 
# Exercise 5 - Marathon 

class Marathon:
    def __init__(self,name,position = 0): 
        self.name = name 
        self.position = position 
        print("Good Job")



class RedPlayer(Marathon): 
    def walk(self):
        steps = random.randrange(1,11)
        self.position += steps


class BluePlayer(Marathon):
    def walk(self):
        steps = random.randrange(1,11)
        self.position += steps


def play_game():
    player_list = []
    x = 1 
    while len(player_list) < 6: 
        if x <= 3:
            player_list.append(BluePlayer(f"BluePlayer{x}"))
        else: 
            player_list.append(RedPlayer(f"RedPlayer{x + 3}"))
        x += 1
    turns = 0 
    while True:
        turns += 1
        for player in player_list:
            player.walk()
            if player.position >= 100:
                return player.name,turns




if __name__ == "__main__":
    winner, turns = play_game() 
    print(f"The Winner is... {winner} and it took {turns} turns")

