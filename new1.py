import flask
import pickle
import numpy as np
import pandas as pd
# Use pickle to load in the pre-trained model.
with open('datascore.pkl', 'rb') as f:
    model = pickle.load(f)
app = flask.Flask(__name__, template_folder='templates')
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('employee.html'))
    if flask.request.method == 'POST':
        hours = flask.request.form['experience']
        input_variables = pd.DataFrame([[hours]],
                                       columns=['Hours'],
                                       dtype=float)
        prediction = model.predict(input_variables)[0]
        return flask.render_template('employee.html',
                                     original_input={'Hours studied':hours},
                                     result=round(prediction,2),
                                     )
if __name__ == '__main__':
    app.run(debug=True)