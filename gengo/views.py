from flask import redirect
from flask import render_template
from flask import request, Response
from flask import url_for

from gengo.app import app
from gengo.component.lookup import lookup
from gengo.utils import bad_query
from gengo.utils import beautify
from gengo.utils import supported_query

@app.route('/')
def home():
    return "TODO"

@app.route('/api/<lang>/<query>')
def api(lang: str, query: str):
    if not supported_query(lang) or bad_query(query):
        return invalid_query()
    result = beautify(lang, lookup(lang, query))
    return Response(str(result), mimetype='application/json')

def invalid_query():
    return "Invalid query."

