nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
rounds=int

from random import choice

def get_jokes(rounds, nouns, adverbs, adjectives):

    x = 0
    jokes=[]

    while x < rounds:

        jokes.append((choice(nouns)) + ' ' + choice(adverbs) + ' ' +choice(adjectives))
        x += 1

    print(jokes)

get_jokes(5, nouns, adverbs, adjectives)