from flask import Flask


my_app = Flask(__name__)


@my_app.route('/')
def about():
    return 'This is about Us page...!'


if __name__=='__main__':
    my_app.run()
