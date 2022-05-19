import json
import logging

logger = logging.getLogger(__name__)

with open('test.json', 'r') as f:
  #data = ast.literal_eval(f)
  data = json.load(f)

moves = ['F', 'T', 'L', 'R']

self = 'https://watersplash-ya6rumdz4a-uc.a.run.app'
dimension = data['arena']['dims']
mydir = data['arena']['state'][self]['direction']
mycor = [data['arena']['state'][self]['x'], data['arena']['state'][self]['y']]



# should fire
for user in data['arena']['state']:
    if user != self: 
        print('user: %s, data: %s' % (user, data['arena']['state'][user]))