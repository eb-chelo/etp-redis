#!/bin/python

from flask import Flask
from flask import request
import redis
import json
# from flask import Response, stream_with_context

app = Flask(__name__)
app.debug = True
redis_instance = redis.Redis('localhost') # connect to server

DECK = [
    'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK',
    'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK', 'H1', 'H2', 'H3',
    'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6',
    'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK'
]

@app.route('/cards', methods=['GET', 'PUT'])
def deck():
    def _decode(item):
        return item.decode('utf-8')

    if request.method == 'PUT':
        redis_instance.delete('deck')
        redis_instance.sadd('deck', *[card for card in DECK])
        return json.loads({})

    redis_instance.sunionstore('new_game_deck', 'deck')
    cards = redis_instance.spop('new_game_deck', 5)
    cards = map(_decode, cards)
    cards = list(cards)
    return json.dumps(cards)


if __name__ == "__main__":
    app.run()
