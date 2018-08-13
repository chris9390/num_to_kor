
# 한자어
ancient_dict = {'0' : '공', '1' : '일', '2' : '이', '3' : '삼', '4' : '사', '5' : '오', '6' : '육', '7' : '칠', '8' : '팔', '9' : '구'}
# 명사 고유어
Kca_n_dict = {'0' : '공', '1' : '하나', '2' : '둘', '3' : '셋', '4' : '넷', '5' : '다섯', '6' : '여섯', '7' : '일곱', '8' : '여덟', '9' : '아홉'}
# 관형어 고유어
Kca_b_dict = {'1' : '한', '2' : '두', '3' : '세', '4' : '네', '5' : '다섯', '6' : '여섯', '7' : '일곱', '8' : '여덟', '9' : '아홉'}
# 관형어 고유어 10의 자리
Kca_b_10_dict = {'1' : '열', '2' : '스물', '3' : '서른', '4' : '마흔', '5' : '쉰', '6' : '예순', '7' : '일흔', '8' : '여든', '9' : '아흔'}
# 수의 단위
unit_dict = {'0' : '',
             '1' : '', '2' : '십', '3' : '백', '4' : '천',
             '5' : '', '6' : '십', '7' : '백', '8' : '천',         # 만
             '9' : '', '10' : '십', '11' : '백', '12' : '천',      # 억
             '13' : '', '14' : '십', '15' : '백', '16' : '천'}     # 조
# 특수문자
mark_dict = {'℃' : '섭씨', '℉' : '화씨', '$' : '달러', '＄' : '달러', '￦' : '원', '￥' : '엔',
             '%' : '퍼센트', '%p' : '퍼센트 포인트', '%P' : '퍼센트 포인트',
             '+' : '플러스', '-' : '마이너스', '±' : '플러스 마이너스'}





translated_str = ''

def number_unit_trans(nu, index, text_list):
    for nu_str in nu:
        number_str = nu_str
        word_str = ''

        space_len = nu_str.count(' ')
        comma_len = nu_str.count(',')
        kor_len = 1                     # '조', '억', '만'

        num_len = len(nu_str) - space_len - comma_len - kor_len         # 자리수 예) 6,000 억 => num_len = 4

        word_str = Cca_b_U_trans(nu_str, word_str, num_len)





        translated_str = text_list[index].replace(number_str, word_str, 1)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.


def currency_kor_trans(ck, index, text_list):

    for i in ck:

        if type(i) == tuple:
            ck_str = i[0]
        elif type(i) == str:
            ck_str = i


        number_str = ck_str
        word_str = ''

        space_len = ck_str.count(' ')
        comma_len = ck_str.count(',')

        if '달러' in ck_str or '위안' in ck_str:
            kor_len = 2
        elif '원' in ck_str or '엔' in ck_str:
            kor_len = 1

        num_len = len(ck_str) - space_len - comma_len - kor_len         # 자리수 예) 6,000 달러 => num_len = 4

        word_str = Cca_b_U_trans(ck_str, word_str, num_len)




        translated_str = text_list[index].replace(number_str, word_str, 1)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.





def phonenum_trans(pn, index, text_list):
    # pn_str은 리스트 안의 휴대전화번호 문자열
    for pn_str in pn:

        number_str = pn_str  # 예) 010-1111-2222
        word_str = ''  # 예) 공일공 일일일일 이이이이

        for char in pn_str:
            if char == '-' or char == ' ':
                word_str = word_str + ' '
            else:
                word_str = word_str + ancient_dict[char]


        translated_str = text_list[index].replace(number_str, word_str, 1)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.


def carnum_trans(cn, index, text_list):
    for cn_tuple in cn:

        cn_str = cn_tuple[0]

        number_str = cn_str
        word_str = ''

        for char in cn_str:
            if (ord(char) >= ord('가') and ord(char) <= ord('힣')) or char == ' ':
                word_str = word_str + char
            else:
                word_str = word_str + ancient_dict[char]


        translated_str = text_list[index].replace(number_str, word_str, 1)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.

def regnum_trans(rn, index, text_list):
    for rn_str in rn:
        number_str = rn_str
        word_str = ''

        for char in rn_str:
            if char == '-' or char == ' ':
                word_str = word_str + ' '
            else:
                word_str = word_str + ancient_dict[char]


        translated_str = text_list[index].replace(number_str, word_str, 1)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.

