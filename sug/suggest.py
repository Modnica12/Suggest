#!/usr/bin/env python3
import json
from flask import Flask
from flask import request
app = Flask(__name__)


MAX_FOUND = 10
SUGGEST_FILE = "ruwords.txt"
SUGGESTER = None
DEBUG = True


class Suggester:
    def __init__(self, filename):
        with open(filename) as f:
            self.words = list(f)

    def get(self, word):
        found = []
        for w in self.words:
            if w.startswith(word):
                found.append(w)
            if len(found) >= MAX_FOUND:
                break
        return found


@app.route('/')
def suggest_handler():
    global SUGGESTER
    if SUGGESTER is None:
        SUGGESTER = Suggester(SUGGEST_FILE)

    w = request.args.get('w')
    found = SUGGESTER.get(w)
    return json.dumps(found), 200, {'Content-Type': 'text/json'}


if __name__ == '__main__':
    app.run(debug=DEBUG)
