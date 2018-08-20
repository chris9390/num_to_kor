# -*- coding: utf-8 -*-

from trans_functions import *
import re


# 2~3개
#pattern_wave = re.compile(r'\d+\s*[~]\s*\d+')


#age_possible_list = '(남성|여성|남자|여자|주부|지적장애인|조선족|대학생|재력가|할머니|할아버지|아버지|어머니|아들|딸|' \
#                '일당|중국동포|차량털이범|초반|중반|후반|교수|초등|정신질환자|여대생|용의자|운전자|고령|재력가|' \
#                '내연녀|제자|마약|노인|어르신|가장|마을|주민|미혼|기혼|고교|고등|청소년)'



# ??대 앞뒤로 두 어절
#pattern_age_with_dae = re.compile(r'([1-9]0대\s*' +age_possible_list + r')')
pattern_age_with_dae = re.compile(r'[가-힣A-Z]{0,10}\s*[가-힣A-Z]{0,10}\s*[1-9]0대[가-힣]?\s*[가-힣A-Z]{0,10}\s*[가-힣A-Z]{0,10}')

# 3대 조직, 10대 대기업
#pattern_generation = re.compile(r'([0-9]+?대\s*[가-힣]*(원칙|운영|사업|과제|총장|선거|조직|혁신|그룹|국회|증권사|로펌|주요 로펌|기업|신기술|대기업|슈퍼푸드|건강식품))|((제|국내)\s*[0-9]+대)')
pattern_generation = re.compile(r'[가-힣A-Z]{0,10}\s*[가-힣A-Z]{0,10}\s*[0-9]+대[가-힣]?\s*[가-힣A-Z]{0,10}\s*[가-힣A-Z]{0,10}')


# 1조 3000억
pattern_number_unit = re.compile(r'(\d+(,\d{3})*\s*[조억만])')


# 달러, 원, 엔, 위안
pattern_currency_kor = re.compile(r'(\d+(,\d{3})*\s*((달러|위안)|[원엔]))')

#예) 82-010-1234-5678
#예) 82-053-1234-5678
pattern_phonenumber_with_NNA = re.compile(r'\d+\s*[-]\s*?\d{2,3}\s*[-]\s*\d{2,4}\s*[-]\s*\d{3,4}')

#예) 010-1234-5678
#예) 02-123-4567
pattern_phonenumber = re.compile(r'\d{2,3}\s*[-]\s*\d{2,4}\s*[-]\s*\d{3,4}')

#예) 서울 12 마 3456
pattern_carnumber = re.compile(r'((서울|부산|대구|인천|대전|광주|울산|제주|경기|강원|충남|전남|전북|경남|경북|세종)?\s*\d{1,3}\s*[아바사자허가나다라마거너더러머버서어저고노도로모보소오조구누두루무부수우주]\s*\d{4})')

#예) 111111 - 9999999
pattern_register = re.compile(r'\d{6}\s*[-]\s*\d{7}')

#예) 123. 456. 789. 000
pattern_ip = re.compile(r'\d{1,3}\s*[.]\s*\d{1,3}\s*[.]\s*\d{1,3}\s*[.]\s*\d{1,3}')

#예) 오후 8: 25: 05
pattern_time = re.compile(r'((새벽|아침|오전|오후|저녁)?\s*\d{1,2}\s*[:]\s*\d{2}\s*[:]?\s*\d{0,2})')

#예) $3,400
pattern_currency = re.compile(r'[$＄￦￥]\s*[\d,.]+')

#예) -6.5℃
pattern_temper = re.compile(r'[+-]?[.\d]+\s*[℃℉]')

#예) 3 차례 -> 세 차례
pattern_order = re.compile(r'(\d+\s*(차례|번째|번씩))')

#예) 2018-1-1, 2018-01-01
#예) 2018.1.1, 2018.01.01
#예) 2018/1/1, 2018/01/01
pattern_date = re.compile(r'((19|20)\d{2}\s*[-./]\s*(0?[1-9]|1[012])\s*[-./]\s*(0?[1-9]|[12][0-9]|3[0-1]))')

#예) 5.18 광주민주화운동, 12 12 사태, 6. 25 전쟁
pattern_anniversary = re.compile(r'(([1-9]|1[0-2])\s*[.]?\s*(0?[1-9]|[12][0-9]|3[0-1])\s*[가-힣]*(운동|전쟁|사태|성명|조치|선거|공동|대북|제재|세월호))')


# 한자어 수사 + 분류사
#예) 3 개월 -> 삼 개월, 3 개년 -> 삼 개년
pattern_ancient_with_classifier = re.compile(r'(\d+(,\d{3})*\s*(퍼센트|(개월|개년)|[원년일세월도]))')

# 50미만 고유어 수사, 50이상 한자어 수사 + 분류사
#예) 3 마리 -> 세 마리, 52 마리 -> 오십이 마리
pattern_kor_with_classifier = re.compile(r'(\d+(,\d{3})*\s*((시간|군데|마리|가지|사람|개사)|[명시개살달해곳배대장갑]))')



#위의 정해진 패턴 제외 나머지 모든 숫자 패턴.('-130%', '36.5' 같은 패턴 포함)
pattern_general_with_point = re.compile(r'([+-]?\s*\d+[.]\d+(%p|%|t|㎏|kg|g|km|cm|mm|m)?)', re.IGNORECASE)       # 35.64
pattern_general_with_comma = re.compile(r'([+-]?\s*\d+(,\d{3})+(%p|%|t|㎏|kg|g|km|cm|mm|m)?)', re.IGNORECASE)    # 123,456,789
pattern_general_only_number = re.compile(r'([+-]?\s*\d+(%p|%|t|㎏|kg|g|km|cm|mm|m)?)', re.IGNORECASE)            # 12345






