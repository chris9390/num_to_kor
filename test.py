import re
#pattern_phonenumber = re.compile(r'\d*\s*[-]?\s*?\d{3}\s*[-]\s*\d{3,4}\s*[-]\s*\d{4}')
#pattern_homenumber = re.compile(r'\d*\s*[-]?\s*?\d{2,3}\s*[-]\s*\d{2,4}\s*[-]\s*\d{3,4}')
pattern_phonenumber_with_NNA = re.compile(r'\d+\s*[-]\s*?\d{2,3}\s*[-]\s*\d{2,4}\s*[-]\s*\d{3,4}')
pattern_phonenumber = re.compile(r'\d{2,3}\s*[-]\s*\d{2,4}\s*[-]\s*\d{3,4}')

pattern_carnumber = re.compile(r'(([서울|부산|대구|인천|대전|광주|울산|제주|경기|강원|충남|전남|전북|경남|경북|세종]{2})?\s*\d{1,3}\s*[가-힣]{1}\s*\d{4})')
pattern_register = re.compile(r'\d{6}\s*-\s*\d{7}')
pattern_ip = re.compile(r'\d{1,3}\s*[.]\s*\d{1,3}\s*[.]\s*\d{1,3}\s*[.]\s*\d{1,3}')
pattern_time = re.compile(r'((?P<TST>[새벽|아침|오전|오후|저녁]{2})?\s*\d{1,2}\s*:\s*\d{2}\s*:?\s*\d{0,2})')
pattern_currency = re.compile(r'[$＄￦￥]\s*[\d,.]+')
pattern_temper = re.compile(r'[.\d]+\s*[℃℉]')

pattern_normal = re.compile(r'\d+')


ancient_dict = {'0' : '공', '1' : '일', '2' : '이', '3' : '삼', '4' : '사', '5' : '오', '6' : '육', '7' : '칠', '8' : '팔', '9' : '구'}
kor_dict = {'0' : '공', '1' : '하나', '2' : '둘', '3' : '셋', '4' : '넷', '5' : '다섯', '6' : '여섯', '7' : '일곱', '8' : '여덟', '9' : '아홉'}
Kca_b_dict = {'1' : '한', '2' : '두', '3' : '세', '4' : '네', '5' : '다섯', '6' : '여섯', '7' : '일곱', '8' : '여덟', '9' : '아홉'}
unit_dict = {'1' : '', '2' : '십', '3' : '백', '4' : '천',
             '5' : '', '6' : '십', '7' : '백', '8' : '천',         # 만
             '9' : '', '10' : '십', '11' : '백', '12' : '천',      # 억
             '13' : '', '14' : '십', '15' : '백', '16' : '천'}     # 조


#fr = open('/home/s20131533/pycharm_numbertoword/100_264_filtered.txt', 'r', encoding='UTF8')
fr = open('patterned.txt', 'r', encoding='UTF8')
fw = open('result.txt', 'w')


original_list = []          # 원본 text 저장용
text_list = []              # 중간 text 변환 작업용
result_list = []            # 변환된 text 저장용
translated_str = ''


def phonenum_trans(pn, index):
    # pn_str은 리스트 안의 휴대전화번호 문자열
    for pn_str in pn:

        number_str = ''  # 예) 010-1111-2222
        word_str = ''  # 예) 공일공 일일일일 이이이이

        for char in pn_str:
            if char == '-':
                word_str = word_str + ' '
                number_str = number_str + '-'
            elif char == ' ':
                word_str = word_str + ' '
                number_str = number_str + ' '
            else:
                word_str = word_str + ancient_dict[char]
                number_str = number_str + char

        translated_str = text_list[index].replace(number_str, word_str)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.


def carnum_trans(cn, index):
    for cn_tuple in cn:
        number_str = ''
        word_str = ''

        cn_str = cn_tuple[0]

        for char in cn_str:
            if (ord(char) >= ord('가') and ord(char) <= ord('힣')) or char == ' ':
                word_str = word_str + char
                number_str = number_str + char
            else:
                word_str = word_str + ancient_dict[char]
                number_str = number_str + char

        translated_str = text_list[index].replace(number_str, word_str)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.

