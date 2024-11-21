from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    welcome_messages = {
        'english': 'Welcome',
        'korean': '환영합니다'
    }
    return render_template('index.html', messages=welcome_messages)

if __name__ == '__main__':
    app.run(debug=True)
