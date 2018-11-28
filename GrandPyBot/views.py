from flask import Flask, render_template

app = Flask(__name__)

app.config.from_object('config')


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/about')
@app.route('/about/')
def about():
    pass


if __name__ == "__main__":
    app.run()
