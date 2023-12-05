import random

board =[]
deck = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100']
number_of_players = []
station = []

def main():
    shuffle_cards()
    print("the drawn card is", draw_card(),"\n")
    show_station()
    print("the board is now [", board,"]\n", sep="")
    carry_on()

def confirm_players():
    global number_of_players
    prompt = input("Enter number of players \n")
    number_of_players.append(prompt)
    print("there are", number_of_players[0], "players\n")
    return number_of_players

def shuffle_cards():
    return random.shuffle(deck)

def create_station():
    global number_of_players
    station.append(random.sample(deck,int(number_of_players[0])))
    return station

def show_station():
    print("stations        ", station)

def draw_card():
    card = deck.pop()
    global board
    def insert_card(card_to_be_inserted): 
        #takes in variable card_to_be_inserted
        board.insert(0,card_to_be_inserted)
    insert_card(card)
    return (card)

def carry_on():
    #checks how the game should progress to keep adding to board or proceed the train
    global number_of_players
    question = input("Next? Enter y for yes; else anything key to cancel \n")
    if question == "y" and len(deck) != 0 and len(board) < int(number_of_players[0]):
        main()
    elif question == "y" and len(board) == int(number_of_players[0]):
         moving_train(int(number_of_players[0]))
    else:
        print("operation cancelled")

def moving_train(n=0): 
    #advances the train by checking if the no. of elements in [Board] =n; n = no. of players
    global board
    if board.count("__") != n:
        board.insert(0,"__")
        board.pop()
        show_station()
        print ("the board is now [", board,"]\n", sep="")
        carry_on()
    else:
        print("[train has passed]]}>\n","o o o o o o o o")                

if __name__ == '__main__':
    confirm_players()
    create_station()
    main()



