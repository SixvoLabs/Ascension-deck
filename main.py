import json
import sys

# Death rate
def dr(data):
    return float(data['People and Society']['Death rate']['text'].split()[0])
# Birth rate
def br(data):
    return float(data['People and Society']['Birth rate']['text'].split()[0])

if len(sys.argv) != 3:
    print('Ugh.. you didn not specify all the arguments. Check the README.')
    sys.exit(0)

path = sys.argv[1]
country = sys.argv[2]
with open('factbook.json/' + path) as f:
    data = json.load(f)
    #print(data['People and Society']['Death rate'])
    print('\nThis year in', country + ',\n')
    print('****************\n')
    print( int(br(data)) * 309, 'descended' )
    print( int(dr(data)) * 309, 'ascended' )
    print('\n****************\n')
