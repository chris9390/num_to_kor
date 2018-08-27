import re
pattern_wave_with_space = re.compile(r'\s*[~-]\s*')
pattern_only_num = re.compile(r'\d+')

# 한자어
ancient_dict = {'0' : '공', '1' : '일', '2' : '이', '3' : '삼', '4' : '사', '5' : '오', '6' : '육', '7' : '칠', '8' : '팔', '9' : '구'}
# 명사 고유어
Kca_n_dict = {'0' : '공', '1' : '하나', '2' : '둘', '3' : '셋', '4' : '넷', '5' : '다섯', '6' : '여섯', '7' : '일곱', '8' : '여덟', '9' : '아홉'}
# 관형어 고유어
Kca_b_dict = {'0':'', '1' : '한', '2' : '두', '3' : '세', '4' : '네', '5' : '다섯', '6' : '여섯', '7' : '일곱', '8' : '여덟', '9' : '아홉'}
# 관형어 고유어 10의 자리
Kca_b_10_dict = {'0':'', '1' : '열', '2' : '스물', '3' : '서른', '4' : '마흔', '5' : '쉰', '6' : '예순', '7' : '일흔', '8' : '여든', '9' : '아흔'}
# 수의 단위
unit_dict = {'0' : '',
             '1' : '', '2' : '십', '3' : '백', '4' : '천',
             '5' : '', '6' : '십', '7' : '백', '8' : '천',         # 만
             '9' : '', '10' : '십', '11' : '백', '12' : '천',      # 억
             '13' : '', '14' : '십', '15' : '백', '16' : '천'}     # 조

# 수의 영어 읽기 사전
num_eng_dict = {'0' : '제로', '1' : '원', '2' : '투', '3' : '쓰리', '4' : '포', '5' : '파이브', '6' : '식스', '7' : '세븐', '8' : '에잇', '9' : '나인'}


# 특수문자
mark_dict = {'%' : '퍼센트', 'p' : '포인트',
             '℃': '섭씨', '℉': '화씨',
             '+': '플러스', '-': '마이너스', '±': '플러스마이너스',
             '$': '달러', '＄': '달러', '￦': '원', '￥': '엔',
             'gw': '기가와트', '㎾' : '킬로와트', 'kw' : '킬로와트', 'w': '와트',
             't': '톤', '㎏': '킬로그램', 'kg': '킬로그램', 'g': '그램',
             '㎞' : '킬로미터', 'km': '킬로미터', 'cm': '센티미터', 'mm': '밀리미터', 'm': '미터', '㎡' : '제곱미터'}


percent_dict = {'%p' : '퍼센트포인트', '%' : '퍼센트'}
temperature_dict = {'℃' : '섭씨', '℉' : '화씨'}
math_sign_dict = {'+' : '플러스', '-' : '마이너스', '±' : '플러스마이너스'}
currency_dict = {'$' : '달러', '＄' : '달러', '￦' : '원', '￥' : '엔'}
watt_dict = {'gw' : '기가와트','㎾' : '킬로와트', 'kw' : '킬로와트',  'w' : '와트'}
weight_dict = {'t' : '톤', '㎏' : '킬로그램', 'kg' : '킬로그램', 'g' : '그램'}
distance_dict = {'㎞' : '킬로미터', 'km' : '킬로미터', 'cm' : '센티미터', 'mm' : '밀리미터', 'm' : '미터', '㎡' : '제곱미터'}



