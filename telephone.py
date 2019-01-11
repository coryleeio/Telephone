import sys
import requests
from googletrans import Translator

if __name__ == '__main__':
    translator = Translator()
    language_codes = 'en' ,'bs' ,'cy' ,'ga' ,'ny' ,'la' ,'am' ,'tr' ,'ml' ,'hy' ,'zh-CN' ,'lv' ,'en'
    inp = ' '.join(sys.argv[1:])
    for i in range(0, len(language_codes)-1):
        inp = translator.translate(inp, src=language_codes[i], dest=language_codes[i+1]).text
        # print(inp.encode('utf-8')) #debug
    print(str.format("\n{}",inp))

