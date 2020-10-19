from flask import Flask, render_template, redirect, request, jsonify, make_response

app = Flask(__name__)

current_message = ""


@app.route('/', methods=["GET", "POST"])
def save_message():
    global current_message
    if request.method == "GET":
        return render_template("send_message.html")
    else:
        current_message = request.form.get("message")
        return redirect('xss')


@app.route('/xss')
def view_message():
    return render_template("view_message.html")


@app.route('/message')
def get_message():
    response = make_response(str(current_message), 200)
    response.mimetype = "text/plain"
    return response


app.run(debug=True)