def ipnum_trans(ip, index, text_list):
    for ip_str in ip:
        number_str = ip_str
        word_str = ''

        for char in ip_str:
            if char == '.' or char == ' ':
                word_str = word_str + ' '
            else:
                word_str = word_str + ancient_dict[char]


        translated_str = text_list[index].replace(number_str, word_str, 1)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.

def timenum_trans(tn, index, text_list):
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
                            word_str = word_str + '열시 '
                            flag_10 = 0
                            break

                        elif ('11' in part_str or  '12' in part_str) and flag_10 == 1:
                            word_str = word_str + '열'
                            flag_10 = 0
                            continue

                        elif ('13' in part_str or '14' in part_str or '15' in part_str or
                              '16' in part_str or '17' in part_str or '18' in part_str or '19' in part_str) and flag_10 == 1:
                            word_str = word_str + '십'
                            flag_10 = 0
                            flag_ancient = 1
                            continue

                        elif '20' in part_str and flag_20 == 1:
                            word_str = word_str + '이십시 '
                            flag_20 = 0
                            break



                        elif ('21' in part_str or '22' in part_str or '23' in part_str or '24' in part_str) and flag_20 == 1:
                            word_str = word_str + '이십'
                            flag_20 = 0
                            flag_ancient = 1
                            continue



                        if flag_ancient == 1:
                            word_str = word_str + ancient_dict[char] + '시 '
                        else:
                            word_str = word_str + Kca_b_dict[char] + '시 '

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
                                    word_str = word_str + '분 '
                                elif li_count == 1:
                                    word_str = word_str + '초 '
                            else:
                                if li_count == 2 or (li_count == 1 and flag_NoSecond == 1):
                                    word_str = word_str + ancient_dict[char] + '분 '
                                elif li_count == 1:
                                    word_str = word_str + ancient_dict[char] + '초 '



            li_count = li_count - 1

        translated_str = text_list[index].replace(number_str, word_str, 1)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.



def order_trans(on, index, text_list):

    for i in on:

        if type(i) == tuple:
            on_str = i[0]
        elif type(i) == str:
            on_str = i

        number_str = on_str
        word_str = ''
        unit_flag = 0

        space_count = on_str.count(' ')

        num_len = len(on_str) - 2           # -2 하는 이유는 '번째' or '차례' 길이 만큼 빼줘야 하기 때문
        num_len = num_len - space_count       # 공백 개수 만큼 빼주기

        len_checker = num_len

        for char in on_str:
            if (ord(char) >= ord('가') and ord(char) <= ord('힣')) or char == ' ':
                word_str = word_str + char

            else:
                # 자리수가 2일때 부터 Kca 로 바꿔준다. 2보다 클땐 Cca_b[+U]로 읽는다.
                # Kca_b
                if len_checker == 2:
                    word_str = word_str + Kca_b_10_dict[char]
                elif len_checker == 1:
                    word_str = word_str + Kca_b_dict[char]

                # Cca_b[+U]
                else:
                    if char == '0':

                        if len_checker == 5 and unit_flag == 1:
                            word_str = word_str + '만'
                            unit_flag = 0
                        elif len_checker == 9 and unit_flag == 1:
                            word_str = word_str + '억'
                            unit_flag = 0
                        elif len_checker == 13 and unit_flag == 1:
                            word_str = word_str + '조'
                            unit_flag = 0

                        len_checker = len_checker - 1

                        continue

                    elif char == '1':
                        # 일, 만, 억, 조 단위는 1도 '일'이라고 말해줘야 한다.
                        if len_checker == 1 or len_checker == 5 or len_checker == 9 or len_checker == 13:

                            if len_checker == 5 and num_len == len_checker:     # 5자리 숫자에서 만의 자리가 1이면 '일' 붙이면 안된다.
                                print('')                                       # 아무 작업도 안함
                            else:
                                word_str = word_str + '일'

                        word_str = word_str + unit_dict[str(len_checker)]       # 그 외에는 1말하지 않음. 예) 100 => 백
                        unit_flag = 1
                    else:
                        word_str = word_str + ancient_dict[char] + unit_dict[str(len_checker)]
                        unit_flag = 1



                    if len_checker == 5:
                        word_str = word_str + '만'
                        unit_flag = 0
                    elif len_checker == 9:
                        word_str = word_str + '억'
                        unit_flag = 0
                    elif len_checker == 13:
                        word_str = word_str + '조'
                        unit_flag = 0


            len_checker = len_checker - 1


        translated_str = text_list[index].replace(number_str, word_str, 1)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.