human = ['남성', '장애인', '조선족', '여성', '고교', '연령', '미성년자', '할머니', '부부', '씨', '후반', '초반', '세탁', '여학생', '미혼', '고객', '장인', '중반', '아들', '가장', '실직', '직원', '꽃뱀', '일용직', '사진사', '한국인', '주차', '입주민', '경비원', '어머니', '취객', '아파트', '주민', '경찰관', '전직', '교사', '수배', '직장인', '카페', '주인', '도둑', '집주인', '고령', '엘리트', '이웃', '이혼녀', '장애', '손님', '백화점', '소년', '이웃집', '신원', '미상', '교직원', '초등학교', '신불', '부모', '노부', '층', '희생자', '업자', '이모', '청년층', '피의자', '디자이너', '동포', '여고생', '남매', '인질', '고교생', '인질범', '남', '남편', '보육', '남녀', '학생', '중국인', '때', '연인', '싱글', '맘', '청년', '소녀', '자살률', '여교사', '방', '엄마', '사이비', '후보', '법관', '딜러', '역술인', '재미', '교수', '회사원', '내연', '남자', '시절', '구속', '이복', '누나', '실종', '청소년', '교회', '선배', '피고인', '누리꾼', '조기', '조합원', '돌보미', '군', '포섭', '정신', '영어', '학원', '조직원', '의사', '수사', '피해자', '절도범', '귀농', '징역형', '남녀노소', '귀촌', '촌', '공갈', '딸', '단원', '예술', '감독', '일본', '선원', '관리', '대상', '아내', '강모', '정신과', '신경', '환자', '방글라데시', '여동생', '조폭', '조직', '폭력배', '사업가', '비서', '무직자', '종업원', '재력가', '공무원', '건물', '관리인', '재력', '치매', '아빠', '여대생', '용의자', '사병', '영어교사', '폭력', '세무', '제자', '여군', '뺑소니', '기사', '징역', '간호', '조무사', '산모', '어린이', '집', '대학생', '노모', '학원강사', '강사', '중후반', '원장', '유학생', '일당', '동호회', '커플', '의붓딸', '점장', '중학생', '운전자', '무속인', '할아버지', '질주', '남학생', '노동자', '주부', '검거', '검거외국계', '외국계', '등산객', '임신부', '매몰', '청와대', '호스트', '호스트바', '바', '당원', '정신분열병', '분열병', '클럽', '클럽여직원', '여직원', '여성대원', '대원', '여성교사', '아버지', '추정', '버스', '버스기사', '연인사이', '사이', '외국인', '모친', '형', '성인', '세입자', '덤프', '덤프트럭', '트럭', '고등', '고등학교', '학교', '유부남', '배낭', '배낭여행객', '여행객', '모로코', '성폭행', '대표', '노조', '대의원', '수련생', '이력서', '결혼', '중년층', '장년층', '협박', '내연녀', '행인', '사기범', '기혼', '숙박업', '숙박업주가', '독신', '여자', '다리', '가출', '경찰', '범행', '중년', '과외', '과외교사', '비중', '목', '자산가', '사위', '아저씨', '노령', '출마자', '형제간', '형수', '동생', '친형', '상습', '급증', '혼탁', '긴급', '체포', '충북', '마약', '의식', '영장', '여제자', '방화범', '남성환자', '강도', '가출청소년', '고교동창', '동창', '독거', '의경', '덜미', '아이돌그룹', '언니', '음악', '음악교사', '연예', '연예기획사', '기획사', '무명', '바바리맨', '청각', '청각장애', '새터민', '무속', '정신분열증', '분열증', '스포츠', '아나운서', '이사장', '도주', '오빠', '나이', '불량', '불량청소년', '긴급체포', '미국인', '가출소녀', '재판', '취업', '인도', '총선', '천안', '법원장', '사설', '초청', '초청강사', '살인범', '개인', '개인택시', '택시', '캐디', '근로', '근로자', '복무', '요원', '환경미화원', '미화원', '혁신', '혁신대책', '대책', '여주인', '식당', '실형', '만취', '정신지체장애인', '중형', '시매부', '노숙인', '회원', '사망률', '인재', '대학원', '젊은이', '자매', '패륜', '직장', '태국', '일본인', '사기꾼', '행동', '행동대장', '대장', '인부', '털이', '털이범', '여아', '여중생', '질식', '마약범', '택시기사', '강도단', '쌍둥이', '혼성', '마약사범', '사범', '전문직', '대학교수', '제주', '화가', '시어머니', '중앙', '중앙부처', '부처', '수용자', '실향민', '패륜남', '우정', '미국', '연소', '압수', '도망자', '전문', '골프', '동포여성', '전자발찌', '미혼모', '동거', '항소심', '백골', '고집', '고집불통', '취업준비', '준비', '택배', '택배기사', '해녀', '명문대', '검사', '헬스장', '유형', '목사', '구원', '구원파', '독일인', '조카', '승객', '학원생', '원생', '학원장', '집행', '집행유예', '유예', '전과자', '폭행', '입건', '대한민국', '탈북', '건설', '건설현장', '현장', '사회경험', '경험', '스토커', '성범죄', '모범', '모범무기수', '무기수', '불법', '불법체류', '체류', '수감자', '시각장애인', '한인', '중개인', '어르신', '국회의원', '만학도', '동거녀', '부친', '자녀', '국회', '병원', '응급', '응급처치', '처치', '가정주부', '사기단', '여기자', '추행', '매니저', '알코올', '중증', '중증장애', '총선거', '구속기소', '기소', '흉기', '부동산', '커피', '비율', '전화', '전화금융사기', '금융', '사기', '계모', '자전거', '폭력조직', '외국', '여자친구', '친구', '봉사자', '포스코', '격투기', '지제장애인', '스파이', '사장', '명품', '동네', '동네조폭', '업주', '공모자', '예비군', '전자팔찌', '팔찌', '여성환자', '익사', '마약제조업자', '제조', '다이버', '소개', '소개업체', '업체', '숙련공', '여사원', '발달', '발달장애인', '구속위조', '위조', '신혼부부', '정치인', '공중보건의', '보건', '트렌스젠더', '막내', '자살', '인물', '로스쿨', '적발', '전후', '횡령', '탈북여성', '의붓', '몽골인', '독립', '영화', '국기', '옛', '여성운전자', '성희롱', '사건', '고령자', '약사', '사망자', '입양아', '사망', '여인', '프랑스인', '선장', '메르스', '부부싸움', '싸움', '시민', '간호사', '스리랑카', '감염자', '칼부림', '고등학생', '보건복지부', '확진', '양성', '지역', '유명', '확진자', '임산부', '참가', '여류', '보안', '학부모', '정규직', '공익', '초보', '외과', '정신지체장애', '광주', '고법', '보행자', '터키인', '북한군', '남자가요', '가요', '자택', '슈퍼마켓', '범인', '고소', '순경', '필리핀', '마을', '의심', '목숨', '집유', '흑인', '의료진', '대학', '예비신랑', '신랑', '바다', '암', '암환자', '가수', '가요제', '인출', '응급실', '인원', '여행자', '강릉', '신도', '관광객', '노부부', '이상인', '건설업체', '회계사', '탈북자', '연령', '허리', '친딸', '변태', '지방', '행정', '연수', '주한', '이집트', '몰카', '비위', '발생', '여조카', '재벌기업', '배달', '노점상', '오토바이', '연구소', '예비역', '노숙자', '유망', '기술', '장모', '과실', '나이롱', '우울증', '납치', '커뮤니티', '건축', '살해', '변호사', '자신', '정신건강', '건강', '베이비부머', '간부', '잠적', '경기', '윗층', '현직', '전반', '여승무원', '승무원', '술자리', '동자승', '미혼남녀', '상습절도범', '편의점', '농민', '동료', '파견', '집행부', '안팎', '여하사', '배달원', '서비스', '연령별', '취업준비생', '무면허', '포함', '신입', '검찰', '남교사', '여성살인사건', '살인', '가사', '도우미', '일반', '부녀자', '보험', '설계사', '난민', '상해', '중고생', '새내기', '판사', '공기업', '구직', '구직여성', '재벌그룹', '직장인여성', '재경', '군인', '무직', '여판사', '복역', '승려', '관장', '술집', '고도비만', '비만', '상점', '독서광', '계약', '계약직', '소방관', '입원', '수강생', '팬', '몽골', '연습생', '교감', '관원', '할배', '여사', '휴학생', '아동', '투숙객', '유죄', '도박', '성폭력', '범죄', '보이스', '보이스피싱', '흡연', '연구원', '참전', '골프강사', '배달족', '헌병', '노인', '소장', '선로', '뺑소니범', '정비', '장애여성', '투자', '헬스', '트레이너', '해경', '인턴', '친부', '낚시꾼', '촬영', '소식', '채팅', '세관', '총책', '손녀', '자영업자', '기업인', '안마사', '에이즈', '감염자청춘', '피해', '범죄자', '사망원인', '중심', '의원', '난동', '나이트', '애인', '한의사', '민간', '차주', '의무경찰', '노년층', '취준', '마사지', '초등학생', '여성업주', '온라인', '대통령', '미군', '해외', '사용자', '계곡', '퇴역', '전역', '전역군인', '대졸', '퇴역군인', '중소기업', '성인남녀', '패륜아', '극성팬', '극성', '교도관', '농장', '농장주', '부인', '교민', '부산', '익사체', '해양', '해양경찰관', '흡연율', '농업', '농업인', '금은방', '운영자', '신부', '캣맘', '보복', '보복운전자', '병원장', '여가', '임차인', '날치기', '운전기사', '형제', '대리', '대리주차', '기혼남성', '이혼남', '양궁', '무죄', '수배자', '총리', '정신지체', '어민', '정신지체아', '지체아', '지구대', '습격', '고시생', '정신장애', '소방장', '초교', '당구장', '지체장애', '성매매', '주임', '유치원', '투신', '예비신부', '금수저', '미취업자', '중증장애인', '용접', '치매여성', '치매환자', '벌금형', '낚시객', '노부모', '아킬레스', '민원인', '골동품', '노교수', '위주', '유학파', '인기', '이식', '여성고객', '상가털이', '협력', '협력업체', '중년여성', '여신도', '친모', '대만인', '부문', '인도네시아', '가정', '가정폭력', '인도네시아인', '이집트인', '여경', '인구', '고아', '오늘', '정신병', '자가', '조사전', '금융관행', '관행', '약대', '기수', '치매질환', '질환', '박사', '논쟁', '주범', '식당주인', '유부녀', '북브로커', '브로커', '광화문', '시각장애', '김진태', '검찰총장', '불자', '전단', '아르바이트', '빈집', '국민', '다단계', '원로', '호텔', '태국인', '싱글족', '죽음', '예술인', '신원확인', '감시원', '사원', '회사', '재활', '프로그래머', '무장', '총괄', '흡연자', '순천', '순천향', '여행사', '워킹', '워킹맘', '루마니아', '불구속', '동창생']
generation = ['국정원','세계','신문','영역','원칙','운영','사업','과제','총장','선거','조직','혁신','그룹','국회','증권사','로펌','기업','신기술','대기업','슈퍼푸드','건강식품']



