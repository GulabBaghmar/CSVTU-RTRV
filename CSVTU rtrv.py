from flask import Flask, request, redirect, url_for
import webbrowser

app = Flask(__name__)

# HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Link Editor</title>
</head>
<body>
    <h1>Edit the Link</h1>
    <form method="post">
        <label for="semester">Semester (S):</label>
        <input type="number" id="semester" name="semester" min="1" max="8" required><br><br>
        
        <label for="exam">Exam (E):</label>
        <select id="exam" name="exam" required>
            <option value="Apr-May">Apr-May</option>
            <option value="Nov-Dec">Nov-Dec</option>
        </select><br><br>
        
        <label for="roll_number">Roll Number (R):</label>
        <input type="text" id="roll_number" name="roll_number" required><br><br>
        
        <button type="submit">Open Link</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def edit_link():
    if request.method == "POST":
        semester = request.form.get("semester")
        exam = request.form.get("exam")
        roll_number = request.form.get("roll_number")
        
        # Generate the URL
        link = f"https://csvtu.digivarsity.online/WebApp/Result/SemesterResult.aspx?S={semester}%20SEMESTER&E={exam}%202024&R={roll_number}&T=RTRV"
        
        # Open the link in the default web browser
        webbrowser.open(link)
        return f"<p>The link is being opened in your browser: <a href='{link}' target='_blank'>{link}</a></p>"
    
    return HTML_TEMPLATE

if __name__ == "__main__":
    app.run(debug=True)
