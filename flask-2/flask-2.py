from flask import Flask

app= Flask(__name__)

@app.route('/', methods=["POST","GET"])
def test():
    print("This is v2")
    return "This is v2"

if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)