anc_kor_list = ['시간','차례','군데','마리','가지','사람','개사','보루','명','시','개','살','달','해','곳','배','대','장','갑','건','종','권']


translated_str = ''

def number_unit_trans(nu, index, text_list):
    for i in nu:

        if type(i) == tuple:
            nu_str = i[0]
        else:
            nu_str = i


        number_str = nu_str
        word_str = ''
        symbol = ''
        symbol_flag = 0
        symbol_len = 0

        space_len = nu_str.count(' ')
        comma_len = nu_str.count(',')
        kor_len = 1                     # '조', '억', '만', '천', '백', '십'

        for i in mark_dict:
            if i in nu_str:
                symbol = mark_dict[i]
                symbol_flag = 1
                symbol_len = len(i)

        num_len = len(nu_str) - space_len - comma_len - kor_len - symbol_len         # 자리수 예) 6,000 억 => num_len = 4


        if num_len == 1 and '1' in nu_str and '만' in nu_str:
            word_str = '만'
        elif num_len == 1 and '1' in nu_str and '천' in nu_str:
            word_str = '천'
        elif num_len == 1 and '1' in nu_str and '백' in nu_str:
            word_str = '백'
        elif num_len == 1 and '1' in nu_str and '십' in nu_str:
            word_str = '십'
        else:
            word_str = Cca_b_U_trans(nu_str, word_str, num_len)


        if symbol_flag == 1:
            word_str = word_str + symbol



        translated_str = text_list[index].replace(number_str, word_str, 1)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.

    return text_list[index]


