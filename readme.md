
Python Flask based RESTful API ‘hello world’ sample to return natural language word chunks of the given text.
-	Sample is based on nltk library – Natural language toolkit for python
        http://www.nltk.org/
        https://pythonprogramming.net/tokenizing-words-sentences-nltk-tutorial/
-	How to test in dev machine:
        Python nltkapi.py
        Navigate to http://localhost:5000/api/v1.0/nltk/chunks/'My name is George'<your text>
        Output - {"chunks": "(S 'My/POS name/NN is/VBZ (NE George/NNP) '/POS)"}
-	Output is based on https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
