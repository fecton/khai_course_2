import wikipediaapi
import requests

output = open('output.txt', 'w', encoding='utf-8')

def get_paragraph(text: str) -> str:
    end_pos = 1
    while text[end_pos] != '\n': end_pos += 1
    return text[:end_pos]

ua_words = open('words.txt', encoding='utf-8').read().split('\n')
ru_words = open('rus.txt', encoding='utf-8').read().split('\n')

ru = wikipediaapi.Wikipedia('ru')
ukr = wikipediaapi.Wikipedia('ukr')

for i in range(len(ua_words)):
    page = ukr.page(ua_words[i])
    try:
        t = page.exists()
    except requests.exceptions.ConnectionError:
        t = False

    if t:
        print(page)
    else:
        page = ru.page(ru_words[i])
        try:
            t = page.exists()
        except requests.exceptions.ConnectionError:
            t = False
        if t:
            print(page)
        else:
            print('[SKIPPED]: %s' % ua_words[i])
            output.write('[SKIPPED]: %s\n' % ua_words[i])
            continue


    txt = page.text
    txt = get_paragraph(txt)
    # print(txt)
    output.write(txt + '\n')


output.close()