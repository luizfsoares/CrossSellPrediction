from flask import Flask, request, render_template
import utils

app = Flask(__name__)


@app.route('/')
def home():
    print('home')
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    print('antes')
    data = request.form
    print('depois')

    model_input = utils.preprocess(data)
    result = utils.predict(model_input)

    return render_template('index.html',
                           prediction_text='O preço é {}'.format(result))

@app.route('/sobre')
def sobre():

    return render_template('sobre.html')

@app.route('/contato')
def contato():

    return render_template('contato.html')

@app.route('/index1')
def home2():

    return render_template('index.html')


if __name__ == '__main__':
    app.run(threaded=True, host="0.0.0.0", port=8080)
