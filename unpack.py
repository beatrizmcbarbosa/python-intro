def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

# By using * in *coins, I am unpacking in individual members of the coins list
# * can take a data structure and unpack it
print(total(*coins), "Knuts")
