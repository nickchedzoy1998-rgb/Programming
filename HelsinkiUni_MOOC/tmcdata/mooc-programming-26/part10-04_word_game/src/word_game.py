# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        else:
            return None


class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        vowels = ["a", "e", "i", "o", "u"]

        p1_vowels = 0
        p2_vowels = 0

        for char in player1_word:
            if char in vowels:
                p1_vowels +=1

        for char in player1_word:
            if char in vowels:
                p2_vowels +=1
        
        if p1_vowels > p2_vowels:
            return 1
        elif p2_vowels > p1_vowels:
            return 2
        else:
            return None
        

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        valid = ['rock', 'paper', 'scissors']

        if player1_word not in valid and player2_word not in valid:
            return None
        elif player1_word in valid and player2_word not in valid:
            return 1
        elif player1_word not in valid and player2_word in valid:
            return 2
        
        elif player1_word == 'rock' and player2_word == 'scissors':
            return 1
        elif player1_word == 'rock' and player2_word == 'paper':
            return 2
        elif player1_word == 'paper' and player2_word == 'rock':
            return 1
        elif player1_word == 'paper' and player2_word == 'scissors':
            return 2
        elif player1_word == 'scissors' and player2_word == 'paper':
            return 1
        elif player1_word == 'scissors' and player2_word == 'rock':
            return 2
        
        elif player1_word == player2_word:
            return None
        
if __name__ == '__main__':
    p = RockPaperScissors(4)
    p.play()



        






if __name__ == '__main__':
    p = LongestWord(3)
    p.play()