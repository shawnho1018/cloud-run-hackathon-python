import json
import logging

logger = logging.getLogger(__name__)

with open('test.json', 'r') as f:
  #data = ast.literal_eval(f)
  data = json.load(f)

moves = ['F', 'T', 'L', 'R']



self = 'https://watersplash-ya6rumdz4a-uc.a.run.app'
dimension = data['arena']['dims']
mydir = data['arena']['state'][self].direction
mycor = [data['arena']['state'][self][x], data['arena']['state'][self][y]



# should fire
for user in data['arena']['state']:
    if user != self: 
        print('user: %s, data: %s' % (user, data['arena']['state'][user]))
    

def moveTo(dst_x, dst_y, mydir, my_x, my_y):
    move = 'None'
    if my_y > dst_y:
        if mydir == 'N':
            move = 'T'
        elif mydir == 'E':
            move = 'L'
        elif mydir == 'W':
            move = 'R'
        else:
            move = 'L'
    elif my_y < dst_y:
        if mydir == 'N':
            move = 'L'
        elif mydir == 'E':
            move = 'R'
        elif mydir == 'W':
            move = 'L'
        else:
            move = 'T'        
    else:
        if my_x > dst_x:
            if mydir == 'N':
                move = 'L'
            elif mydir == 'E':
                move = 'L'
            elif mydir == 'W':
                move = 'T'
            elif mydir == 'S':
                move = 'R'
        elif my_x < dst_x:            
            if mydir == 'N':
                move = 'R'
            elif mydir == 'E':
                move = 'T'
            elif mydir == 'W':
                move = 'R'
            elif mydir == 'S':
                move = 'L'
            
    return move


        