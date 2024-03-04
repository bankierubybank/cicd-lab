from flask import Flask
from flask import render_template, redirect, url_for, make_response

server = Flask(__name__)

@server.route('/', methods=['GET'])
def base():
    return redirect(url_for('index'))

@server.route('/index')
def index():
	return render_template('index.html')

@server.route('/api/v1')
def api():
    headers = {"Content-Type": "application/json"}
    return make_response(
        'Test worked!',
        200,
        headers=headers
    )

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=8080, debug=True)
