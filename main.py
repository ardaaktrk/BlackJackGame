from art import logo
from replit import clear
import random

play_game = "n"

def calculate_score(list_of_cards):
  """will return the total score of hand, returns 0 if blackjack occurs"""
  if len(list_of_cards) == 2 and sum(list_of_cards) == 21:
    return 0 # 0 will represent blackjack
  else:
    if 11 in list_of_cards and sum(list_of_cards) > 21:
      index = list_of_cards.index(11)
      list_of_cards[index] = 1
    return sum(list_of_cards)

def compare_scores(player_score, dealer_score):
  """compare scores of player and dealer, print the result"""
  if player_score == dealer_score:
    return "Draw 😮‍💨"
  elif player_score == 0:
    return "Blackjack! You win 🥳"
  elif dealer_score == 0:  
    return "Dealer has blackjack. You lose 😢"
  elif player_score > dealer_score:
    return "You win 🤩" 
  else:
    return "You lose 😞"
  
def game():
  clear()
  print(logo) 
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  
  player_hand, dealer_hand = [], []
  player_score, dealer_score = 0, 0
  draw = random.choice
  for i in range(2):
    player_hand.append(draw(cards))
    dealer_hand.append(draw(cards))

  player_score = calculate_score(player_hand)
  dealer_score = calculate_score(dealer_hand)
    
  print(f"Your hand: {player_hand}, your score: {player_score}")
  print(f"Dealer's hand: [{dealer_hand[0]}, x]")

  game_continues = True
  player_draws = True
  player_bust = False
  dealer_bust = False

  while player_draws:
    player_draws = input("Do you want to hit or stand? Type 'H' or 'S': ").lower()
    if player_draws == "h":
      new_card = draw(cards)
      player_hand.append(new_card)
      player_score = calculate_score(player_hand)
      print(f"Your hand: {player_hand}, your score: {player_score}")
      if player_score > 21:
        player_draws = False
        player_bust = True
        print(f"Dealer hand: {dealer_hand}, dealer's score: {dealer_score}")
        print("Bust. You lose 😣")
    else:
      player_draws = False
      while dealer_score != 0 and dealer_score < 17:
        new_card = draw(cards)
        dealer_hand.append(new_card)
        dealer_score = calculate_score(dealer_hand)
      print(f"Dealer hand: {dealer_hand}, dealer's score: {dealer_score}")
      if dealer_score > 21:
        player_bust = True
        print("Dealer bust. You win 🥳")
  # Neither player nor dealer bust. Compare scores 
  if not (player_bust or dealer_bust):
    print(compare_scores(player_score, dealer_score))
    

play_game = input("Do you want to play a game of BlackJack 21?: Type 'Y' or 'N': ").lower()
while play_game != 'n':
  game()
  play_game = input("Do you want to play again? Type 'Y' or 'N': ").lower()
          
      

      
    
  


    

  

    
        
        
      
  
    
  