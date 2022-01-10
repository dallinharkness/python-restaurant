"""Restaurant rating lister."""


# put your code here
def ratings():
    scores_txt = open('scores.txt')

    scores = {}#creating an empty dictionary for things to get added into it.

    for line in scores_txt:
        line = line.rstrip()
        restaurant, score = line.split(':')
        scores[restaurant] = int(score)

    return scores

def addrestaurant(scores):

    print('Add a rating to your favorite restaurant!')
    restaurant = input('Restaurant name...')
    rating = int(input('Rating...'))

    scores[restaurant] = rating

def sortedlist(scores):

    for restaurant, rating in sorted(scores.items()):
        print(f'{restaurant} has a {rating} star rating!')


scores = ratings()

addrestaurant(scores)

sortedlist(scores)