def regnum_trans(rn, index):
    for rn_str in rn:
        number_str = ''
        word_str = ''

        for char in rn_str:
            if char == '-':
                word_str = word_str + ' '
                number_str = number_str + '-'
            elif char == ' ':
                word_str = word_str + ' '
                number_str = number_str + ' '
            else:
                word_str = word_str + ancient_dict[char]
                number_str = number_str + char

        translated_str = text_list[index].replace(number_str, word_str)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.

def ipnum_trans(ip, index):
    for ip_str in ip:
        number_str = ''
        word_str = ''

        for char in ip_str:
            if char == '.':
                word_str = word_str + ' '
                number_str = number_str + '.'
            elif char == ' ':
                word_str = word_str + ' '
                number_str = number_str + ' '
            else:
                word_str = word_str + ancient_dict[char]
                number_str = number_str + char

        translated_str = text_list[index].replace(number_str, word_str)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.

def timenum_trans(tn, index):
    for tn_tuple in tn:

        word_str = ''
        flag_10 = 1
        flag_20 = 1
        flag_ancient = 0        # 이 flag가 1이 되면 ancient 방식으로 읽음
        flag_NoSecond = 0
        total_str = tn_tuple[0]
        number_str = total_str          # number_str 을 word_str 으로 바꿀것.

        li = total_str.split(':')
        li_count = len(li)

        if li_count == 2:           # 13:35 / 오후 11:40
            flag_NoSecond = 1

        #if li_count == 2:         # 13:35:22 / 오전 11:40:22
        # li => ['오전 11', '40', '22']
        for part_str in li:

            flag_first = 1
            flag_second = 0

            # part_str => 오전 11 / 40 / 22
            if '00' in part_str:
                li_count = li_count - 1
                continue


            for char in part_str:

                # 시간 파트
                if li_count == 3 or (li_count == 2 and flag_NoSecond == 1):
                    if (ord(char) >= ord('가') and ord(char) <= ord('힣')) or char == ' ':
                        word_str = word_str + char
                    else:

                        if '10' in part_str and flag_10 == 1:
                            word_str = word_str + '열시'
                            flag_10 = 0
                            break

                        elif ('11' or '12') in part_str and flag_10 == 1:
                            word_str = word_str + '열'
                            flag_10 = 0
                            continue

                        elif ('13' or '14' or '15' or '16' or '17' or '18' or '19') in part_str and flag_10 == 1:
                            word_str = word_str + '십'
                            flag_10 = 0
                            flag_ancient = 1
                            continue

                        elif '20' in part_str and flag_20 == 1:
                            word_str = word_str + '이십시'
                            flag_20 = 0
                            break



                        elif ('21' or '22' or '23' or '24') in part_str and flag_20 == 1:
                            word_str = word_str + '이십'
                            flag_20 = 0
                            flag_ancient = 1
                            continue



                        if flag_ancient == 1:
                            word_str = word_str + ancient_dict[char] + '시'
                        else:
                            word_str = word_str + Kca_b_dict[char] + '시'

                # 분/초 파트
                elif li_count == 2 or li_count == 1:
                    if char == ' ':
                        word_str = word_str + char
                    else:
                        if flag_first == 1:
                            flag_first = 0
                            flag_second = 1

                            if char == '0':
                                continue
                            word_str = word_str + ancient_dict[char] + '십'


                        elif flag_second == 1:
                            flag_second = 0

                            if char == '0':
                                if li_count == 2 or (li_count == 1 and flag_NoSecond == 1):
                                    word_str = word_str + '분'
                                elif li_count == 1:
                                    word_str = word_str + '초'
                            else:
                                if li_count == 2 or (li_count == 1 and flag_NoSecond == 1):
                                    word_str = word_str + ancient_dict[char] + '분'
                                elif li_count == 1:
                                    word_str = word_str + ancient_dict[char] + '초'



            li_count = li_count - 1



        translated_str = text_list[index].replace(number_str, word_str)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.


