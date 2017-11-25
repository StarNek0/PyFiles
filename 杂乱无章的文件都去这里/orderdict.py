from time import time
from random import randint
from collections import OrderedDict

score_list = OrderedDict()
players = list('ABCDEFGH')
start_time = time()

for i in xrange(8):
    raw_input()
    player = players.pop(randint(0, 7 - i))
    end_time = time()
    print i+1, player, end_time - start_time,
    score_list[player] = (i+1, end_time - start_time)

print 
print '-'*20
print score_list
print '-'*20
for k in score_list:
    print k, score_list[k]