def currency_kor_trans(ck, index, text_list):

    for i in ck:

        if type(i) == tuple:
            ck_str = i[0]
        #elif type(i) == str:
        else:
            ck_str = i


        number_str = ck_str
        word_str = ''
        kor_len = 0

        space_len = ck_str.count(' ')
        comma_len = ck_str.count(',')


        # 추출된 패턴에서 한글길이를 세어준다.
        for char in ck_str:
            if ord(char) >= ord('가') and ord(char) <= ord('힣'):
                kor_len = kor_len + 1


        num_len = len(ck_str) - space_len - comma_len - kor_len         # 자리수 예) 6,000 달러 => num_len = 4

        word_str = Cca_b_U_trans(ck_str, word_str, num_len)




        translated_str = text_list[index].replace(number_str, word_str, 1)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.

    return text_list[index]



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

    return text_list[index]


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

    return text_list[index]


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

    return text_list[index]


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

    return text_list[index]


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

    return text_list[index]


def order_trans(on, index, text_list):

    for i in on:

        if type(i) == tuple:
            on_str = i[0]
        #elif type(i) == str:
        else:
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

    return text_list[index]


def date_trans(da, index, text_list):

    for i in da:

        if type(i) == tuple:
            da_str = i[0]
        #elif type(i) == str:
        else:
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

    return text_list[index]


def anniversary_trans(an, index, text_list):
    for i in an:

        if type(i) == tuple:
            an_str = i[0]
        #elif type(i) == str:
        else:
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

    return text_list[index]



