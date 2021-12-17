# Rules:
# 1. To win the match, a team must win 3 sets.
# 2. To win a set, a team must win at least 25 points with a 2-points margin minimum, e.g. 25-27, 24-26, 28-26.
# 4. Team 1 starts serving in set 1, Team 2 starts serving in set 2, Team 1 starts serving in set 3, and so on.
# 5. The team that won the previous point serves for the next point, unless the set is just starting.

from random import random
from time import time


def printInfo():
    '''
    function:  print information about the program 
    '''
    print("{:*^70}".format(" product introduction "))
    print(" the product name ：  volleyball competition simulation analyzer ")
    print(" product overview ：  by entering 2 teams A and b's ability value (0 decimal representation between pi and 1 )， able to simulate 2 teams multiple times A a volleyball match against b ， to figure out their winning percentage ！")
    print(" products of the author ：  step ordinary - 04")
    print("{:*^70}".format(" simulation start "))


def getInputs():
    '''
    function:  get the parameters entered by the user 
    '''
    probA = eval(input(" please enter the capability value of team a (0~1)："))
    probB = eval(input(" please enter the capability value of team b (0~1)："))
    n = eval(input(" please enter the number of matches you want to simulate ："))
    return probA, probB, n


def printResult(n, winsA, winsB):
    '''
    function:  output the results of simulated matches 
    '''
    print("{:*^70}".format(" end of the simulation "))
    print(" competition analysis begins, total simulation {} games. ".format(n))
    print(">>> team a wins {} a match, a share {:0.1%}".format(winsA, winsA/n))
    print(">>> team b wins {} a match, a share {:0.1%}".format(winsB, winsB/n))


def simNGames(n, probA, probB):
    '''
    function:  simulate n games 
    n:  simulate n games 
    probA, probB:  are team a and B the ability to value 
    winA, winB:  team a and B the number of innings won in a game 
    winsA, winsB:  team a and B number of games won, total n field 
    '''
    winsA, winsB = 0, 0
    for _ in range(n):
        winA, winB = simOneGame(probA, probB)
        if winA > winB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


def simOneGame(probA, probB):
    '''
    function:  simulate a game, including five rounds ， the best-of-five system is adopted 
   probA, probB：  are team a and B the ability to value 
   return:  return to team a and B the number of games won in the game 
   scoreA, scoreB:  are team a and B the score of a game 
    winA, winB:  are team a and B the number of games won 
    N:  represents the game's innings 
    '''
    winA, winB = 0, 0
    for N in range(5):
        serving = 'B' if N % 2 == 0 else 'A' 
        scoreA, scoreB = simAGame(N, probA, probB, serving)
    if scoreA > scoreB:
        winA += 1
    else:
        winB += 1
    if winA == 3 or winB == 3:
        return winA, winB


def simAGame(N, probA, probB, serving):
    '''
    function:  simulated game 
    N:  represents the game's innings 
    probA, probB：  are team a and B the ability to value 
    return:  return to team a and B points won in a competition 
    '''
    scoreA, scoreB = 0, 0  # are team a and B the score of a game
    while not GameOver(N, scoreA, scoreB):
        if serving == 'A':
            if random() > probA:
                scoreB += 1
                serving = 'B'
            else:
                scoreA += 1
        else:
            if random() > probB:
                scoreA += 1
                serving = 'A'
            else:
                scoreB += 1
    return scoreA, scoreB


def GameOver(N, scoreA, scoreB):
    # '''
    # function:  define the end conditions of a match
    # N:  represents the current game ( the fifth game was a decider )
    # return:  true if the end of match condition is true, false otherwise
    # '''
    if N <= 4:
        return (scoreA >= 25 and abs(scoreA-scoreB) >= 2) or (scoreB >= 25 and abs(scoreA-scoreB) >= 2)
    else:
        return (scoreA >= 15 and abs(scoreA-scoreB) >= 2) or (scoreB >= 15 and abs(scoreA-scoreB) >= 2)


if __name__ == "__main__":
    printInfo()
    probA, probB, n = getInputs()
    Time = time()
    winsA, winsB = simNGames(n, probA, probB)
    print(" simulation time : {:.1f}s".format(time()-Time))
    printResult(n, winsA, winsB)
