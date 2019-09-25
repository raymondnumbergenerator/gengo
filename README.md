## Gengo

### Overview
言語 means "language." It's pronounced differently in different languages (yányǔ in Mandarin, giân-gí in Min Nan, gengo in Japanese, etc.), but they all share a common root and more notably, a common writing system. Chinese characters are the oldest writing system in the world that is still in widespread active use and its' elegance is seen in all the languages that use it. Gengo is a multilingual dictionary with a focus on languages that have been strongly influenced by Chinese characters.

### Development Setup
1. Fork this repository and clone your fork.
2. Add this repository as the upstream remote.
3. `make venv` will set up the virtual environment.
4. `make init` will bootstrap the dictionary data.
5. `make dev` will run the development copy.

### Sources

#### Mandarin, Min Nan, Hakka
* [language.moe.gov.tw](https://language.moe.gov.tw)

Dictionary data for Mandarin, Min Nan and Hakka languages originally provided by the Ministry of Education of Taiwan. ([CC BY-ND 3.0 TW](https://language.moe.gov.tw/001/Upload/Files/site_content/M0001/respub/index.html))

Data obtained from the [moedict](https://github.com/g0v/moedict-webkit) project, maintained by [g0v.tw](https://g0v.tw). ([CC0 1.0](https://github.com/g0v/moedict-webkit#cc0-10-%E5%85%AC%E7%9C%BE%E9%A0%98%E5%9F%9F%E8%B2%A2%E7%8D%BB%E5%AE%A3%E5%91%8A))

* [cc-cedict.org](https://cc-cedict.org/wiki)

Chinese (Mandarin)-English bilingual dictionary data provided by the CC-CEDICT project. ([CC BY-SA 4.0](https://www.mdbg.net/chinese/dictionary?page=cc-cedict))

Data obtained from the [CC-CEDICT](https://www.mdbg.net/chinese/dictionary?page=cc-cedict) project, maintained by [cc-cedict.org](https://cc-cedict.org/wiki/).

#### Japanese
* [edrdg.org](http://www.edrdg.org)

Dictionary data for Japanese provided by the Electronic Dictionary Research and Development Group. ([CC BY-SA 3.0](https://www.edrdg.org/edrdg/licence.html))

Vocabulary data obtained from the [JMDict](http://www.edrdg.org/jmdict/j_jmdict.html) project, maintained by [EDRDG.org](https://edrdg.org).

Kanji data obtained from the [KANJIDIC](http://www.edrdg.org/wiki/index.php/KANJIDIC_Project) project, maintained by [EDRDG.org](https://edrdg.org).

* [tatoeba.org](https://tatoeba.org)

Japanese corpus data originally provided by the Tanaka Corpus, originally maintained by the EDRDG and currently maintained by the Tatoeba project. ([CC BY 2.0 FR](https://tatoeba.org/eng/downloads))

Data obtained from the [Tatoeba](https://tatoeba.org/eng/downloads) project, maintained by [tatoeba.org](https://tatoeba.org).

* [bunka.go.jp](http://www.bunka.go.jp)

Mapping between Shinjitai to Kyūjitai obtained from [namakajiri.net](https://namakajiri.net/kanjigen/data/shinjitai.txt), which contains data pulled directly from the Jōyō Kanji table provided by the Agency for Cultural Affairs of Japan.

#### Korean
* [kdict.org](http://www.kdict.org)

Dictionary data for Korean provided by the CC-KEDICT project. ([CC BY-SA 3.0](https://github.com/mhagiwara/cc-kedict))

Data obtained from the the [CC-KEDICT](https://github.com/mhagiwara/cc-kedict) project, maintained by [kdict.org](http://www.kdict.org).

* engdic

Hanja and vocabulary data originally provided by the engdic project, compiled by KwangSuk Lee at [kecl.ntt.co.jp/icl/mtg/resources/engdic](http://www.kecl.ntt.co.jp/icl/mtg/resources/engdic/). No longer maintained. (GPL)

Data obtained from the [hanja-dictionary](https://github.com/dbravender/hanja-dictionary) project.
