"""
WHY IS THIS APP VULNERABLE:
Template Rendering: The user bio is rendered with {{ bio|safe }}, which allows raw HTML and JavaScript to be injected.
Potential Attack: An attacker could set a bio like <script>alert('XSS Attack!');</script>, which would execute in the browser.
"""

from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template with a vulnerability
template = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Vulnerable Profile</title>
</head>
<body>
    <h1>User Profile</h1>
    <form action="/update" method="post">
        <textarea name="bio" placeholder="Enter your bio"></textarea>
        <input type="submit" value="Update Bio">
    </form>
    <div>
        <h2>Your Bio:</h2>
        <p>{{ bio|safe }}</p>
    </div>
</body>
</html>
'''

bio = ""

@app.route("/", methods=["GET"])
def profile():
    return render_template_string(template, bio=bio)

@app.route("/update", methods=["POST"])
def update():
    global bio
    bio = request.form.get("bio", "")
    return profile()

if __name__ == "__main__":
    app.run(debug=True)
