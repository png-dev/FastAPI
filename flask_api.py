import flask
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    result = json.dumps({"Hello": 'World'})
    return result


if __name__ == '__main__':
    app.run()
