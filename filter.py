import re
pattern_kor = re.compile(r'[^0-9]*')
pattern_대 = re.compile(r'[1-9]0대')

fr = open('/home/public_data/news_corpus/news_norm_2015_103_237.txt', 'r', encoding='UTF8')
fw = open('103_237_filtered.txt', 'w')
#fw = open('대_filtered.txt','w')

total = fr.readlines()

text_list = []


count = 0
for i in total:
    #if count == 30:
    #    break

    text_list.append(i)

    count = count + 1


for text in text_list:
    s = pattern_kor.search(text)
    if s.group() != text:
        #print(text)
        fw.write(text)
    else:
        print('only text')

'''
for text in text_list:
    s = pattern_대.search(text)

    if s:
        fw.write(text)
        #print(text)
'''

fr.close()
fw.close()
