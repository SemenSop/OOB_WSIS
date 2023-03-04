from flask import (
    Flask,
    render_template as render,
    request, 
    redirect, 
    send_from_directory
)

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render('error.html')


@app.route('/assets/<path:path>', methods=['GET'])
def send_assets(path):
    return send_from_directory('assets', path)


@app.route('/data/<path:path>', methods=['GET'])
def send_data(path):
    return send_from_directory('data', path)


@app.route('/', methods=['GET'])
@app.route('/signin', methods=['GET'])
def signin():
    return render('signin.html')


if __name__ == '__main__':
    app.run(debug=True, port=8050
