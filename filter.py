import re
pattern_kor = re.compile('[^0-9]*')

fr = open('/home/public_data/news_corpus/news_norm_2015_101_771.txt', 'r', encoding='UTF8')
fw = open('101_771_filtered.txt', 'w')

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



fr.close()
fw.close()