fr = open('filtered/100_264_filtered.txt', 'r', encoding='UTF8')
#fr = open('patterned.txt', 'r', encoding='UTF8')
fw = open('result.txt', 'w', encoding='UTF8')


original_list = []          # 원본 text 저장용
text_list = []              # 중간 text 변환 작업용
result_list = []            # 변환된 결과 text 저장용


def pattern_check(text):

    global ad, ge, nu, ck, pn_NNA, pn, cn, rn, ip, tn, cu, te, da, on, an, ac, kc, general_only_number, general_with_point, general_with_comma

    # 패턴화된 결합구조들
    #########################################################
    ad = pattern_age_with_dae.findall(text) # '대'가 붙은 나이
    ge = pattern_generation.findall(text)           # 세대
    nu = pattern_number_unit.findall(text)  # 숫자 단위
    ck = pattern_currency_kor.findall(text)  # 화폐 한글 단위
    pn_NNA = pattern_phonenumber_with_NNA.findall(text)  # 국가번호 + 전화번호
    pn = pattern_phonenumber.findall(text)  # 전화번호
    cn = pattern_carnumber.findall(text)  # 차량 등록번호
    rn = pattern_register.findall(text)  # 주민번호
    ip = pattern_ip.findall(text)  # ip주소
    tn = pattern_time.findall(text)  # 시간
    cu = pattern_currency.findall(text)  # 통화
    te = pattern_temper.findall(text)  # 기온
    da = pattern_date.findall(text)  # 날짜
    on = pattern_order.findall(text)  # 차례
    an = pattern_anniversary.findall(text)  # 기념일

    ac = pattern_ancient_with_classifier.findall(text)  # 한자어 수사 + 분류사
    kc = pattern_kor_with_classifier.findall(text)  # 고유어 수사 + 분류사
    #########################################################


    general_with_comma = pattern_general_with_comma.findall(text)
    general_with_point = pattern_general_with_point.findall(text)
    general_only_number = pattern_general_only_number.findall(text)


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

    pattern_check(text)
    print(str(index+1))



    # 패턴화된 결합구조로 일단 걸러낸다.
    if ad:
        updated_text = general_trans(ad, index, text_list, 'ad')
        pattern_check(updated_text)

    if ge:
        updated_text = general_trans(ge, index, text_list, 'ge')
        pattern_check(updated_text)
    if an:
        updated_text = anniversary_trans(an, index, text_list)
        pattern_check(updated_text)
    if nu:
        updated_text = number_unit_trans(nu, index, text_list)
        pattern_check(updated_text)
    if ck:
        updated_text = currency_kor_trans(ck, index, text_list)
        pattern_check(updated_text)
    if pn_NNA:
        updated_text = phonenum_trans(pn_NNA, index, text_list)
        pattern_check(updated_text)
    if pn:
        updated_text = phonenum_trans(pn, index, text_list)
        pattern_check(updated_text)
    if cn:
        updated_text = carnum_trans(cn, index, text_list)
        pattern_check(updated_text)
    if rn:
        updated_text = regnum_trans(rn, index, text_list)
        pattern_check(updated_text)
    if ip:
        updated_text = ipnum_trans(ip, index, text_list)
        pattern_check(updated_text)
    if tn:
        updated_text = timenum_trans(tn, index, text_list)
        pattern_check(updated_text)
    if da:
        updated_text = date_trans(da, index, text_list)
        pattern_check(updated_text)
    if cu:
        updated_text = general_trans(cu, index, text_list, None)
        pattern_check(updated_text)
    if te:
        updated_text = general_trans(te, index, text_list, None)
        pattern_check(updated_text)
    if on:
        updated_text = order_trans(on, index, text_list)
        pattern_check(updated_text)


    if ac:
        updated_text = general_trans(ac, index, text_list, None)
        pattern_check(updated_text)
    if kc:
        updated_text = Kca_b_trans(kc, index, text_list)
        pattern_check(updated_text)


    # 걸러지지 않은 나머지 숫자들 매치

    if general_with_comma:
        updated_text = general_trans(general_with_comma, index, text_list, None)
        pattern_check(updated_text)
    if general_with_point:
        updated_text = general_trans(general_with_point, index, text_list, None)
        pattern_check(updated_text)
    if general_only_number:
        updated_text = general_trans(general_only_number, index, text_list, None)
        pattern_check(updated_text)


    '''    
    else:
        print('No Match : ' + text)
    '''


    index = index + 1




result_list = text_list

for text in result_list:
    #print(text)
    fw.write(text)






# 정답 비교
fr_answer = open('correct/1~100_100_correct.txt', 'r', encoding='UTF8')
answer_list = fr_answer.readlines()


wrong_count = 0
for i in range(len(answer_list)):
    if answer_list[i] != result_list[i]:
        print('Line ' + str(i+1) + ' : ' + result_list[i])
        wrong_count = wrong_count + 1

print('==================================================================================\n')

print('전체 : ' + str(len(answer_list)))
print('맞은 개수 : ' + str(len(answer_list) - wrong_count))
print('틀린 개수 : ' + str(wrong_count))
wrong_prob = wrong_count / len(answer_list)
print('\n오답률 : ' + str(wrong_prob * 100) + '%')




fr_answer.close()



fr.close()
fw.close()