def wave_anc_trans(wa, index, text_list):
    for i in wa:
        if type(i) == tuple:
            wa_str = i[0]
        #elif type(i) == str:
        else:
            wa_str = i

        number_str = wa_str
        word_str = ''
        symbol = ''

        symbol_flag = 0
        symbol_len = 0
        space_len = 0
        kor_len = 0
        num_len = 0



        # 물결('~') 양옆의 공백 제거
        wws = pattern_wave_with_space.findall(wa_str)
        for i in wws:
            if '~' in wa_str:
                wa_str = wa_str.replace(i, '~')
            elif '∼' in wa_str:
                wa_str = wa_str.replace(i, '∼')
            elif '-' in wa_str:
                wa_Str = wa_str.replace(i, '-')



        if '~' in wa_str:
            wave_divided_list = wa_str.split('~')
        elif '∼' in wa_str:
            wave_divided_list = wa_str.split('∼')
        elif '-' in wa_str:
            wave_divided_list = wa_str.split('-')



        # '~' 앞 부분 처리
        for i in mark_dict:
            if i in wave_divided_list[0]:
                symbol = i
                symbol_kor = mark_dict[i]
                symbol_len = len(symbol)
                symbol_flag = 1
                break



        # 소수점이 있는 경우
        if '.' in wave_divided_list[0]:
            word_str = word_str + point_read(wave_divided_list[0])

        # 소수점이 없는 경우
        else:
            # '퍼센트'같은 우리말이 사용된 경우
            if symbol_flag == 0:
                for char in wave_divided_list[0]:
                    if ord(char) >= ord('가') and ord(char) <= ord('힣'):
                        kor_len = kor_len + 1
                    if char == ' ':
                        space_len = space_len + 1

                num_len = len(wave_divided_list[0]) - kor_len - space_len


            # '%'같은 특수문자가 사용된 경우
            elif symbol_flag == 1:
                for char in wave_divided_list[0]:
                    if char == ' ':
                        space_len = space_len + 1

                num_len = len(wave_divided_list[0]) - symbol_len - space_len

                wave_divided_list[0] = wave_divided_list[0].replace(symbol, '')


            word_str = word_str + Cca_b_U_trans(wave_divided_list[0], word_str, num_len)


        # 특수문자가 사용되었으면 다시 붙여주자
        if symbol_flag == 1:
            word_str = word_str + symbol_kor


        # =========================================================================

        # '~' 문자 변환
        word_str = word_str + '에서'

        # =========================================================================


        space_len = 0
        symbol_len = 0
        kor_len = 0
        num_len = 0
        symbol_flag = 0

        # '~' 뒷 부분 처리
        for i in mark_dict:
            if i in wave_divided_list[1]:
                symbol = i
                symbol_kor = mark_dict[i]
                symbol_len = len(symbol)
                symbol_flag = 1
                break

        # 소수점이 있는 경우
        if '.' in wave_divided_list[1]:
            word_str = word_str + point_read(wave_divided_list[1])

        # 소수점이 없는 경우
        else:
            if symbol_flag == 0:
                for char in wave_divided_list[1]:
                    if ord(char) >= ord('가') and ord(char) <= ord('힣'):
                        kor_len = kor_len + 1
                    if char == ' ':
                        space_len = space_len + 1

                num_len = len(wave_divided_list[1]) - kor_len - space_len

            elif symbol_flag == 1:
                for char in wave_divided_list[1]:
                    if char == ' ':
                        space_len = space_len + 1

                num_len = len(wave_divided_list[1]) - symbol_len - space_len

                wave_divided_list[1] = wave_divided_list[1].replace(symbol, '')



            word_str = word_str + Cca_b_U_trans(wave_divided_list[1], '', num_len)


        # 특수문자가 사용되었으면 다시 붙여주자
        if symbol_flag == 1:
            word_str = word_str + symbol_kor



        translated_str = text_list[index].replace(number_str, word_str, 1)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.


    return text_list[index]



