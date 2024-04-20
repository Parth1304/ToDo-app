from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    return render_template('todo.html')

if __name__ == "__main__":
    app.run(debug=True)
