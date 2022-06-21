from flask import Flask, request, jsonify
from .huggingface import HuggingFace

import logging

app = Flask(__name__)
hf = HuggingFace('nlptown/bert-base-multilingual-uncased-sentiment')

@app.route('/')
def index():
    logging.info('Start process request')
    sentence = request.args.get('sentence')

    if sentence:
        out = hf.analyze(sentence)
        return jsonify(out)
    else:
        return jsonify({
            "error": "Pass a sentence as query parameter for a personalized response."
        })

@app.route('/health')
def health():
    return jsonify('{"status": "ok"}')