def wave_kor_trans(wk, index, text_list):

    for i in wk:

        if type(i) == tuple:
            wk_str = i[0]
        else:
            wk_str = i


        number_str = wk_str
        word_str = ''

        kor_len = 0
        space_len = 0
        symbol_before_flag = 0
        unit_after_flag = 0
        Cca_should_work = 0

        num_diff = 0




        # 물결('~') 양옆의 공백 제거
        wws = pattern_wave_with_space.findall(wk_str)
        for i in wws:
            if '~' in wk_str:
                wk_str = wk_str.replace(i, '~')
            elif '∼' in wk_str:
                wk_str = wk_str.replace(i, '∼')
            elif '-' in wk_str:
                wk_str = wk_str.replace(i, '-')



        if '~' in wk_str:
            wave_divided_list = wk_str.split('~')
        elif '∼' in wk_str:
            wave_divided_list = wk_str.split('∼')
        elif '-' in wk_str:
            wave_divided_list = wk_str.split('-')

        # =========================================================================

        symbol_before = ''
        for char in wave_divided_list[0]:
            if (ord(char) >= ord('가') and ord(char) <= ord('힣')) or char == ' ':
                symbol_before_flag = 1
                symbol_before = symbol_before + char


        # '10~60명' 의 예에서 num_before는 '10'에 해당
        num_before = wave_divided_list[0].replace(symbol_before, '')

        # =========================================================================

        symbol_after = ''
        for char in wave_divided_list[1]:
            if (ord(char) >= ord('가') and ord(char) <= ord('힣')) or char == ' ':
                symbol_after = symbol_after + char
            # 글자 단위가 있으면
            if char == '십' or char == '백' or char == '만':
                unit_after_flag = 1



        # '10~60명' 의 예에서 num_after는 '60'에 해당
        num_after = wave_divided_list[1].replace(symbol_after, '')

        # =========================================================================


        if '.' not in num_before and '.' not in num_after:
            num_diff = int(num_after) - int(num_before)


        num_before_len = len(num_before) #- space_before
        num_after_len = len(num_after) #- space_after

        # 2~3명 => 두세명   이런 경우
        if num_diff == 1 and num_before_len == 1 and num_after_len == 1 and symbol_before_flag == 0 and unit_after_flag == 0:
            word_str = word_str + Kca_b_trans(num_before, word_str, num_before_len)
            word_str = word_str + Kca_b_trans(num_after, '', num_after_len)
            word_str = word_str + symbol_after


        # 10 ~ 60명 => 십 에서 육십명   이런 경우
        # 10명 ~ 60명 => 열명 에서 육십명
        else:

            # '~' 앞 부분 처리

            # 소수점이 있는 경우
            if '.' in wave_divided_list[0]:
                word_str = word_str + point_read(wave_divided_list[0])

            # 소수점이 없는 경우
            else:
                for char in wave_divided_list[0]:
                    if (ord(char) >= ord('가') and ord(char) <= ord('힣')):
                        kor_len = kor_len + 1
                    if char == ' ':
                        space_len = space_len + 1

                num_len = len(wave_divided_list[0]) - kor_len - space_len


                # '10명 ~ 60명' 이렇게 앞부분의 숫자에도 분류사가 있는 경우
                if symbol_before_flag == 1:
                    #if (num_len == 2 and int(num_before) >= 5) or num_len >= 3:
                    if int(num_before) >= 50:
                        Cca_should_work = 1

                    if Cca_should_work == 1:
                        word_str = word_str + Cca_b_U_trans(wave_divided_list[0], word_str, num_len)


                    else:
                        word_str = word_str + Kca_b_trans(wave_divided_list[0], word_str, num_len)


                # '10 ~ 60명'
                else:
                    word_str = word_str + Cca_b_U_trans(wave_divided_list[0], word_str, num_len)

            # =========================================================================

            # '~' 문자 변환
            word_str = word_str + '에서'

            # =========================================================================

            kor_len = 0
            space_len = 0
            #Cca_should_work = 0


            # '~' 뒷 부분 처리

            # 소수점이 있는 경우
            if '.' in wave_divided_list[1]:
                word_str = word_str + point_read(wave_divided_list[1])

            # 소수점이 없는 경우
            else:

                for char in wave_divided_list[1]:
                    if ord(char) >= ord('가') and ord(char) <= ord('힣'):
                        kor_len = kor_len + 1
                    if char == ' ':
                        space_len = space_len + 1

                num_len = len(wave_divided_list[1]) - kor_len - space_len



                if symbol_before_flag == 1:
                    #if (num_len == 2 and int(num_before) >= 5) or num_len >= 3:
                    if int(num_after) >= 50:
                        Cca_should_work = 1

                    if Cca_should_work == 1:
                        word_str = Cca_b_U_trans(wave_divided_list[1], word_str, num_len)


                    else:
                        word_str = Kca_b_trans(wave_divided_list[1], word_str, num_len)


                else:
                    word_str = Cca_b_U_trans(wave_divided_list[1], word_str, num_len)





        translated_str = text_list[index].replace(number_str, word_str, 1)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.

    return text_list[index]



def wave_else(we, index, text_list):
    for i in we:

        if type(i) == tuple:
            we_str = i[0]
        #elif type(i) == str:
        else:
            we_str = i

        number_str = we_str
        word_str = ''


        if '∼' in we_str:
            word_str = we_str.replace('∼', '에서')
        elif '~' in we_str:
            word_str = we_str.replace('~', '에서')



        translated_str = text_list[index].replace(number_str, word_str, 1)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.

    return text_list[index]




def eng_num_trans(en, index, text_list):
    for i in en:

        if type(i) == tuple:
            en_str = i[0]
        else:
            en_str = i

        number_str = en_str
        word_str = ''
        num_str = ''
        no_more = 0

        # 숫자 부분만 추출
        num_extract = pattern_only_num.findall(en_str)
        if num_extract:
            num_str = num_extract[0]

        # 숫자 제외 영어 부분
        eng_str = en_str.replace(num_str, '')

        # sm5, k9
        if len(num_str) == 1:
            word_str = en_str.replace(num_str, num_eng_dict[num_str])

        # QZ8501
        else:
            for char in en_str:
                if ord(char) >= ord('0') and ord(char) <= ord('9'):
                    if no_more == 0:
                        word_str =  word_str + Cca_b_U_trans(num_str, '', len(num_str))
                        no_more = 1
                else:
                    word_str = word_str + char



        translated_str = text_list[index].replace(number_str, word_str, 1)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.

    return text_list[index]



def num_eng_trans(ne, index, text_list):
    for i in ne:

        if type(i) == tuple:
            ne_str = i[0]
        else:
            ne_str = i


        number_str = ne_str
        word_str = ''

        ne_str = ne_str.lower()

        # 숫자 부분만 추출
        num_extract = pattern_only_num.findall(ne_str)
        if num_extract:
            num_str = num_extract[0]


        # 숫자 제외 영어 부분
        eng_str = ne_str.replace(num_str, '')
        eng_str = eng_str.replace(' ', '')


        # 3cm 같이 단위를 뜻하는 것이면 여기서 처리하는게 아니라 나중에 처리해준다.
        # 2D 같이 단위를 뜻하지 않는 것만 이 함수에서 처리.
        if eng_str in mark_dict:
            break

        # '2014 MBC 가요 대전' 같이 숫자 부분이 1자리 초과인 경우 거른다.
        if len(num_str) > 1:
            break


        word_str = ne_str.replace(num_str, num_eng_dict[num_str])



        translated_str = text_list[index].replace(number_str, word_str, 1)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.

    return text_list[index]