def date_trans(da, index, text_list):

    for i in da:

        if type(i) == tuple:
            da_str = i[0]
        elif type(i) == str:
            da_str = i


        number_str = da_str
        word_str = ''

        date_count = 3

        # 2018-1-1
        if '-' in da_str:
            da_list = da_str.split('-')

        # 2018.1.1
        elif '.' in da_str:
            da_list = da_str.split('.')

        # 2018/1/1
        elif '/' in da_str:
            da_list = da_str.split('/')


        for part_str in da_list:
            part_str = part_str.strip()         # 양옆 공백 제거
            part_len = len(part_str)
            word_str = Cca_b_U_trans(part_str, word_str, part_len)

            if date_count == 3:
                word_str = word_str + '년 '
            elif date_count == 2:
                word_str = word_str + '월 '
            elif date_count == 1:
                word_str = word_str + '일 '

            date_count = date_count - 1

        translated_str = text_list[index].replace(number_str, word_str, 1)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.


def anniversary_trans(an, index, text_list):
    for i in an:

        if type(i) == tuple:
            an_str = i[0]
        elif type(i) == str:
            an_str = i

        number_str = an_str
        word_str = ''

        for char in an_str:
            if (ord(char) >= ord('가') and ord(char) <= ord('힣')) or char == ' ':
                word_str = word_str + char
            elif char == '.':
                continue
            else:
                word_str = word_str + ancient_dict[char]


        translated_str = text_list[index].replace(number_str, word_str, 1)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.





# 관형어 고유어 변환
# 50미만은 고유어 수사
# 50이상은 Cca_b_U_trans함수 호출해서 한자어 수사 처리..
# 3 마리 -> 세 마리, 50 마리-> 오십 마리
def Kca_b_trans(kca, index, text_list):
    for i in kca:

        if type(i) == tuple:
            kca_str = i[0]
        elif type(i) == str:
            kca_str = i


        number_str = kca_str
        word_str = ''
        kor_len = 0
        unit_flag = 0
        Cca_should_work = 0

        space_count = kca_str.count(' ')            # 공백 개수
        comma_count = kca_str.count(',')            # ',' 개수
        #kca_str = kca_str.replace(',', '')          # 숫자 3자리 마다 있는 ',' 제거



        if '시간' in kca_str or '군데' in kca_str or '마리' in kca_str or '가지' in kca_str or '사람' in kca_str or '개사' in kca_str:
            kor_len = 2

        elif '명' in kca_str or '시' in kca_str or '개' in kca_str or '살' in kca_str or '달' in kca_str or '해' in kca_str\
                or '곳' in kca_str or '배' in kca_str:
            kor_len = 1                                            # 2'살' or 10'시' 1글자


        num_len = len(kca_str) - space_count - comma_count - kor_len         # 숫자만의 길이. 공백, 콤마 개수 빼준다.
        len_checker = num_len


        # 여기서 숫자 부분의 크기를 측정해서 50이상은 Cca함수 호출 / 50미만은 이 밑의 과정
        if (num_len == 2 and int(kca_str[0]) >= 5) or num_len >= 3:
            Cca_should_work = 1



        # 숫자가 50이상인 경우
        if Cca_should_work == 1:
            word_str = Cca_b_U_trans(kca_str, word_str, num_len)

        # 숫자가 50미만인 경우
        else:
            for char in kca_str:
                if (ord(char) >= ord('가') and ord(char) <= ord('힣')) or char == ' ':
                    word_str = word_str + char

                elif char == ',':
                    continue

                # 0시 같은 경우
                elif char == '0' and num_len == 1:
                    word_str = word_str +'영'

                elif char == '0' and num_len != 1:
                    continue

                else:
                    # 자리수가 2일때 부터 Kca 로 바꿔준다. 2보다 클땐 Cca_b[+U]로 읽는다.
                    # Kca_b
                    if len_checker == 2:
                        word_str = word_str + Kca_b_10_dict[char]
                    elif len_checker == 1:
                        word_str = word_str + Kca_b_dict[char]

                    # Cca_b[+U]
                    else:
                        if char == '0':

                            if len_checker == 5 and unit_flag == 1:
                                word_str = word_str + '만'
                                unit_flag = 0
                            elif len_checker == 9 and unit_flag == 1:
                                word_str = word_str + '억'
                                unit_flag = 0
                            elif len_checker == 13 and unit_flag == 1:
                                word_str = word_str + '조'
                                unit_flag = 0

                            len_checker = len_checker - 1

                            continue

                        elif char == '1':
                            # 일, 만, 억, 조 단위는 1도 '일'이라고 말해줘야 한다.
                            if len_checker == 1 or len_checker == 5 or len_checker == 9 or len_checker == 13:

                                if len_checker == 5 and num_len == len_checker:  # 5자리 숫자에서 만의 자리가 1이면 '일' 붙이면 안된다.
                                    print('')  # 아무 작업도 안함
                                else:
                                    word_str = word_str + '일'

                            word_str = word_str + unit_dict[str(len_checker)]  # 그 외에는 1말하지 않음. 예) 100 => 백
                            unit_flag = 1
                        else:
                            word_str = word_str + ancient_dict[char] + unit_dict[str(len_checker)]
                            unit_flag = 1

                        if len_checker == 5:
                            word_str = word_str + '만'
                            unit_flag = 0
                        elif len_checker == 9:
                            word_str = word_str + '억'
                            unit_flag = 0
                        elif len_checker == 13:
                            word_str = word_str + '조'
                            unit_flag = 0

                len_checker = len_checker - 1


        translated_str = text_list[index].replace(number_str, word_str, 1)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.







