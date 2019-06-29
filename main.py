import time
from threading import Thread

from Game import Game

starttime = time.time()
#def func():

if __name__=='__main__':
    game = Game([260, 950, 2100, 5200, 8900],
                [25, 18, 26, 66, 21],
                [0.5, 0.7, 1, 1.5, 2],

                [220, 850, 1900, 5000, 8700],
                [16, 13, 26, 58, 36],
                [0.2, 0.4, 1, 1.2, 1.5])
    for i in range(0, 100000):
        print(i, game(), time.time() - starttime)
    # for i in range(0, 2):
    #     test = Thread(target=func)
    #     test.start()
