import json
import re

CHN = {'cmn', 'hak', 'nan'}

def beautify(lang: str, data) -> str:
    if lang in CHN:
        return remove_delimiters(json.dumps(data, indent=4, ensure_ascii=False))
    elif lang == 'jpn':
        # TODO
        return
    return

def remove_delimiters(s: str):
    return re.sub('`|~', '', s)
