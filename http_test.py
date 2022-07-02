from flask import Flask, request

app = Flask(__name__)
# ログイン機能
@app.route("/login", methods=["GET", "POST"])
def login():
    # print(request.method)
    if request.method == "GET":
        return """
        <form action="/login" method="post">
            Password:<input type="text"><br>
            <input type='submit'>
        </from>
        """
    # リクエストメソッドPOSTの時は以下の処理を行う
    if request.method == "POST":
        return "Login in!!"


if __name__ == "__main__":
    app.run(debug=True)
