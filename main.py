
# Video test implement flask ajax to display result
from flask import Flask, render_template, request, jsonify
from flask.scaffold import F
import wolframalpha

client = wolframalpha.Client('JPY49W-5R97J6XYAX')
app = Flask(__name__)
global past_ans  # List of the past answers
past_ans = []


@app.route('/')
def index():
    return render_template("test.html")


@app.route('/test', methods=["POST"])  # Happens when the form submits.
def wolframRequest():
    # Gets the question from the input box.
    question = request.form["question"]
    res = client.query(question)  # Queries the api for the answer.
    ans = next(res.results).text  # Gets the answer from the XML.
    # If the answer exists, return the q/a pair, else return error.
    if ans != None:
        past_ans.insert(0,  (question, ans))
        return render_template('result.html')
    return jsonify({'error': 'Missing answer'})


@app.route('/test', methods=["GET"])
def pastAnswersRequest():
    return jsonify(past_ans)


if __name__ == "__main__":
    app.run(debug=True)
