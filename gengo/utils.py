import json
import pprint

CHN = {'cmn', 'hak', 'nan'}

def beautify(lang: str, data) -> str:
    if lang in CHN:
        return json.dumps(data, indent=4, ensure_ascii=False)
    elif lang == 'jpn':
        # TODO
        return
    return