# Cca_b[+U] 로 읽는 경우
# 315 => 삼백십오  이런식으로 변환해준다.
def Cca_b_U_trans(input_str, output_str, length):

    new_u_str = input_str
    word_str = output_str
    original_len = length
    unit_len = length           # 단위 제외 숫자만의 길이 ('12 개월' => unit_len = 2)
    unit_flag = 0
    no_more = 0


    for char in new_u_str:
        if '10' in new_u_str and '월' in new_u_str and no_more == 0:
            word_str = word_str + '시'
            no_more = 1

        elif '6' in new_u_str and '월' in new_u_str and no_more == 0:
            word_str = word_str + '유'
            no_more = 1

        elif char == ',':
            continue

        elif (char == '$' or char == '＄' or char == '￦' or char == '￥') or (char == '℃' or char == '℉'):
            continue

        elif (ord(char) >= ord('가') and ord(char) <= ord('힣')) or char == ' ':
            word_str = word_str + char

        elif char == '%' or char == '%p' or char == '%P':
            word_str = word_str + ' ' + mark_dict[char]

        elif char == '-' or char == '+' or char == '±':
            word_str = word_str + ' ' + mark_dict[char] + ' '

        else:

            # 숫자가 0인 경우
            if char == '0':
                if original_len == 1:
                    word_str = word_str + '영'

                elif unit_len == 5 and unit_flag == 1:
                    word_str = word_str + '만'
                    unit_flag = 0

                elif unit_len == 9 and unit_flag == 1:
                    word_str = word_str + '억'
                    unit_flag = 0

                elif unit_len == 13 and unit_flag == 1:
                    word_str = word_str + '조'
                    unit_flag = 0

                unit_len = unit_len - 1

                continue

            # 숫자가 1인 경우 '일'을 말해주는 경우와 생략하는 경우로 나뉜다.
            elif char == '1':
                if unit_len == 1 or unit_len == 5 or unit_len == 9 or unit_len == 13:  # 일, 만, 억, 조 단위는 1도 '일'이라고 말해줘야 한다.

                    if unit_len == 5 and original_len == unit_len:      # 5자리 숫자에서 만의 자리가 1이면 '일' 붙이면 안된다.
                        print('')                                       # 아무 작업도 안함
                    else:
                        word_str = word_str + '일'

                word_str = word_str + unit_dict[str(unit_len)]  # 그 외에는 1말하지 않음. 예) 100 => 백
                unit_flag = 1

            # 0 과 1 이 아닌 숫자
            else:
                word_str = word_str + ancient_dict[char] + unit_dict[str(unit_len)]
                unit_flag = 1


            # 단위 붙여주는 부분
            if unit_len == 5:
                word_str = word_str + '만'
                unit_flag = 0

            elif unit_len == 9:
                word_str = word_str + '억'
                unit_flag = 0

            elif unit_len == 13:
                word_str = word_str + '조'
                unit_flag = 0


            unit_len = unit_len - 1


    return word_str



