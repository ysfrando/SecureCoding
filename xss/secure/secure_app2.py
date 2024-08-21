"""
WHY IS THIS APP SECURE:
Bleach Library: We use bleach to sanitize user input. It removes potentially dangerous HTML tags and attributes while allowing safe content.
Sanitized Rendering: The sanitized bio is rendered without the |safe filter, ensuring that any unsafe content is stripped out.
"""

from flask import Flask, request, render_template_string
import bleach

app = Flask(__name__)

# HTML template with proper sanitization
template = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Secure Profile</title>
</head>
<body>
    <h1>User Profile</h1>
    <form action="/update" method="post">
        <textarea name="bio" placeholder="Enter your bio"></textarea>
        <input type="submit" value="Update Bio">
    </form>
    <div>
        <h2>Your Bio:</h2>
        <p>{{ bio }}</p>
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
    raw_bio = request.form.get("bio", "")
    # Sanitize user input to remove harmful HTML
    safe_bio = bleach.clean(raw_bio, tags=[], attributes={}, strip=True)
    bio = safe_bio
    return profile()

if __name__ == "__main__":
    app.run(debug=True)
