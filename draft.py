import random
import csv
import time


def make_pick(rankings):  # selects a player then removes them from all rankings
    # select random list and best avail player from list
    rank_select = random.sample(rankings, 1)
    pick = rank_select[0][0]

    # remove selected player from all lists
    for rnk in rankings:
        p = None  # nullify
        for player in rnk:
            p = None  # nullify
            if player == pick:
                p = rnk.index(player)  # find drafted player in each ranking
                break  # break loop if player found
        if p is not None:
            rnk.pop(p)  # remove drafted player from ranking if player in rankings
    return pick, rankings  # return pick and updated rankings


def rundraft():  # runs through the first round of the draft with given rankings
    # initialize draft rankings
    rankings = []

    # iterate through text files and add each ranking to ranking list
    for k in range(1, 5):  # add more rankings as they come out
        k = str(k)
        draft_ranking = 'rnk' + k + '.txt'
        with open(draft_ranking, 'r') as f:
            rnk_list = [line.strip() for line in f]
        rankings.append(rnk_list)

    draftees = []  # players drafted

    i = 0
    while i < 31:
        draftees.append(make_pick(rankings)[0])
        i += 1
    return draftees


def main():
    # create dictionary of all possible players
    # key PlayerName, value empty list of all 31 possible draft spots
    players = {
        "Alexis Lafreniere": [0] * 31,
        "Tim Stuetzle": [0] * 31,
        "Quinton Byfield": [0] * 31,
        "Cole Perfetti": [0] * 31,
        "Jamie Drysdale": [0] * 31,
        "Jack Quinn": [0] * 31,
        "Yaroslav Askarov": [0] * 31,
        "Marco Rossi": [0] * 31,
        "Lucas Raymond": [0] * 31,
        "Hendrix Lapierre": [0] * 31,
        "Connor Zary": [0] * 31,
        "Jake Sanderson": [0] * 31,
        "Alexander Holtz": [0] * 31,
        "Dylan Holloway": [0] * 31,
        "Tyson Foerster": [0] * 31,
        "Anton Lundell": [0] * 31,
        "Dawson Mercer": [0] * 31,
        "William Wallinder": [0] * 31,
        "Rodion Amirov": [0] * 31,
        "Mavrik Bourque": [0] * 31,
        "Jeremie Poirier": [0] * 31,
        "Brendan Brisson": [0] * 31,
        "Seth Jarvis": [0] * 31,
        "Kaiden Guhle": [0] * 31,
        "Braden Schneider": [0] * 31,
        "Justin Barron": [0] * 31,
        "Daniel Torgersson": [0] * 31,
        "Shakir Mukhamadullin": [0] * 31,
        "Ozzy Wiesblatt": [0] * 31,
        "Ridly Greig": [0] * 31,
        "Eemil Viro": [0] * 31,
        "Noel Gunler": [0] * 31,
        "Jan Mysak": [0] * 31,
        "Lukas Cormier": [0] * 31,
        "John-Jason Peterka": [0] * 31,
        "Alexander Pashin": [0] * 31,
        "Zion Nybeck": [0] * 31,
        "Martin Chromiak": [0] * 31,
        "Vasily Ponomarev": [0] * 31,
        "Ty Smilanic": [0] * 31,
        "Thomas Bordeleau": [0] * 31,
        "Helge Grans": [0] * 31,
    }

    # run the draft k times
    j = 0
    k = 10000

    while j < k:
        draft = rundraft()  # save draft results in list
        # iterate through draft results and update the overall results
        for selection in draft:
            try:
                location = draft.index(selection)
                players[selection][location] += 1
            except:
                pass

        j += 1

        # progress
        if j == k // 1 or j == k // 2.5 or j == k // 2 or j == k // (5 / 3) or j == k // 1.25:
            print(round((j / k) * 100, 1), " % complete...", j, " simulations out of ", k, " completed")

    # write raw results to csv file
    with open('SimResultsRaw.csv', 'w') as f:
        w = csv.writer(f)
        w.writerows(players.items())

    # find percentage values for each player at each pick
    for values in players.values():
        values[:] = [float(num) / k * 100 for num in values]

    # write results with percentage values to csv file
    with open('SimResultsPercentage.csv', 'w') as f:
        w = csv.writer(f)
        w.writerows(players.items())


TimeStart = time.time()
main()
TimeEnd = time.time()
print('The simulation took: ', TimeEnd - TimeStart, ' seconds to complete')
