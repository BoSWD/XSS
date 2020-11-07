from flask import Flask, render_template, redirect, request

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
    return render_template("view_message.html", message=current_message)


if __name__ == '__main__':
    app.run()
