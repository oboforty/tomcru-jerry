from flask import Flask, jsonify

from tomcru_jerry import flask_jerry_setup, print_endpoints
from tomcru_jerry.controllers import add_controllers
from tomcru_jerry.mockapi import MockedController

app = Flask(__name__)
flask_jerry_setup(app)


@app.route('/dynamic', methods=['GET'])
def dynamic_ep():
    return jsonify({
        "resp": "dynamic endpoint!",
    })


add_controllers(app, {
    'Mocked': MockedController(app, {
        'POST /oauth/me': {
            "headers": {
                "fos": "foscsi"
            },
            "body": {
                # 'tkn': "My Token is {access_token}",
                # "keke": "{headers.Authorization}_tesomsz {body.fsaz}",
                "fsaz": "{body.fsaz}"
            }
        },
        '/hello': {
            "body": {
                'hello': "hello hello"
            }
        }
    })
})


if __name__ == "__main__":
    print_endpoints(app)
    app.run('0.0.0.0', 5000, debug=True)
