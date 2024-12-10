from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = ""
    if request.method == 'POST':
        name = request.form.get('name')
        if not name:
            name = "Guest"

    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>Hello</title>
            <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
          </head>
          <body>
            <div class="container mt-5">
              {% if name %}
                <h1>Hello, {{ name }}!</h1>
              {% else %}
                <h1>Enter your name below:</h1>
                <form method="post">
                  <div class="form-group">
                    <label for="name">Your Name:</label>
                    <input type="text" class="form-control" id="name" name="name" placeholder="Your name" required>
                  </div>
                  <button type="submit" class="btn btn-primary">Submit</button>
                </form>
              {% endif %}
            </div>
          </body>
        </html>
    ''', name=name)

if __name__ == '__main__':
    app.run(debug=True)