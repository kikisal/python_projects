from random import randrange
import math

siti_raw = []

with open('data.txt', 'r') as f:
    siti_raw = f.readlines()



total_scores = 0
CRITICI = 100

siti = [{'sito': sito.replace('\n', ''), 'score': 0} for sito in siti_raw]

def update_total_scores(score):
    global total_scores

    total_scores += score


def vota():
    index = randrange(0, len(siti))
    sito = siti[index]

    score_random = randrange(1, CRITICI)
    sito['score'] += score_random
    update_total_scores(score_random)


def log():
    global total_scores

    max_score = 0
    last_id = None
    
    print(f'VOTI TOTALI {total_scores}')
    
    for sito in siti:
        frequency = ( sito['score'] / total_scores ) * 100
        frequency = math.floor(frequency)
        
        print(f"il {frequency}% della popolazione ha votato: {sito['sito']}")
        
        # get the winner
        if ( sito['score'] > max_score ):
            max_score = sito['score']
            last_id = sito['sito']

        
    
    print(f'IL SITO VINCITORE È {last_id}')

def main():
    for n in range(CRITICI):
        score = vota()

    print('elezione finita!')
    log()

if __name__ == '__main__':
    main()