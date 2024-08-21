"""
WHY IS THIS APP SECURE?
Escape Function: The escape function from markupsafe is used to sanitize user comments before rendering them, preventing the execution of any embedded JavaScript or HTML.
Safe Rendering: Comments are rendered without the |safe filter, ensuring that any HTML tags are displayed as plain text.
"""



from flask import Flask, request, render_template_string
from markupsafe import escape

app = Flask(__name__)

# HTML template with proper escaping
template = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Secure App</title>
</head>
<body>
    <h1>Post a Comment</h1>
    <form action="/post" method="post">
        <textarea name="comment" placeholder="Enter your comment"></textarea>
        <input type="submit" value="Submit">
    </form>
    <div>
        <h2>Comments:</h2>
        {% for comment in comments %}
            <div>
                {{ comment }}
            </div>
        {% endfor %}
    </div>
</body>
</html>
'''

comments = []

@app.route("/", methods=["GET"])
def index():
    return render_template_string(template, comments=comments)

@app.route("/post", methods=["POST"])
def post():
    comment = request.form.get("comment", "")
    safe_comment = escape(comment)  # Escape user input
    comments.append(safe_comment)
    return index()

if __name__ == "__main__":
    app.run(debug=True)

