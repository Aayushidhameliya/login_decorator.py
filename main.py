from flask import Flask

app = Flask(__name__)

def logging_decorator(fn):
    def wrapper(*args):
        print(f"You called {fn.__name__} {args}")
        result = fn(*args)
        print(f"It returned: {result}")
        return result
    return wrapper

@app.route('/')
def index():
    return "This is the index page."

@app.route('/calculate/<int:a>/<int:b>/<int:c>')
@logging_decorator
def calculate(a, b, c):
    return str(a * b * c)

if __name__ == "__main__":
    app.run(debug=True)
