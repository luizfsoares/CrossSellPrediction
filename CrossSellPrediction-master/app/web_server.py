from flask import Flask, request, render_template
import utils

app = Flask(__name__)


@app.route('/')
def home():
    print('home')
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':

        print('antes')
        data = request.form
        print('depois')

        model_input = utils.preprocess(data)
        result = utils.predict(model_input)

    return render_template('index.html',
                           prediction_text='O preço é {}'.format(result))


if __name__ == '__main__':
    app.run(app.run(host='127.0.0.1', port=5015))
