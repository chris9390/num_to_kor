
#import trans_functions as trf
from trans_functions import *
import re

#예) 82-010-1234-5678
#예) 82-053-1234-5678
pattern_phonenumber_with_NNA = re.compile(r'\d+\s*[-]\s*?\d{2,3}\s*[-]\s*\d{2,4}\s*[-]\s*\d{3,4}')

#예) 010-1234-5678
#예) 02-123-4567
pattern_phonenumber = re.compile(r'\d{2,3}\s*[-]\s*\d{2,4}\s*[-]\s*\d{3,4}')

#예) 서울 12 마 3456
pattern_carnumber = re.compile(r'(([서울|부산|대구|인천|대전|광주|울산|제주|경기|강원|충남|전남|전북|경남|경북|세종]{2})?\s*\d{1,3}\s*[가-힣]{1}\s*\d{4})')

#예) 111111 - 9999999
pattern_register = re.compile(r'\d{6}\s*[-]\s*\d{7}')

#예) 123. 456. 789. 000
pattern_ip = re.compile(r'\d{1,3}\s*[.]\s*\d{1,3}\s*[.]\s*\d{1,3}\s*[.]\s*\d{1,3}')

#예) 오후 8: 25: 05
pattern_time = re.compile(r'(([새벽|아침|오전|오후|저녁]{2})?\s*\d{1,2}\s*[:]\s*\d{2}\s*[:]?\s*\d{0,2})')

#예) $3,400
pattern_currency = re.compile(r'[$＄￦￥]\s*[\d,.]+')

#예) -6.5℃
pattern_temper = re.compile(r'[+-]?[.\d]+\s*[℃℉]')

#예) 3 차례
pattern_order = re.compile(r'\d+\s*[차례|번째|번씩]{2}')

#예) 2018-1-1, 2018-01-01
#예) 2018.1.1, 2018.01.01
#예) 2018/1/1, 2018/01/01
pattern_date = re.compile(r'((19|20)\d{2}\s*[-./]\s*(0?[1-9]|1[012])\s*[-./]\s*(0?[1-9]|[12][0-9]|3[0-1]))')

#예) 5.18 광주민주화운동, 12 12 사태, 6. 25 전쟁
pattern_anniversary = re.compile(r'(([1-9]|1[0-2])\s*[.]?\s*(0?[1-9]|[12][0-9]|3[0-1])\s*[가-힣]*[운동|전쟁|사태|성명|조치|선거|공동|대북|제재]{2})')

#예) 개수가 8,000만건에 달했다.
#pattern_comma = re.compile(r'(\d[,](\d{3}[,]?)*)')

#예) 50 살
pattern_age = re.compile(r'\d+\s*살')

#예) 6시, 11시
pattern_hour_only = re.compile(r'((1[0-2]|[0-9])\s*시)')

#예) 6월, 10월
pattern_month_only = re.compile(r'((1[0-2]|[0-9])\s*월)')

#위의 정해진 패턴 제외 나머지 모든 숫자 패턴.('-130%', '36.5', '10월' 같은 패턴 포함)
pattern_general = re.compile(r'[+-]?\s*\d+[,.]?\d*[%]?')





#fr = open('/home/s20131533/pycharm_numbertoword/100_264_filtered.txt', 'r', encoding='UTF8')
fr = open('100_264_filtered.txt', 'r', encoding='UTF8')
#fr = open('patterned.txt', 'r', encoding='UTF8')
fw = open('result.txt', 'w', encoding='UTF8')


original_list = []          # 원본 text 저장용
text_list = []              # 중간 text 변환 작업용
result_list = []            # 변환된 결과 text 저장용






##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################



total = fr.readlines()

# 입력 파일을 읽어서 text_list 에 추가
count = 0
for i in total:
    if count == 100:
        break

    # 원본
    original_list.append(i)

    # text_list에 입력파일의 모든 text가 리스트 형식으로 들어온다.
    text_list.append(i)

    count = count + 1


index = 0
# text는 리스트 안의 각 문장.
for text in text_list:

    # 패턴화된 결합구조들
    #########################################################
    pn_NNA = pattern_phonenumber_with_NNA.findall(text)     # 국가번호 + 전화번호
    pn = pattern_phonenumber.findall(text)                  # 전화번호
    cn = pattern_carnumber.findall(text)                    # 차량 등록번호
    rn = pattern_register.findall(text)                     # 주민번호
    ip = pattern_ip.findall(text)                           # ip주소
    tn = pattern_time.findall(text)                         # 시간
    cu = pattern_currency.findall(text)                     # 통화
    te = pattern_temper.findall(text)                       # 기온
    da = pattern_date.findall(text)                         # 날짜
    on = pattern_order.findall(text)                        # 차례
    an = pattern_anniversary.findall(text)                  # 기념일
    ag = pattern_age.findall(text)                          # 나이
    hr = pattern_hour_only.findall(text)                    # 시간만
    mo = pattern_month_only.findall(text)                   # 월만
    #########################################################


    general = pattern_general.findall(text)                   # 일반적인 숫자들




    # 패턴화된 결합구조로 일단 걸러낸다.
    if pn_NNA or pn or cn or rn or ip or tn or da or cu or te or on or an or ag or hr or mo:
        if pn_NNA:
            phonenum_trans(pn_NNA, index, text_list)
        if pn:
            phonenum_trans(pn, index, text_list)
        if cn:
            carnum_trans(cn, index, text_list)
        if rn:
            regnum_trans(rn, index, text_list)
        if ip:
            ipnum_trans(ip, index, text_list)
        if tn:
            timenum_trans(tn, index, text_list)
        if da:
            date_trans(da, index, text_list)
        if cu:
            general_trans(cu, index, text_list)
        if te:
            general_trans(te, index, text_list)
        if on:
            order_trans(on, index, text_list)
        if an:
            anniversary_trans(an, index, text_list)
        if ag:
            Kca_b_trans(ag, index, text_list)
        if hr:
            Kca_b_trans(hr, index, text_list)
        if mo:
            month_trans(mo, index, text_list)

    # 걸러지지 않은 나머지 숫자들 매치
    if general:
        general_trans(general, index, text_list)

    else:
        print('No Match')


    index = index + 1


result_list = text_list

for text in result_list:
    #print(text)
    fw.write(text)





# 정답 비교
fr_answer = open('1~100_correct.txt', 'r', encoding='UTF8')
answer_list = fr_answer.readlines()


wrong_count = 0
for i in range(len(answer_list)):
    if answer_list[i] != result_list[i]:
        print('Line ' + str(i+1) + ' : ' + result_list[i])
        wrong_count = wrong_count + 1

print('==================================================================================\n')

print('틀린 개수 : ' + str(wrong_count))
wrong_prob = wrong_count / len(answer_list)
print('오답률 : ' + str(wrong_prob * 100) + '%')







fr.close()
fr_answer.close()
fw.close()





