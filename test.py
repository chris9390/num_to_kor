import re
pattern_phonenumber = re.compile(r'\d*\s*-\s*?\d{3}\s*-\s*\d{3,4}\s*-\s*\d{4}')
pattern_homenumber = re.compile(r'\d*\s*-\s*?\d{2,3}\s*-\s*\d{2,4}\s*-\s*\d{3,4}')
pattern_carnumber = re.compile(r'(([서울|부산|대구|인천|대전|광주|울산|제주|경기|강원|충남|전남|전북|경남|경북|세종]{2})?\s*\d{1,3}\s*[가-힣]{1}\s*\d{4})')
pattern_register = re.compile(r'\d{6}\s*-\s*\d{7}')
pattern_ip = re.compile(r'\d{1,3}\s*[.]\s*\d{1,3}\s*[.]\s*\d{1,3}\s*[.]\s*\d{1,3}')
pattern_time = re.compile(r'(([새벽|아침|오전|오후|저녁]{2})?\s*\d{1,2}\s*:\s*\d{2}\s*:?\s*\d{0,2})')
pattern_currency = re.compile(r'[$＄￦￥]\s*[\d,.]+')
pattern_temper = re.compile(r'[.\d]+\s*[℃℉]')


ancient_dict = {'0' : '영', '1' : '일', '2' : '이', '3' : '삼', '4' : '사', '5' : '오', '6' : '육', '7' : '칠', '8' : '팔', '9' : '구'}
kor_dict = {'0' : '공', '1' : '하나', '2' : '둘', '3' : '셋', '4' : '넷', '5' : '다섯', '6' : '여섯', '7' : '일곱', '8' : '여덟', '9' : '아홉'}
Kca_b_dict = {'1' : '한', '2' : '두', '3' : '세', '4' : '네', '5' : '다섯', '6' : '여섯', '7' : '일곱', '8' : '여덟', '9' : '아홉', '10' : '열', '11' : '열한', '12' : '열두'}


# fr = open('/home/public_data/news_corpus/news_norm_2015_100_264.txt', 'r')
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

        for num in pn_str:
            if num == '-':
                word_str = word_str + ' '
                number_str = number_str + '-'
            else:
                word_str = word_str + ancient_dict[num]
                number_str = number_str + num

        translated_str = text_list[index].replace(number_str, word_str)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.

def homenum_trans(hn, index):
    for hn_str in hn:
        number_str = ''
        word_str = ''

        for num in hn_str:
            if num == '-':
                word_str = word_str + ' '
                number_str = number_str + '-'
            else:
                word_str = word_str + ancient_dict[num]
                number_str = number_str + num

        translated_str = text_list[index].replace(number_str, word_str)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.

def carnum_trans(cn, index):
    for cn_tuple in cn:
        number_str = ''
        word_str = ''

        cn_str = cn_tuple[0]

        for num in cn_str:
            if (ord(num) >= ord('가') and ord(num) <= ord('힣')) or num == ' ':
                word_str = word_str + num
                number_str = number_str + num
            else:
                word_str = word_str + ancient_dict[num]
                number_str = number_str + num

        translated_str = text_list[index].replace(number_str, word_str)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.

def regnum_trans(rn, index):
    for rn_str in rn:
        number_str = ''
        word_str = ''

        for num in rn_str:
            if num == '-':
                word_str = word_str + ' '
                number_str = number_str + '-'
            else:
                word_str = word_str + ancient_dict[num]
                number_str = number_str + num

        translated_str = text_list[index].replace(number_str, word_str)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.

def ipnum_trans(ip, index):
    for ip_str in ip:
        number_str = ''
        word_str = ''

        for num in ip_str:
            if num == '.':
                word_str = word_str + ' '
                number_str = number_str + '.'
            else:
                word_str = word_str + ancient_dict[num]
                number_str = number_str + num

        translated_str = text_list[index].replace(number_str, word_str)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.

def timenum_trans(tn, index):
    for tn_tuple in tn:
        number_str = ''
        word_str = ''

        hour_flag = 1

        minute_flag = 0
        minute_turn = 2

        second_flag = 0
        second_turn = 2

        zero_before = 0

        tn_str = tn_tuple[0]
        if ('새벽' or '아침' or '오전' or '오후' or '저녁') not in tn_str:
            for num in tn_str:
                print('1')

        for num in tn_str:

            if (ord(num) >= ord('가') and ord(num) <= ord('힣')) or num == ' ':
                word_str = word_str + num
                number_str = number_str + num

            elif num == ':':
                word_str = word_str + ' '
                number_str = number_str + ':'

            else:
                number_str = number_str + num

                if hour_flag == 1:
                    word_str = word_str + Kca_b_dict[num] + '시'
                    hour_flag = 0
                    minute_flag = 1

                elif minute_flag == 1:
                    if minute_turn == 2:
                        if num == '0':
                            zero_before = 1
                            minute_turn = minute_turn - 1
                            continue
                        word_str = word_str + ancient_dict[num] + '십'
                        minute_turn = minute_turn - 1

                    elif minute_turn == 1:
                        if num == '0':
                            if zero_before == 1:
                                zero_before = 0
                                minute_flag = 0
                                second_flag = 1
                                continue
                            word_str = word_str + '분'
                        else:
                            word_str = word_str + ancient_dict[num] + '분'
                        minute_turn = minute_turn - 1
                        minute_flag = 0
                        second_flag = 1


                elif second_flag == 1:
                    if second_turn == 2:
                        if num == '0':
                            second_turn = second_turn - 1
                            zero_before = 1
                            continue
                        word_str = word_str + ancient_dict[num] + '십'
                        second_turn = second_turn - 1

                    elif second_turn == 1:
                        if num == '0':
                            if zero_before == 1:
                                zero_before = 0
                                second_flag = 0
                                continue
                            word_str = word_str + '초'
                        else:
                            word_str = word_str + ancient_dict[num] + '초'
                        second_turn = second_turn - 1
                        second_flag = 0


        translated_str = text_list[index].replace(number_str, word_str)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.




total = fr.readlines()

# 입력 파일을 읽어서 text_list 에 추가
count = 0
for i in total:
    if count == 13:
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
    pn = pattern_phonenumber.findall(text)
    hn = pattern_homenumber.findall(text)
    cn = pattern_carnumber.findall(text)
    rn = pattern_register.findall(text)
    ip = pattern_ip.findall(text)
    tn = pattern_time.findall(text)


    if pn:
        phonenum_trans(pn, index)
    elif hn:
        homenum_trans(hn, index)
    elif cn:
        carnum_trans(cn, index)
    elif rn:
        regnum_trans(rn, index)
    elif ip:
        ipnum_trans(ip, index)
    elif tn:
        timenum_trans(tn, index)

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




