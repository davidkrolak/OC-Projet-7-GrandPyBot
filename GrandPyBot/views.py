from flask import Flask

app = Flask(__name__)

app.config.from_object('config')


@app.route('/')
def main():
    pass


if __name__ == "__main__":
    app.run()
