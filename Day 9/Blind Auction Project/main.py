import art

# TODO-1: Ask the user for input
print(art.logo)
user_data = {}
other_bids = 'yes'
while other_bids == 'yes':

    name = input("What is your name?:")
    price = int(input("What is your bid?: $"))
    user_data[name] = price
    other_bids = input("Are there any other bidders? Type 'yes' or 'no': ")
    if other_bids == 'yes' :
        print("\n" * 100)

max_bids = 0
winner = ""
for key, value in user_data.items():
    if value > max_bids:
        max_bids = value
        winner = key
print(f'The winner is {winner} with a bid of ${max_bids}')
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