# Cca_b[+U] 로 읽는 경우
def unit_trans(u, index):
    for u_str in u:
        temperature_flag = 0
        currency_flag = 0
        word_str = ''

        if '℃' in u_str:
            temperature_flag = 1
            word_str = word_str + '섭씨 '

        elif  '℉' in u_str:
            temperature_flag = 1
            word_str = word_str + '화씨 '

        elif '$' in u_str or '＄' in u_str:
            cs = '＄'
            currency_flag = 1
        elif '￦' in u_str:
            cs = '￦'
            currency_flag = 1
        elif '￥' in u_str:
            cs = '￥'
            currency_flag = 1


        number_str = u_str
        new_u_str = u_str.replace(',', '')        # new_cu_str 은 ',' 제거한 문자열

        if currency_flag == 1 or temperature_flag == 1:
            unit_len = len(new_u_str) - 1              # -1 하는 이유는 화폐 기호 / 섭씨, 화씨 기호 때문.
        else:
            unit_len = len(new_u_str)

        unit_flag = 0


        # 0 하나만 있는 경우 따로 처리.
        if unit_len == 1 and '0' in new_u_str:
            word_str = word_str + '영'

        # 1 하나만 있는 경우도 따로 처리.
        elif unit_len == 1 and '1' in new_u_str:
            word_str = word_str + '일'

        else:
            for char in new_u_str:
                if char == '$' or char == '＄' or char == '￦' or char == '￥':
                    #cs = char
                    continue
                elif char == '℃' or char == '℉':
                    continue
                elif char == ' ':
                    word_str = word_str + ' '
                else:
                    if char == '0':
                        unit_len = unit_len - 1

                        if unit_len == 4 and unit_flag == 1:
                            word_str = word_str + '만'
                            unit_flag = 0
                        elif unit_len == 8 and unit_flag == 1:
                            word_str = word_str + '억'
                            unit_flag = 0
                        elif unit_len == 12 and unit_flag == 1:
                            word_str = word_str + '조'
                            unit_flag = 0

                        continue

                    if char == '1':
                        if unit_len == 9 or unit_len == 13:             # 억, 조 단위는 1도 말해줘야 한다.
                            word_str = word_str + ancient_dict[char]
                        word_str = word_str + unit_dict[str(unit_len)]  # 그 외에는 1말하지 않음. 예) 100 => 백
                        unit_flag = 1
                    else:
                        word_str = word_str + ancient_dict[char] + unit_dict[str(unit_len)]
                        unit_flag = 1

                    unit_len = unit_len - 1

                    if unit_len == 4:
                        word_str = word_str + '만'
                        unit_flag = 0
                    elif unit_len == 8:
                        word_str = word_str + '억'
                        unit_flag = 0
                    elif unit_len == 12:
                        word_str = word_str + '조'
                        unit_flag = 0

        if currency_flag == 1:
            if cs == '$' or cs == '＄':
                word_str = word_str + ' 달러'
            elif cs == '￦':
                word_str = word_str + ' 원'
            elif cs == '￥':
                word_str = word_str + ' 엔'

        elif temperature_flag == 1:
            word_str = word_str + ' 도'

        translated_str = text_list[index].replace(number_str, word_str)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.



##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################



total = fr.readlines()

# 입력 파일을 읽어서 text_list 에 추가
count = 0
for i in total:
    if count == 22:
        break

    # 원본
    original_list.append(i)

    # text_list에 입력파일의 모든 text가 리스트 형식으로 들어온다.
    text_list.append(i)

    count = count + 1


index = 0
# text는 리스트 안의 각 문장
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
    #########################################################


    # 일반적인 숫자들
    normal = pattern_normal.findall(text)


    if pn_NNA:
        phonenum_trans(pn_NNA, index)
    if pn:
        phonenum_trans(pn, index)
    if cn:
        carnum_trans(cn, index)
    if rn:
        regnum_trans(rn, index)
    if ip:
        ipnum_trans(ip, index)
    if tn:
        timenum_trans(tn, index)
    if cu:
        unit_trans(cu, index)
    if te:
        unit_trans(te, index)
    elif normal:
        unit_trans(normal, index)
    else:
        print('No Match')

    index = index + 1

result_list = text_list




# 결과 출력
for text in original_list:
    print(text)

print('=======================================================')
print('=======================================================\n')

for text in result_list:
    print(text)






fr.close()
fw.close()




