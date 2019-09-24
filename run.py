from gengo.app import app

import gengo.views

if __name__ == '__main__':
    exit(app.run(host='0.0.0.0', port=8513, debug=True))
