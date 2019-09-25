import json

from gengo.app import app

def lookup(lang: str, query: str):
    result = None
    if lang in {'cmn', 'hak', 'nan'}:
        json_file = open(app.config['DATA_PATH'] + '/{}/{}.json'.format(lang, query), encoding='utf-8')
        result = json.load(json_file)
    elif lang == 'jpn':
        # TODO
        return

    return result
