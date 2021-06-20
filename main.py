#import wolframalpha

#client = wolframalpha.Client('JPY49W-5R97J6XYAX')


# while True:
#query = str(input("Your Question: "))
#res = client.query(query)
#output = next(res.results).text
# print(output)"""

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
        past_ans.insert(0,  ans)
        past_ans.insert(0,  question)
        for i in range(0, len(past_ans)[2]):
            ansFormat = f"{past_ans[i]}|{past_ans[i+1]}"

        return render_template('result.html', answer=ansFormat)
    return jsonify({'error': 'Missing answer'})
    #
    # if answer:
    #  return(jsonify({'answer': answer}))
    # return jsonify({'error': 'Missing answer'})


if __name__ == "__main__":
    app.run(debug=True)
