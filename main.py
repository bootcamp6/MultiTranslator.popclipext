# coding=utf-8
import os
import translate
import btranslate
import time


#使用BaiduTranslate中的scpted方法
def output(result,baiduresult):
    os.environ['result'] = result
    os.environ['baiduresult'] = baiduresult
    os.system('osascript ./translate.scptd \"%s\" \"%s\"' % (result, baiduresult))
    print(result,baiduresult)


LANGUAGES = {
    '簡體中文': 'zh-Hans',
    '繁體中文': 'zh-Hant',
    '英語': 'en'
}

BLANGUAGES = {
    '簡體中文': 'zh',
    '繁體中文': 'cht',
    '英語': 'en'
}

if __name__ == '__main__':
    #獲取設置信息
    mother_lang = os.environ['POPCLIP_OPTION_MOTHERLANG']
    ###mother_lang = '英語'
    dest_lang = os.environ['POPCLIP_OPTION_DESTLANG']
    ###dest_lang = '繁體中文'
    '''#to_clipboard = os.environ['POPCLIP_OPTION_TOCLIPBOARD']
    #location = os.environ['POPCLIP_OPTION_LOCATION']'''
    # 獲取需要翻譯的文本
    text = os.environ['POPCLIP_TEXT']
    
    #初始化微軟翻譯器
    translator = translate.Translator()
    #初次微軟翻譯Microsoft Translator
    result = translator.translate(text=text, to_lang=LANGUAGES[mother_lang])
    #獲取返回的翻譯文本語言的類型
    detected = result[0].get('detectedLanguage').get('language')
    #如果需要翻譯的文本類型和母語類型一致，調轉目標語言和母語再次翻譯
    if LANGUAGES[mother_lang] == detected:
        result = translator.translate(text=text, to_lang=LANGUAGES[dest_lang])
    result=result[0].get('translations')[0].get('text').encode('utf-8')
    
    #初始化百度翻譯器
    btranslator = btranslate.BTranslator()
    #初次百度翻譯Baidu Translator
    bresult = btranslator.btranslate(text=text, bto_lang=BLANGUAGES[mother_lang])
    #獲取返回的翻譯文本語言的類型
    bdetected = bresult['from']
    #如果需要翻譯的文本類型和母語類型一致，調轉目標語言和母語再次翻譯
    if BLANGUAGES[mother_lang] == bdetected:
        #bresult就是類中的r.json()
        time.sleep(1)
        bresult = btranslator.btranslate(text=text, bto_lang=BLANGUAGES[dest_lang])
    res2 = []
    if 'trans_result' in bresult:
        for _res2 in bresult['trans_result']:
            res2.append(_res2['dst'])
        res2 = "\n\n".join(res2)
        baiduresult = res2.encode("utf-8")
    #輸出結果
    output(result, baiduresult)
