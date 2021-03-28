from flask import *
import random


app = Flask(__name__)


@app.route('/', methods=["Get", "Post"])
def home():
    if request.method == 'POST':
        friendship_percent = random.randint(1, 101)
        friendship_percent = str(friendship_percent)
        return render_template('home.html', friendship=(friendship_percent+"%"))
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
