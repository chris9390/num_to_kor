# -*- coding: utf-8 -*-

from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma = Kkma()

import re
pattern_kor = re.compile(r'[^0-9]*')
pattern_short = re.compile(r'[1-9]0대\s*[가-힣]{0,10}')
pattern_long = re.compile(r'[가-힣]{0,10}\s*[가-힣]{0,10}\s*[1-9]0대\s*[가-힣]{0,10}\s*[가-힣]{0,10}')
pattern_wave = re.compile(r'\D{0,10}\s*\d+\s*\D{0,5}\s*[~]\s*\d+\s*\D{0,10}')


fr = open('/home/s20131533/pycharm_numbertoword/filtered/103_237_filtered.txt', 'r', encoding='UTF8')
#fw = open('filtered/103_237_filtered.txt', 'w')
fw = open('wave.txt','w')

total = fr.readlines()

text_list = []


vehicle = ['차량', '헬기', '버스', '승용차', '중고차', '차', '배치', '신규', '선적', '연소', '확보', '분량']
human = ['남성', '장애인', '조선족', '여성', '고교', '연령', '미성년자', '할머니', '부부', '씨', '후반', '초반', '세탁', '여학생', '미혼', '고객', '장인', '중반', '아들', '가장', '실직', '직원', '꽃뱀', '일용직', '사진사', '한국인', '주차', '입주민', '경비원', '어머니', '취객', '아파트', '주민', '경찰관', '전직', '교사', '수배', '직장인', '카페', '주인', '도둑', '집주인', '고령', '엘리트', '이웃', '이혼녀', '장애', '손님', '백화점', '소년', '이웃집', '신원', '미상', '교직원', '초등학교', '신불', '부모', '노부', '층', '희생자', '업자', '이모', '청년층', '피의자', '디자이너', '동포', '여고생', '남매', '인질', '고교생', '인질범', '남', '남편', '보육', '남녀', '학생', '중국인', '때', '연인', '싱글', '맘', '청년', '소녀', '자살률', '여교사', '방', '엄마', '사이비', '후보', '법관', '딜러', '역술인', '재미', '교수', '회사원', '내연', '남자', '시절', '구속', '이복', '누나', '실종', '청소년', '교회', '선배', '피고인', '누리꾼', '조기', '조합원', '돌보미', '군', '포섭', '정신', '영어', '학원', '조직원', '의사', '수사', '피해자', '절도범', '귀농', '징역형', '남녀노소', '귀촌', '촌', '공갈', '딸', '단원', '예술', '감독', '일본', '선원', '관리', '대상', '아내', '강모', '정신과', '신경', '환자', '방글라데시', '여동생', '조폭', '조직', '폭력배', '사업가', '비서', '무직자', '종업원', '재력가', '공무원', '건물', '관리인', '재력', '치매', '아빠', '여대생', '용의자', '사병', '영어교사', '폭력', '세무', '제자', '여군', '뺑소니', '기사', '징역', '간호', '조무사', '산모', '어린이', '집', '대학생', '노모', '학원강사', '강사', '중후반', '원장', '유학생', '일당', '동호회', '커플', '의붓딸', '점장', '중학생', '운전자', '무속인', '할아버지', '질주', '남학생', '노동자', '주부', '검거', '검거외국계', '외국계', '등산객', '임신부', '매몰', '청와대', '호스트', '호스트바', '바', '당원', '정신분열병', '분열병', '클럽', '클럽여직원', '여직원', '여성대원', '대원', '여성교사', '아버지', '추정', '버스', '버스기사', '연인사이', '사이', '외국인', '모친', '형', '성인', '세입자', '덤프', '덤프트럭', '트럭', '고등', '고등학교', '학교', '유부남', '배낭', '배낭여행객', '여행객', '모로코', '성폭행', '대표', '노조', '대의원', '수련생', '이력서', '결혼', '중년층', '장년층', '협박', '내연녀', '행인', '사기범', '기혼', '숙박업', '숙박업주가', '독신', '여자', '다리', '가출', '경찰', '범행', '중년', '과외', '과외교사', '비중', '목', '자산가', '사위', '아저씨', '노령', '출마자', '형제간', '형수', '동생', '친형', '상습', '급증', '혼탁', '긴급', '체포', '충북', '마약', '의식', '영장', '여제자', '방화범', '남성환자', '강도', '가출청소년', '고교동창', '동창', '독거', '의경', '덜미', '아이돌그룹', '언니', '음악', '음악교사', '연예', '연예기획사', '기획사', '무명', '바바리맨', '청각', '청각장애', '새터민', '무속', '정신분열증', '분열증', '스포츠', '아나운서', '이사장', '도주', '오빠', '나이', '불량', '불량청소년', '긴급체포', '미국인', '가출소녀', '재판', '취업', '인도', '총선', '천안', '법원장', '사설', '초청', '초청강사', '살인범', '개인', '개인택시', '택시', '캐디', '근로', '근로자', '복무', '요원', '환경미화원', '미화원', '혁신', '혁신대책', '대책', '여주인', '식당', '실형', '만취', '정신지체장애인', '중형', '시매부', '노숙인', '회원', '사망률', '인재', '대학원', '젊은이', '자매', '패륜', '직장', '태국', '일본인', '사기꾼', '행동', '행동대장', '대장', '인부', '털이', '털이범', '여아', '여중생', '질식', '마약범', '택시기사', '강도단', '쌍둥이', '혼성', '마약사범', '사범', '전문직', '대학교수', '제주', '화가', '시어머니', '중앙', '중앙부처', '부처', '수용자', '실향민', '패륜남', '우정', '미국', '연소', '압수', '도망자', '전문', '골프', '동포여성', '전자발찌', '미혼모', '동거', '항소심', '백골', '고집', '고집불통', '취업준비', '준비', '택배', '택배기사', '해녀', '명문대', '검사', '헬스장', '유형', '목사', '구원', '구원파', '독일인', '조카', '승객', '학원생', '원생', '학원장', '집행', '집행유예', '유예', '전과자', '폭행', '입건', '대한민국', '탈북', '건설', '건설현장', '현장', '사회경험', '경험', '스토커', '성범죄', '모범', '모범무기수', '무기수', '불법', '불법체류', '체류', '수감자', '시각장애인', '한인', '중개인', '어르신', '국회의원', '만학도', '동거녀', '부친', '자녀', '국회', '병원', '응급', '응급처치', '처치', '가정주부', '사기단', '여기자', '추행', '매니저', '알코올', '중증', '중증장애', '총선거', '구속기소', '기소', '흉기', '부동산', '커피', '비율', '전화', '전화금융사기', '금융', '사기', '계모', '자전거', '폭력조직', '외국', '여자친구', '친구', '봉사자', '포스코', '격투기', '지제장애인', '스파이', '사장', '명품', '동네', '동네조폭', '업주', '공모자', '예비군', '전자팔찌', '팔찌', '여성환자', '익사', '마약제조업자', '제조', '다이버', '소개', '소개업체', '업체', '숙련공', '여사원', '발달', '발달장애인', '구속위조', '위조', '신혼부부', '정치인', '공중보건의', '보건', '트렌스젠더', '막내', '자살', '인물', '로스쿨', '적발', '전후', '횡령', '탈북여성', '의붓', '몽골인', '독립', '영화', '국기', '옛', '여성운전자', '성희롱', '사건', '고령자', '약사', '사망자', '입양아', '사망', '여인', '프랑스인', '선장', '메르스', '부부싸움', '싸움', '시민', '간호사', '스리랑카', '감염자', '칼부림', '고등학생', '보건복지부', '확진', '양성', '지역', '유명', '확진자', '임산부', '참가', '여류', '보안', '학부모', '정규직', '공익', '초보', '외과', '정신지체장애', '광주', '고법', '보행자', '터키인', '북한군', '남자가요', '가요', '자택', '슈퍼마켓', '범인', '고소', '순경', '필리핀', '마을', '의심', '목숨', '집유', '흑인', '의료진', '대학', '예비신랑', '신랑', '바다', '암', '암환자', '가수', '가요제', '인출', '응급실', '인원', '여행자', '강릉', '신도', '관광객', '노부부', '이상인', '건설업체', '회계사', '탈북자', '연령', '허리', '친딸', '변태', '지방', '행정', '연수', '주한', '이집트', '몰카', '비위', '발생', '여조카', '재벌기업', '배달', '노점상', '오토바이', '연구소', '예비역', '노숙자', '유망', '기술', '장모', '과실', '나이롱', '우울증', '납치', '커뮤니티', '건축', '살해', '변호사', '자신', '정신건강', '건강', '베이비부머', '간부', '잠적', '경기', '윗층', '현직', '전반', '여승무원', '승무원', '술자리', '동자승', '미혼남녀', '상습절도범', '편의점', '농민', '동료', '파견', '집행부', '안팎', '여하사', '배달원', '서비스', '연령별', '취업준비생', '무면허', '포함', '신입', '검찰', '남교사', '여성살인사건', '살인', '가사', '도우미', '일반', '부녀자', '보험', '설계사', '난민', '상해', '중고생', '새내기', '판사', '공기업', '구직', '구직여성', '재벌그룹', '직장인여성', '재경', '군인', '무직', '여판사', '복역', '승려', '관장', '술집', '고도비만', '비만', '상점', '독서광', '계약', '계약직', '소방관', '입원', '수강생', '팬', '몽골', '연습생', '교감', '관원', '할배', '여사', '휴학생', '아동', '투숙객', '유죄', '도박', '성폭력', '범죄', '보이스', '보이스피싱', '흡연', '연구원', '참전', '골프강사', '배달족', '헌병', '노인', '소장', '선로', '뺑소니범', '정비', '장애여성', '투자', '헬스', '트레이너', '해경', '인턴', '친부', '낚시꾼', '촬영', '소식', '채팅', '세관', '총책', '손녀', '자영업자', '기업인', '안마사', '에이즈', '감염자청춘', '피해', '범죄자', '사망원인', '중심', '의원', '난동', '나이트', '애인', '한의사', '민간', '차주', '의무경찰', '노년층', '취준', '마사지', '초등학생', '여성업주', '온라인', '대통령', '미군', '해외', '사용자', '계곡', '퇴역', '전역', '전역군인', '대졸', '퇴역군인', '중소기업', '성인남녀', '패륜아', '극성팬', '극성', '교도관', '농장', '농장주', '부인', '교민', '부산', '익사체', '해양', '해양경찰관', '흡연율', '농업', '농업인', '금은방', '운영자', '신부', '캣맘', '보복', '보복운전자', '병원장', '여가', '임차인', '날치기', '운전기사', '형제', '대리', '대리주차', '기혼남성', '이혼남', '양궁', '무죄', '수배자', '총리', '정신지체', '어민', '정신지체아', '지체아', '지구대', '습격', '고시생', '정신장애', '소방장', '초교', '당구장', '지체장애', '성매매', '주임', '유치원', '투신', '예비신부', '금수저', '미취업자', '중증장애인', '용접', '치매여성', '치매환자', '벌금형', '낚시객', '노부모', '아킬레스', '민원인', '골동품', '노교수', '위주', '유학파', '인기', '이식', '여성고객', '상가털이', '협력', '협력업체', '중년여성', '여신도', '친모', '대만인', '부문', '인도네시아', '가정', '가정폭력', '인도네시아인', '이집트인', '여경', '인구', '고아', '오늘', '정신병', '자가', '조사전', '금융관행', '관행', '약대', '기수', '치매질환', '질환', '박사', '논쟁', '주범', '식당주인', '유부녀', '북브로커', '브로커', '광화문', '시각장애', '김진태', '검찰총장', '불자', '전단', '아르바이트', '빈집', '국민', '다단계', '원로', '호텔', '태국인', '싱글족', '죽음', '예술인', '신원확인', '감시원', '사원', '회사', '재활', '프로그래머', '무장', '총괄', '흡연자', '순천', '순천향', '여행사', '워킹', '워킹맘', '루마니아', '불구속', '동창생']
ambiguous = ['모두', '이상', '이하', '조사', '이후', '등']



count = 0
for i in total:
    #if count == 200:
    #    break

    text_list.append(i)

    count = count + 1


for text in text_list:
    s = pattern_wave.findall(text)
    if s:
        for i in s:
            fw.write(i + '\n')
    else:
        print('only text')


'''
noun_list = []
noun_str_list = []

for text in text_list:
    s = pattern_short.findall(text)
    l = pattern_long.findall(text)

    if s:
        #fw.write(text)
        for i1, i2 in zip(s,l):
            temp = kkma.nouns(i1)


            print(l, end='')
            print('\t\t\t', end='')


            for j in range(3, len(temp)):
                print(temp[j] + ' ', end='')
                if temp[j] in noun_list:
                    continue

                noun_list.append(temp[j])

            print('\n')

print(noun_list)
print('\n총 개수 : ' + str(len(noun_list)))
'''

fr.close()
fw.close()
