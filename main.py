#import wolframalpha

#client = wolframalpha.Client('JPY49W-5R97J6XYAX')


# while True:
#query = str(input("Your Question: "))
#res = client.query(query)
#output = next(res.results).text
# print(output)"""

# Video test implement flask ajax to display result
from flask import Flask, render_template, request, jsonify
import wolframalpha

client = wolframalpha.Client('JPY49W-5R97J6XYAX')
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("test.html")


@app.route('/test', methods=["POST", "GET"])
def wolframRequest():
    if(request.method == "POST"):
        question = request.form["question"]
        res = client.query(question)
        ans = next(res.results).text
        print(ans)
    else:
        print("The page has been got")
    #
    # if answer:
      #  return(jsonify({'answer': answer}))
    # return jsonify({'error': 'Missing answer'})


if __name__ == "__main__":
    app.run(debug=True)
