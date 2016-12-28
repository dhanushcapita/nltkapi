from flask import Flask
from flask_restful import Resource, Api
import nltk 

app = Flask(__name__)
api = Api(app)

class NLTK(Resource):
    def get(self, text):
        sentences = nltk.sent_tokenize(text)
        tokens = [nltk.word_tokenize(sentence) for sentence in sentences]
        tags = [nltk.pos_tag(token) for token in tokens]
        chunks = nltk.ne_chunk_sents(tags, binary=True)
        return {'chunks': " ".join(str(chunk) for chunk in chunks)}

api.add_resource(NLTK, '/api/v1.0/nltk/chunks/<string:text>')

if __name__ == '__main__':
    app.run(debug=True)