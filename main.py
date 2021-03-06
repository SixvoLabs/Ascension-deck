import json
import sys

# Death rate
def dr(data):
    return float(data['People and Society']['Death rate']['text'].split()[0])
# Birth rate
def br(data):
    return float(data['People and Society']['Birth rate']['text'].split()[0])

if len(sys.argv) != 2:
    print('Ugh.. you didn not specify all the arguments. Check the README.')
    sys.exit(0)

path = sys.argv[1]
#country = sys.argv[2]
with open('factbook.json/' + path) as f:
    data = json.load(f)

    total_pop = int(data['People and Society']['Population']['text'].split()[0].replace(',', ''))
    print('\nThis year in the', data['Government']['Country name']['conventional long form']['text'] + ',\n')
    print('****************\n')
    print( int(br(data) * total_pop/1000), 'descended' )
    print( int(dr(data) * total_pop/1000), 'ascended' )
    print('\n****************\n')
