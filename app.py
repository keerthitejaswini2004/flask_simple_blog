from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# List to store blog posts
posts = []

# Home page - READ posts
@app.route("/")
def index():
    return render_template("index.html", posts=posts)


# CREATE post
@app.route("/create", methods=["GET", "POST"])
def create():

    if request.method == "POST":

        title = request.form["title"]
        content = request.form["content"]

        post = {
            "title": title,
            "content": content
        }

        posts.append(post)

        return redirect("/")

    return render_template("create.html")


# UPDATE post
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    if request.method == "POST":

        posts[id]["title"] = request.form["title"]
        posts[id]["content"] = request.form["content"]

        return redirect("/")

    post = posts[id]

    return render_template("edit.html", post=post, id=id)


# DELETE post
@app.route("/delete/<int:id>")
def delete(id):

    posts.pop(id)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)