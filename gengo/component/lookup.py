import json

from gengo.app import app

CMN_SYNONYMS = json.load(open(app.config['DATA_PATH'] + '/cmn/xref.json'))
HAK_SYNONYMS = json.load(open(app.config['DATA_PATH'] + '/hak/xref.json'))
NAN_SYNONYMS = json.load(open(app.config['DATA_PATH'] + '/nan/xref.json'))
CHN = {
    'cmn': 'a',
    'hak': 'h',
    'nan': 't'}
CHN_SYNONYMS = {
    'a': CMN_SYNONYMS,
    'h': HAK_SYNONYMS,
    't': NAN_SYNONYMS}

def lookup(lang: str, query: str):
    result = None
    if lang in CHN:
        result = lookup_chn(lang, query)
    elif lang == 'jpn':
        result = lookup_jpn(query)

    return result

def lookup_chn(lang: str, query: str):
    json_file = open(app.config['DATA_PATH'] + '/{}/{}.json'.format(lang, query), encoding='utf-8')
    return json.load(json_file)

def lookup_jpn(query: str):
    # TODO
    return

def synonyms(lang: str, query: str):
    if lang in CHN:
        return synonyms_chn(lang, query)
        
def synonyms_chn(lang: str, query: str):
    langs = {'cmn', 'hak', 'nan'}
    langs.remove(lang)
    syns = CHN_SYNONYMS[CHN[lang]]

    result = {}
    for l in langs:
        result.update({l: syns[CHN[l]][query]})
    return result

def synonyms_jpn(query: str):
    # TODO
    return

