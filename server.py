from flask import Flask, redirect, url_for, render_template
from flask import request, json
from flask import jsonify
import config

app = Flask(__name__)


@app.route('/docs')
def documentation():
    return render_template('Doc ServerMedAI API.html')


@app.route("/")
def to_models():
    return redirect(url_for('models_list'))


@app.route('/models', methods=['GET', 'POST'])
def models_list():
    return {'output': config.models_names}


@app.route('/models/<string:name>', methods=['GET', 'POST'])
def search_model(name):
    if name in config.models_names:
        return {'output': name}
    return {'output': "NOT FOUND MODEL"}


@app.route('/models/<string:name>/predict', methods=['POST'])
def model_predict(name):
    if name in config.models_names:
        json_data = request.get_json()
        if len(json_data) != 0:
            output = config.model_predict[name].predict(json_data)
            return jsonify({'output':output})
        return {'output': "NO ARGS"}
    return {'output': "NOT FOUND MODEL"}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
