import json
import pprint

def beautify(lang, data):
    if lang in {'cmn', 'hak', 'nan'}:
        return json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
    elif lang == 'jpn':
        # TODO
        return
    return

