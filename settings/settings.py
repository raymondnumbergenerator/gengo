import os

DATA_PATH = os.environ['DEFAULT_DATA_PATH']

SUPPORTED_LANGUAGES = {
    'cmn', # Chinese Mandarin
    'hak', # Hakka Chinese
    'nan', # Min Nan Chinese (Taiwanese)
    # 'jpn', # Japanese
    # 'kor', # Korean
    }

SUPPORTED_QUERIES = {
    'cmn', # Chinese Mandarin
    'hak', # Hakka Chinese
    'nan', # Min Nan Chinese (Taiwanese)
    'chn', # Mandarin, Hakka, Min Nan
    # 'jpn', # Japanese
    # 'kor', # Korean
    'all', # All languages
    }

MAX_QUERY_LENGTH = 50
