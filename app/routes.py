from flask import render_template
from app import app


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/about')
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/search', methods=['POST'])
def search():
    pass

if __name__ == "__main__":
    app.run()
