from flask import Flask

app = Flask(__name__)
app.config.from_envvar('GENGO_SETTINGS')

import gengo.views

if __name__ == '__main__':
    exit(app.run(debug=True))