# 위의 패턴들에 해당하지 않는 나머지 숫자(온도, 화폐, 퍼센트 등등 포함) 읽는 법
def general_trans(u, index, text_list):

    for i in u:
        if type(i) == tuple:
            u_str = i[0]
        elif type(i) == str:
            u_str = i


        temperature_flag = 0
        currency_flag = 0

        number_str = u_str
        word_str = ''

        kor_len = 0

        if '℃' in u_str:
            temperature_flag = 1
            word_str = word_str + mark_dict['℃'] + ' '
        elif '℉' in u_str:
            temperature_flag = 1
            word_str = word_str + mark_dict['℉'] + ' '


        elif '$' in u_str or '＄' in u_str:
            cs = '＄'
            currency_flag = 1
        elif '￦' in u_str:
            cs = '￦'
            currency_flag = 1
        elif '￥' in u_str:
            cs = '￥'
            currency_flag = 1



        if '퍼센트' in u_str:
            kor_len = 3
        elif '개월' in u_str or '개년' in u_str:
            kor_len = 2
        elif '원' in u_str or '년' in u_str or '일' in u_str or '세' in u_str or '월' in u_str or '도' in u_str:
            kor_len = 1


        new_u_str = u_str.replace(',', '')        # new_cu_str 은 ',' 제거한 문자열


        # 소수점 없는 경우
        if '.' not in new_u_str:

            space_count = new_u_str.count(' ')        # 공백 개수
            unit_len = len(new_u_str) - kor_len - space_count

            if currency_flag == 1 or temperature_flag == 1:                     # -1 하는 이유는 화폐 기호 / 섭씨, 화씨 기호 때문.
                unit_len = unit_len - 1

            if '%' in new_u_str:        # -100, 100% 이면 자리수는 4가 아니라 3
                unit_len = unit_len - 1

            if '-' in new_u_str or '+' in new_u_str or '±' in new_u_str:
                unit_len = unit_len - 1

            if '%p' in new_u_str or '%P' in new_u_str:                          # 30%p 이면 자리수는 4가 아니라 2
                unit_len = unit_len - 2


            word_str = Cca_b_U_trans(new_u_str, word_str, unit_len)


        # 소수점 있는 경우
        elif '.' in new_u_str:
            # 소수점 기준으로 앞 부분과 뒷 부분으로 나눈다.
            point_divided_list = new_u_str.split('.')

            space_count = point_divided_list[0].count(' ')        # 소수점 앞의 공백 개수
            unit_len = len(point_divided_list[0]) - space_count   # 빼주자

            if currency_flag == 1:                          # -1 하는 이유는 화폐 기호 때문.
                unit_len = unit_len - 1

            if '-' in new_u_str or '+' in new_u_str or '±' in new_u_str:        # -36.5 이면 소수점 앞의 자리수는 3이 아니라 2
                unit_len = unit_len - 1

            # 앞부분은 단위 따져가며 읽어야한다.
            word_str = Cca_b_U_trans(point_divided_list[0], word_str, unit_len)

            # 사이에 '쩜' 추가해주고
            word_str = word_str + '쩜'


            # 뒷부분은 단위 없이 각각 한자어(ancient_dict)로 읽어야한다.
            for char in point_divided_list[1]:
                if char == '%' or char == '%p' or char == '%P':
                    word_str = word_str + ' ' + mark_dict[char]
                    continue

                elif char in mark_dict:
                    continue

                elif char == ' ':
                    word_str = word_str + char
                    continue

                elif char == '0':
                    word_str = word_str + '영'
                    continue

                word_str = word_str + ancient_dict[char]




        # 화폐 or 기온일 경우 마지막에 단위 써주자
        if currency_flag == 1:
                word_str = word_str + ' ' + mark_dict[cs]
        elif temperature_flag == 1:
            word_str = word_str + ' 도'



        translated_str = text_list[index].replace(number_str, word_str, 1)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.