# 50미만은 Kca_b_trans함수 호출해서 고유어 수사 처리
# 50이상은 Cca_b_U_trans함수 호출해서 한자어 수사 처리
# 3 마리 -> 세 마리, 50 마리-> 오십 마리
def kor_anc_trans(koranc, index, text_list):
    for i in koranc:

        if type(i) == tuple:
            koranc_str = i[0]
        #elif type(i) == str:
        else:
            koranc_str = i


        number_str = koranc_str
        word_str = ''
        kor_len = 0
        Cca_should_work = 0

        # 소수점인 경우
        if '.' in koranc_str:
            word_str = point_read(koranc_str)
        else:
            space_len = koranc_str.count(' ')  # 공백 개수
            comma_len = koranc_str.count(',')  # ',' 개수

            # 추출된 패턴에서 한글길이를 세어준다.
            for char in koranc_str:
                if ord(char) >= ord('가') and ord(char) <= ord('힣'):
                    kor_len = kor_len + 1

            num_len = len(koranc_str) - space_len - comma_len - kor_len  # 숫자만의 길이. 공백, 콤마 개수 빼준다.


            # 여기서 숫자 부분의 크기를 측정해서 50이상은 Cca함수 호출 / 50미만은 이 밑의 과정
            if (num_len == 2 and int(koranc_str[0]) >= 5) or num_len >= 3:
                Cca_should_work = 1

            # 숫자가 50이상인 경우
            if Cca_should_work == 1:
                word_str = Cca_b_U_trans(koranc_str, word_str, num_len)

            # 숫자가 50미만인 경우
            else:
                word_str = Kca_b_trans(koranc_str, word_str, num_len)



        translated_str = text_list[index].replace(number_str, word_str, 1)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.

    return text_list[index]


# Kca_b 로 읽는 경우
# 관형어 고유어 변환
# 1 -> 한,  10 -> 열
def Kca_b_trans(input_str, output_str, length):

    kca_str = input_str
    word_str = output_str
    num_len = length
    len_checker = num_len
    unit_flag = 0


    for char in kca_str:
        if (ord(char) >= ord('가') and ord(char) <= ord('힣')) or char == ' ':
            word_str = word_str + char
            continue

        elif char == ',':
            continue

        # 0시 같은 경우
        elif char == '0' and num_len == 1:
            word_str = word_str +'영'
            continue

        elif char == '0' and num_len != 1:
            continue

        else:
            # 자리수가 2일때 부터 Kca 로 바꿔준다. 2보다 클땐 Cca_b[+U]로 읽는다.
            # Kca_b
            if len_checker == 2:
                if char == '2' and '0' in kca_str:
                    word_str = word_str + '스무'
                else:
                    word_str = word_str + Kca_b_10_dict[char]
            elif len_checker == 1:
                word_str = word_str + Kca_b_dict[char]

            '''
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
            '''

        len_checker = len_checker - 1

    return word_str





