"""
WHY IS THIS APP VULNERABLE TO XSS:
● Template Rendering: The user comments are rendered with {{ comment|safe }}, which allows raw HTML and JavaScript to be injected.
● Potential Attack: An attacker could post a comment like <script>alert('XSS Attack!');</script>, which would execute in the browser.
"""

from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template with a vulnerability
template = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Vulnerable App</title>
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
                {{ comment|safe }}
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
    comments.append(comment)
    return index()

if __name__ == "__main__":
    app.run(debug=True)
