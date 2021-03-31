# could not remember if i should use radint or randrange so checked that
# randint would randomly generate all flour of all numbers1, 2, 3, 4

import random

NUM_TRAILS = 100
winnings = 0

cost = NUM_TRAILS * 5

for item in range (0, NUM_TRAILS):
    prize = ""
    round_winnings = 0

    for thing in range(0, 3):

            # randint finds numbers between given endpoints, including both endpoints
        prize_num = random.randint(1,10)
        # prize += " "
        if prize_num == 1:
            # one in ten chance of getting gold
            # prize += "gold"
            round_winnings += 5
        elif prize_num == 2:
            # get silver if its a 2 or 3
            # prize += "silver"
            round_winnings += 2
        elif prize_num == 3:
            # copper if its 4, 5, 6, 7 <40: chance of copper>
            # prize += "copper"
            round_winnings += 1
        else:
            prize += "lead"
    # print("You won {} which is worth {}".format(prize, round_winnings))
    winnings += round_winnings

print("Paid In: ${}".format(cost))
print("Paid Out: ${}".format(winnings))

if winnings > cost:
    print("You came out ${} ahead".format(winnings - cost))
else:
    print("Sorry, you lost ${}".format((cost - winnings)))

