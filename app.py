from flask import Flask, render_template, request
from test import create_epic_with_gpt_description

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    prompt = request.form['prompt']
    epic_name = request.form['epic_name']
    description = create_epic_with_gpt_description(prompt, epic_name)
    return render_template('result.html', epic_name=epic_name, description=description)

if __name__ == '__main__':
    app.run(debug=True)