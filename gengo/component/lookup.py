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
    result = {}
    if lang in CHN:
        result = lookup_chn(lang, query)
    elif lang == 'chn':
        for l in CHN:
            result[l] = lookup_chn(l, query)
    elif lang == 'jpn':
        result = lookup_jpn(query)
    return result

def lookup_chn(lang: str, query: str):
    try:
        json_file = open(app.config['DATA_PATH'] + '/{}/{}.json'.format(lang, query))
        return json.load(json_file)
    except:
        return {}

def lookup_jpn(query: str):
    # TODO
    return

def synonyms(lang: str, query: str):
    if lang in CHN:
        return synonyms_chn(lang, query)
 
def synonyms_chn(lang: str, query: str):
    langs = {'hak', 'nan'}
    if lang in langs:
        langs = {'cmn'}
    synonyms = CHN_SYNONYMS[CHN[lang]]

    syns = {}
    result = {'t': query, 's': syns}
    for l in langs:
        s = synonyms[CHN[l]].get(query, None)
        if s is None:
            s = []
        else:
            s = s.split(',')
            for i in range(len(s)):
                if s[i] == '':
                    s[i] = query
        syns[l] = s
    return result

def synonyms_jpn(query: str):
    # TODO
    return

