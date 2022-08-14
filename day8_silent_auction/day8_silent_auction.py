from replit import clear
import sys
try:
    sys.path.insert(0,'C:\\Users\\jon_w\\100days_of_code\\day6_hangman' )
    from day6_hangman import get_word
except:
    print('Import Exception')

    def get_word():
        return 'Gold nugget'

def get_price(item):
    start = len(item)
    for count,letter in enumerate(item):
        start += count + (count/ start+3) *.56
    return start * 19.7

def return_winning_bidder(item,auction):
    highest_bid = auction[item]['Reserve']
    highest_bidder = 'Reserve'

    for bid in auction[item]:
        if auction[item][bid] > highest_bid:
            highest_bid = auction[item][bid]
            highest_bidder = bid
        elif auction[item][bid] == highest_bid:
            continue

    return (highest_bidder, highest_bid)

def main_loop():
    try:
        item = get_word()
        auction = {}
        auction[item] = {'Reserve': float(f'{get_price(item):.2f}')}

        auction_on = True
        while auction_on:
            print(f'Welcome to the Silent Auction\nTodays item is an {item}')
            print(f"Reserve price for {item} is £{auction[item]['Reserve']}")
            print(f'Current bidders: {len(auction[item])-1}\n------------------------------\n')
        
            name = input('Please enter your name:\n')
            offer = float(input('please enter your offer:'))
            auction[item][name] = float(f'{offer:.2f}')

            finished = input('Any more bidders? (Y/N)')
            if finished.upper() != 'N':
                clear()
                continue
            else:
                auction_on = False
        winning_bidder, winning_bid = return_winning_bidder(item, auction)
        if winning_bidder != 'Reserve':     
            print(f'The winning bid was £{winning_bid:.2f} by {winning_bidder}')
            print(auction)
        else:
            print(f'Reserve of £{winning_bid:.2f} was not met.')
    except:
        clear()
        print('Input error\nTry again')
        main_loop()


  


if __name__ == '__main__':
    main_loop()