import json
import re

from gengo.app import app

CHN = {'cmn', 'hak', 'nan', 'chn'}

def beautify(lang: str, data) -> str:
    if lang in CHN:
        return remove_delimiters(json.dumps(data, indent=4, ensure_ascii=False))
    elif lang == 'jpn':
        # TODO
        return
    return

def bad_query(query: str) -> bool:
    if len(query) > app.config['MAX_QUERY_LENGTH']:
        return True
    r = re.search('\/|\.|\s|"|\'', query)
    return bool(r)

def remove_delimiters(s: str) -> str:
    return re.sub('`|~', '', s)

def supported_language(lang: str) -> bool:
    return lang in app.config['SUPPORTED_LANGUAGES']

def supported_query(lang: str) -> bool:
    return lang in app.config['SUPPORTED_QUERIES']

