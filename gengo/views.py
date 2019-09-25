from flask import redirect
from flask import render_template
from flask import request, Response
from flask import url_for

from gengo.app import app
from gengo.component.lookup import lookup
from gengo.component.lookup import synonyms
from gengo.utils import beautify

@app.route('/')
def home():
    return "TODO"

@app.route('/api/<lang>/<query>')
def api(lang: str, query: str):
    result = beautify(lang, lookup(lang, query))
    return Response(str(result), mimetype='text/plain')

@app.route('/api/<lang>/<query>/syn')
def api_syn(lang: str, query: str):
    result = beautify(lang, synonyms(lang, query))
    return Response(str(result), mimetype='text/plain')

