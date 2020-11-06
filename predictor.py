import json
import math

with open('results.json') as f:
   data = json.load(f)

trump_electoral_votes = 0
biden_electoral_votes = 0
for race in data['data']['races']:
   state_trump_votes = 0
   state_biden_votes = 0
   state_trump_expected = 0
   state_biden_expected = 0
   for county in race['counties']:
      county_votes = county['votes']
      county_returned = county['eevp']
      if county_returned == None:
         county_returned = 100
      county_trump_votes = county['results']['trumpd']
      county_biden_votes = county['results']['bidenj']
      try:
         trump_percentage = county_trump_votes / county_votes
         biden_percentage = county_biden_votes / county_votes
      except:
         trump_percentage = 0
         biden_percentage = 0
      county_trump_expected = (math.floor((((100 - county_returned) / 100.0)
                         * trump_percentage * county_trump_votes))
                         + county_trump_votes)
      county_biden_expected = (math.floor((((100 - county_returned) / 100.0)
                         * biden_percentage * county_biden_votes))
                         + county_biden_votes)

      state_trump_votes += county_trump_votes
      state_biden_votes += county_biden_votes
      state_trump_expected += county_trump_expected
      state_biden_expected += county_biden_expected

   if state_trump_expected > state_biden_expected:
      trump_electoral_votes += race['electoral_votes']
#      print(race['state_name'] + ':\tR +' + str(race['electoral_votes']),end='')
      print('{:<20s} {:<10s}'.format(race['state_name'], 'R +' + str(race['electoral_votes'])),end='')
   else:
      biden_electoral_votes += race['electoral_votes']
#      print(race['state_name'] + ':\tD +' + str(race['electoral_votes']), end='')
      print('{:<20s} {:<10s}'.format(race['state_name'], 'D +' + str(race['electoral_votes'])),end='')
   print(' Gap: ' + str(abs(state_trump_expected - state_biden_expected)))

print('\nTrump electoral votes: ' + str(trump_electoral_votes))
print('Biden electoral votes: ' + str(biden_electoral_votes))
print()
if trump_electoral_votes > biden_electoral_votes:
   print('Trump wins')
else:
   print('Biden wins')