# Cca_b[+U] 로 읽는 경우
# 315 => 삼백십오
# -315 => 마이너스삼백십오
def Cca_b_U_trans(input_str, output_str, length):

    cca_str = input_str
    word_str = output_str
    original_len = length
    unit_len = length           # 단위 제외 숫자만의 길이 ('12 개월' => unit_len = 2)
    unit_flag = 0
    no_more = 0



    for char in cca_str:
        if '10' in cca_str and '월' in cca_str and no_more == 0:
            word_str = word_str + '시'
            no_more = 1

        elif '6' in cca_str and '월' in cca_str and no_more == 0:
            word_str = word_str + '유'
            no_more = 1

        elif char in math_sign_dict:
            word_str = word_str + math_sign_dict[char]
            continue

        elif char == ',':
            continue

        elif char in mark_dict:
            continue

        elif (ord(char) >= ord('a') and ord(char) <= ord('z')) or (ord(char) >= ord('A') and ord(char) <= ord('Z')):
            continue

        elif (ord(char) >= ord('가') and ord(char) <= ord('힣')) or char == ' ':
            word_str = word_str + char


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
def anc_trans(anc, index, text_list, pattern):

    for i in anc:
        if type(i) == tuple:
            anc_str = i[0]
        #elif type(i) == str:
        else:
            anc_str = i

        age_flag = 0
        generation_flag = 0


        for j in human:
            if j in anc_str:
                age_flag = 1
                break


        for j in generation:
            if j in anc_str:
                generation_flag = 1
                break




        # 나이를 뜻하는 '대' 인 경우가 아닌 차량 대수를 뜻하는 경우에는 지금 처리하지 않고 나중에 kc패턴에서 처리한다.
        if pattern == 'ad' and age_flag == 0:
            continue


        if pattern == 'ge' and generation_flag == 0:
            continue

        math_sign_flag = 0
        temperature_flag = 0
        currency_flag = 0
        symbol = ''
        no_more = 0

        number_str = anc_str
        word_str = ''

        kor_len = 0
        unit_len = 0

        anc_str = anc_str.lower()



        if no_more == 0:
            for i in temperature_dict:
                if i in anc_str:
                    temperature_flag = 1
                    word_str = word_str + temperature_dict[i] + ' '
                    symbol = '도'
                    unit_len = len(i)
                    no_more = 1
                    break


        if no_more == 0:
            for i in percent_dict:
                if i in anc_str:
                    symbol = percent_dict[i]
                    unit_len = len(i)
                    no_more = 1
                    break

        if no_more == 0:
            for i in currency_dict:
                if i in anc_str:
                    #cs = i
                    symbol = currency_dict[i]
                    unit_len = len(i)
                    currency_flag = 1
                    no_more = 1
                    break

        if no_more == 0:
            for i in watt_dict:
                if i in anc_str:
                    symbol = watt_dict[i]
                    unit_len = len(i)
                    no_more = 1
                    break

        if no_more == 0:
            for i in weight_dict:
                if i in anc_str:
                    symbol = weight_dict[i]
                    unit_len = len(i)
                    no_more = 1
                    break

        if no_more == 0:
            for i in distance_dict:
                if i in anc_str:
                    symbol = distance_dict[i]
                    unit_len = len(i)
                    no_more = 1
                    break



        # -, + 같은 기호는 다른 기호와 함께 나올 수 있으므로 no_more 조건문 없어야한다.
        for i in math_sign_dict:
            if i in anc_str:
                #word_str = word_str + math_sign_dict[i]
                math_sign_flag = 1
                unit_len = unit_len + len(i)
                break


        # 추출된 패턴에서 한글길이를 세어준다.
        for char in anc_str:
            if ord(char) >= ord('가') and ord(char) <= ord('힣'):
                kor_len = kor_len + 1




        new_anc_str = anc_str.replace(',', '')        # new_cu_str 은 ',' 제거한 문자열
        new_anc_str = new_anc_str.replace('\n', '')


        # 소수점 없는 경우
        if '.' not in new_anc_str:

            space_count = new_anc_str.count(' ')        # 공백 개수
            num_len = len(new_anc_str) - kor_len - space_count - unit_len



            word_str = Cca_b_U_trans(new_anc_str, word_str, num_len)


        # 소수점 있는 경우
        elif '.' in new_anc_str:
            word_str = word_str + point_read(new_anc_str)



        # 단위 'symbol' 써주는 부분
        word_str = word_str + symbol



        translated_str = text_list[index].replace(number_str, word_str, 1)
        text_list[index] = translated_str  # 변경된 string을 계속 업데이트 해준다.

    return text_list[index]





# 소수점 읽기 함수
def point_read(string_before):

    string_after = ''

    # 소수점 기준으로 앞 부분과 뒷 부분으로 나눈다.
    point_divided_list = string_before.split('.')

    space_count = point_divided_list[0].count(' ')  # 소수점 앞의 공백 개수
    num_len = len(point_divided_list[0]) - space_count  # 빼주자


    # $3.5 인 경우에 소수점 앞의 자리수는 2가 아니라 1
    for i in currency_dict:
        if i in point_divided_list[0]:
            num_len = num_len - 1
            break


    # -36.5 인 경우에 소수점 앞의 자리수는 3이 아니라 2
    for i in math_sign_dict:
        if i in point_divided_list[0]:
            num_len = num_len - 1
            break


    # 앞부분은 단위 따져가며 읽어야한다.
    string_after = Cca_b_U_trans(point_divided_list[0], string_after, num_len)

    # =========================================================================

    # 사이에 '쩜' 추가해주고
    string_after = string_after + '쩜'

    # =========================================================================

    # 뒷부분은 단위 없이 각각 한자어(ancient_dict)로 읽어야한다.
    for char in point_divided_list[1]:
        if char in mark_dict:
            continue

        elif (ord(char) >= ord('a') and ord(char) <= ord('z')) or (ord(char) >= ord('A') and ord(char) <= ord('Z')):
            continue

        elif (ord(char) >= ord('가') and ord(char) <= ord('힣')) or char == ' ':
            string_after = string_after + char
            continue

        elif char == '0':
            string_after = string_after + '영'
            continue

        string_after = string_after + ancient_dict[char]


    return string_after