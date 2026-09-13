import streamlit as st
import random

st.set_page_config(
    page_title="국어문법 완전정복 (심화)",
    page_icon="📚",
    layout="wide"
)

# ===================================
# 세션 상태 초기화 (퀴즈 점수 저장용)
# ===================================
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'total' not in st.session_state:
    st.session_state.total = 0

# ===================================
# 사이드바 메뉴
# ===================================
st.sidebar.title("📚 목차")
menu = st.sidebar.radio(
    "배우고 싶은 단원을 골라보세요!",
    ["🏠 홈", "1️⃣ 음운론", "2️⃣ 형태론", 
     "3️⃣ 통사론(문장)", "4️⃣ 의미론", "5️⃣ 국어사 (역사)",
     "6️⃣ 어문 규정", "🎯 암기법 총정리", "✏️ 복습 퀴즈"]
)

# ===================================
# 홈 화면
# ===================================
if menu == "🏠 홈":
    st.title("국어문법 완전정복 📚")
    st.write("### 고등학교 2학년까지 배우는 심화 국어문법!")
    st.write("")
    st.info("👈 왼쪽 메뉴에서 배우고 싶은 단원을 골라보세요!")
    
    st.write("---")
    st.write("## 📖 이 앱에서 배울 내용")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("### 1️⃣ 음운론")
        st.write("- 음운 체계")
        st.write("- 음운 변동 심화")
        st.write("- 음운의 축약/탈락")
        
        st.write("### 2️⃣ 형태론")
        st.write("- 형태소 분석")
        st.write("- 품사와 활용")
        st.write("- 단어형성법")
    
    with col2:
        st.write("### 3️⃣ 통사론")
        st.write("- 문장성분 심화")
        st.write("- 문장의 종류")
        st.write("- 높임법/시제/피동사동")
        
        st.write("### 4️⃣ 의미론")
        st.write("- 단어의 의미관계")
        st.write("- 중의성")
    
    with col3:
        st.write("### 5️⃣ 국어사")
        st.write("- 훈민정음")
        st.write("- 중세국어 특징")
        
        st.write("### 6️⃣ 어문 규정")
        st.write("- 맞춤법/표준어")
        st.write("- 로마자/외래어표기")
    
    st.write("---")
    st.write(f"### 📊 현재까지 퀴즈 점수: {st.session_state.score} / {st.session_state.total}")

# ===================================
# 1. 음운론 심화
# ===================================
elif menu == "1️⃣ 음운론":
    st.title("1️⃣ 음운론 (소리의 세계)")
    
    tab1, tab2, tab3, tab4 = st.tabs(["음운 체계", "교체 현상", "축약과 탈락", "첨가 현상"])
    
    with tab1:
        st.header("음운 체계 기초 + 심화")
        st.write("**음운** = 말의 뜻을 구별해주는 소리의 최소 단위")
        st.write("- **분절음운**: 자음, 모음 (쪼갤 수 있음)")
        st.write("- **비분절음운**: 소리의 길이, 억양 (쪼갤 수 없지만 뜻 구별)")
        
        st.success("예: 눈(眼,눈) vs 눈:(雪,눈) → 소리의 길이로 뜻이 달라짐!")
        
        st.subheader("📌 단모음 10개 & 이중모음 11개")
        st.code("단모음: ㅏ ㅐ ㅓ ㅔ ㅗ ㅚ ㅜ ㅟ ㅡ ㅣ")
        st.code("이중모음: ㅑㅕㅛㅠㅒㅖㅘㅙㅝㅞㅢ")
        
        st.warning("🎯 암기법: '아애어에 오외우위 으이' 4글자씩 노래처럼!")
        
        st.subheader("📌 자음 체계표 (조음위치 x 조음방법)")
        cons_data = {
            "조음방법": ["파열음","파찰음","마찰음","비음","유음"],
            "입술소리": ["ㅂㅃㅍ","-","-","ㅁ","-"],
            "잇몸소리": ["ㄷㄸㅌ","-","ㅅㅆ","ㄴ","ㄹ"],
            "센입천장": ["-","ㅈㅉㅊ","-","-","-"],
            "여린입천장": ["ㄱㄲㅋ","-","-","ㅇ","-"],
            "목청소리": ["-","-","ㅎ","-","-"]
        }
        st.table(cons_data)
        st.warning("🎯 암기법: '파파마비유' 조음방법 순서로! '입잇센여목' 위치 순서로!")
    
    with tab2:
        st.header("교체 현상 (한 음운이 다른 음운으로)")
        
        st.subheader("① 음절의 끝소리 규칙")
        st.write("받침이 7개 소리로만 남아요: **ㄱㄴㄷㄹㅁㅂㅇ**")
        st.info("예: 옷[옫], 부엌[부억], 잎[입]")
        st.warning("🎯 암기법: '가나다라마바아' 7형제만!")
        
        st.write("---")
        st.subheader("② 비음화 (자음동화)")
        st.write("받침 **ㄱㄷㅂ** + **ㄴㅁ** → **ㅇㄴㅁ**")
        st.info("예: 국물[궁물], 닫는[단는], 밥물[밤물]")
        st.warning("🎯 암기법: 콧물 나면 코 막힌 소리!")
        
        st.write("---")
        st.subheader("③ 유음화")
        st.write("**ㄴ** + **ㄹ** 또는 **ㄹ** + **ㄴ** → **ㄹㄹ**")
        st.info("예: 신라[실라], 칼날[칼랄]")
        st.warning("🎯 암기법: ㄴ이 ㄹ을 만나면 ㄹ에게 물든다!")
        
        st.write("---")
        st.subheader("④ 구개음화")
        st.write("받침 **ㄷ,ㅌ** + 모음 **'ㅣ'** → **ㅈ,ㅊ**")
        st.info("예: 굳이[구지], 같이[가치], 해돋이[해도지]")
        st.warning("🎯 암기법: ㄷ,ㅌ이 ㅣ를 만나면 부드러워진다!")
        
        st.write("---")
        st.subheader("⑤ 된소리되기(경음화)")
        st.write("받침 **ㄱㄷㅂ** 뒤에서 예사소리 → 된소리")
        st.info("예: 국밥[국빱], 학교[학꾜], 옆집[엽찝]")
        st.warning("🎯 암기법: 강한 받침 뒤엔 강한 소리!")
    
    with tab3:
        st.header("축약과 탈락 (심화)")
        
        st.subheader("① 자음 축약 (거센소리되기)")
        st.write("**ㄱㄷㅂㅈ** + **ㅎ** → **ㅋㅌㅍㅊ** (두 음운이 하나로 합쳐짐)")
        st.info("예: 축하[추카], 좋다[조타], 잡히다[자피다]")
        st.warning("🎯 암기법: ㅎ을 만나면 세게 숨을 내쉰다!")
        
        st.write("---")
        st.subheader("② 모음 축약")
        st.write("두 모음이 합쳐져서 하나의 모음(이중모음)이 됨")
        st.info("예: 보 + 아 = 봐, 가지어 = 가져")
        
        st.write("---")
        st.subheader("③ 자음 탈락")
        st.write("받침 **ㄹ,ㅎ** 등이 특정 조건에서 사라짐")
        st.info("예: 딸 + 님 = 따님(ㄹ탈락), 좋은[조은](ㅎ탈락)")
        st.warning("🎯 암기법: ㄹ,ㅎ은 힘이 약해서 잘 떨어진다!")
        
        st.write("---")
        st.subheader("④ 모음 탈락")
        st.write("같은 모음이나 비슷한 모음이 만나면 하나가 사라짐")
        st.info("예: 가 + 아서 = 가서, 서 + 어서 = 서서")
    
    with tab4:
        st.header("첨가 현상")
        
        st.subheader("ㄴ 첨가")
        st.write("합성어에서 앞말 받침 + 뒷말 '이,야,여,요,유' 만나면 **ㄴ**이 추가됨")
        st.info("예: 솜 + 이불 = [솜니불], 색 + 연필 = [생년필]")
        st.warning("🎯 암기법: 모음 앞에 몰래 ㄴ이 끼어든다!")

# ===================================
# 2. 형태론 심화
# ===================================
elif menu == "2️⃣ 형태론":
    st.title("2️⃣ 형태론 (단어의 세계)")
    
    tab1, tab2, tab3, tab4 = st.tabs(["형태소 분석", "품사와 활용", "단어형성법", "용언의 활용"])
    
    with tab1:
        st.header("형태소란?")
        st.write("**형태소** = 뜻을 가진 가장 작은 단위")
        
        st.success("예: '하늘이 참 맑았다' → 하늘/이/참/맑-/-았-/-다")
        
        col1, col2 = st.columns(2)
        with col1:
            st.info("**자립형태소**: 혼자 쓰임 (하늘)")
            st.info("**의존형태소**: 기대야함 (이,맑-,-았-,-다)")
        with col2:
            st.info("**실질형태소**: 실제뜻 있음 (하늘,맑-)")
            st.info("**형식형태소**: 문법역할만 (이,-았-,-다)")
        
        st.warning("🎯 암기법: 혼자면 자립, 기대면 의존! 뜻있으면 실질, 문법만하면 형식!")
    
    with tab2:
        st.header("품사 9가지 + 심화")
        
        st.warning("🎯 암기법: '명대수관부 조동형감'")
        
        pos_data = {
            "번호": [1,2,3,4,5,6,7,8,9],
            "품사": ["명사","대명사","수사","관형사","부사","조사","동사","형용사","감탄사"],
            "특징": ["체언,불변","체언,불변","체언,불변","수식언,불변","수식언,불변","관계언,불변(서술격제외)","용언,가변","용언,가변","독립언,불변"],
        }
        st.table(pos_data)
        
        st.subheader("📌 심화: 조사의 종류")
        st.write("- **격조사**: 문장성분 자격 부여 (이/가, 을/를, 의)")
        st.write("- **접속조사**: 단어 연결 (와/과, 하고)")
        st.write("- **보조사**: 특별한 뜻 더함 (은/는, 도, 만)")
        st.warning("🎯 암기법: 격조사는 자격증, 접속조사는 접착제, 보조사는 특별양념!")
        
        st.subheader("📌 심화: 어미의 종류")
        st.write("- **어말어미**: 단어 끝에 옴 (종결,연결,전성)")
        st.write("- **선어말어미**: 어간과 어말어미 사이 (-시-,-았-,-겠-)")
        st.warning("🎯 암기법: 선어말은 중간에 끼어드는 얌체!")
    
    with tab3:
        st.header("단어형성법")
        
        col1, col2 = st.columns(2)
        with col1:
            st.success("**합성어** (어근+어근)")
            st.write("밤나무 = 밤+나무")
            st.write("논밭 = 논+밭")
        with col2:
            st.success("**파생어** (어근+접사)")
            st.write("풋사과 = 풋(접두사)+사과")
            st.write("먹이 = 먹(어근)+이(접미사)")
        
        st.warning("🎯 암기법: 합성은 단어끼리 합체! 파생은 접사가 붙어서 파생!")
        
        st.subheader("📌 심화: 합성어의 종류")
        st.write("- **통사적 합성어**: 우리말 문장구조와 같음 (예: 힘들다)")
        st.write("- **비통사적 합성어**: 문장구조와 다름 (예: 덮밥=덮다+밥, 어간+명사 직결)")
        st.warning("🎯 암기법: 통사적은 정상, 비통사적은 특이 케이스!")
    
    with tab4:
        st.header("용언의 활용 (심화)")
        
        st.write("**어간**(뜻 담당, 안 변함) + **어미**(문법기능, 변함)")
        st.success("예: 먹다 → 먹-(어간) + -다(어미)")
        st.write("먹고, 먹으니, 먹어서 → 어간 '먹-'은 그대로!")
        
        st.subheader("📌 규칙활용 vs 불규칙활용")
        col1, col2 = st.columns(2)
        with col1:
            st.info("**규칙활용**: 어간,어미 형태 안변함(먹다)")
        with col2:
            st.info("**불규칙활용**: 형태가 변함")
            st.write("- ㄷ불규칙: 듣다→들어서")
            st.write("- ㅂ불규칙: 눕다→누워서")
            st.write("- 르불규칙: 흐르다→흘러서")
        st.warning("🎯 암기법: 이유없이 변하면 불규칙!")

# ===================================
# 3. 통사론 (문장) 심화
# ===================================
elif menu == "3️⃣ 통사론(문장)":
    st.title("3️⃣ 통사론 (문장의 세계)")
    
    tab1, tab2, tab3, tab4 = st.tabs(["문장성분", "문장의 짜임", "높임법", "시제/피동사동"])
    
    with tab1:
        st.header("문장 성분 7가지")
        st.warning("🎯 암기법: '주서목보관독'")
        
        sentence_data = {
            "성분":["주어","서술어","목적어","보어","관형어","부사어","독립어"],
            "역할":["누가","어찌한다","무엇을","되다/아니다 앞","체언꾸밈","용언꾸밈","홀로쓰임"],
            "예문":["철수가 밥을 먹는다","철수가 밥을 먹는다","철수가 밥을 먹는다",
                    "철수가 의사가 되었다","새 옷을 입었다","빨리 뛰었다","아, 예쁘다!"]
        }
        st.table(sentence_data)
        
        st.subheader("📌 심화: 필수 성분 vs 수의 성분")
        st.write("- **필수성분**: 주어,서술어,목적어,보어,필수부사어")
        st.write("- **수의성분**: 관형어,부사어(일반적),독립어")
        st.warning("🎯 암기법: 없으면 문장이 이상해지면 필수, 없어도 괜찮으면 수의!")
    
    with tab2:
        st.header("문장의 짜임")
        
        col1, col2 = st.columns(2)
        with col1:
            st.success("**홑문장**: 주어+서술어 1번")
        with col2:
            st.success("**겹문장**: 주어+서술어 2번↑")
        
        st.subheader("이어진 문장")
        st.info("**대등**: -고,-며,-지만 (동급 연결)")
        st.write("예: 나는 밥을 먹고, 너는 빵을 먹는다")
        st.info("**종속**: -면,-니까,-러 (하나가 딸림)")
        st.write("예: 비가 오면 우산을 써라")
        
        st.subheader("안은 문장 5가지")
        st.warning("🎯 암기법: '명관부서인'")
        clause_data = {
            "종류":["명사절","관형절","부사절","서술절","인용절"],
            "특징":["-음,-기","-는,-(으)ㄴ","-게,-이","주어+서술어","-고,-라고"],
            "예문":["그가 오기를 기다린다","내가 읽은 책","소리도 없이 사라졌다",
                    "코끼리는 코가 길다","그녀는 간다고 말했다"]
        }
        st.table(clause_data)
    
    with tab3:
        st.header("높임법 (심화)")
        
        st.subheader("① 주체높임법")
        st.write("문장의 **주어**를 높임 (-시-, 조사'께서')")
        st.info("예: 할아버지께서 오신다")
        
        st.subheader("② 객체높임법")
        st.write("문장의 **목적어,부사어**를 높임 (드리다,모시다,여쭙다)")
        st.info("예: 나는 할머니를 모시고 간다")
        
        st.subheader("③ 상대높임법")
        st.write("**듣는 사람(청자)**을 높임 (종결어미로 표현)")
        st.info("예: 합니다(높임) vs 한다(낮춤)")
        
        st.warning("🎯 암기법: 주체는 문장주인, 객체는 문장속손님, 상대는 듣는사람!")
    
    with tab4:
        st.header("시제 & 피동/사동")
        
        st.subheader("📌 시제")
        col1,col2,col3 = st.columns(3)
        with col1:
            st.info("**과거**: -았/었-")
            st.write("먹었다")
        with col2:
            st.info("**현재**: -는/ㄴ-")
            st.write("먹는다")
        with col3:
            st.info("**미래**: -겠-,-리-")
            st.write("먹겠다")
        
        st.write("---")
        st.subheader("📌 피동 vs 사동")
        
        col1, col2 = st.columns(2)
        with col1:
            st.success("**피동**: 남에 의해 당함")
            st.write("먹다 → 먹히다")
            st.write("(-이,-히,-리,-기- 붙임)")
        with col2:
            st.success("**사동**: 남에게 시킴")
            st.write("먹다 → 먹이다")
            st.write("(-이,-히,-리,-기,-우- 붙임)")
        
        st.warning("🎯 암기법: 피동은 당하는것(피해자), 사동은 시키는것(사장님)!")

# ===================================
# 4. 의미론
# ===================================
elif menu == "4️⃣ 의미론":
    st.title("4️⃣ 의미론 (단어의 의미)")
    
    tab1, tab2 = st.tabs(["단어의 의미관계", "중의성"])
    
    with tab1:
        st.header("단어의 의미 관계")
        
        col1, col2 = st.columns(2)
        with col1:
            st.info("**유의관계**: 뜻이 비슷함")
            st.write("예: 기쁘다 - 즐겁다")
            
            st.info("**반의관계**: 뜻이 반대")
            st.write("예: 크다 - 작다")
        
        with col2:
            st.info("**상하관계**: 포함관계")
            st.write("예: 동물(상위) - 개(하위)")
            
            st.info("**다의어 vs 동음이의어**")
            st.write("다의어: 눈(신체)-눈(관찰력) 관련있음")
            st.write("동음이의어: 배(신체)-배(과일) 관련없음")
        
        st.warning("🎯 암기법: 다의어는 뜻이 가족, 동음이의어는 남남!")
    
    with tab2:
        st.header("문장의 중의성")
        st.write("한 문장이 여러 뜻으로 해석되는 것")
        
        st.info("예: '나는 철수와 영희를 만났다'")
        st.write("→ 해석1: 나 + 철수와영희(2명)를 만남")
        st.write("→ 해석2: 나와철수(함께) + 영희를 만남")
        
        st.warning("🎯 암기법: 중의성은 문장이 여러 안경을 쓴 것!")

# ===================================
# 5. 국어사
# ===================================
elif menu == "5️⃣ 국어사 (역사)":
    st.title("5️⃣ 국어의 역사")
    
    tab1, tab2 = st.tabs(["훈민정음", "중세국어 특징"])
    
    with tab1:
        st.header("훈민정음")
        st.write("**세종대왕**이 1443년 창제, 1446년 반포")
        
        st.subheader("창제 원리")
        st.write("- **자음**: 발음기관의 모양을 본뜸 (상형)")
        st.write("- **모음**: 하늘(ㆍ),땅(ㅡ),사람(ㅣ) 을 본뜸")
        
        st.info("예: ㄱ(어금닛소리)=혀뿌리가 목구멍을 막는 모양")
        
        st.warning("🎯 암기법: 자음은 입모양 따라 그리기, 모음은 하늘땅사람!")
    
    with tab2:
        st.header("중세국어 특징")
        st.write("- **성조**(소리 높낮이) 존재: 방점으로 표시")
        st.write("- 사라진 글자: ㆍ(아래아), ㅿ(반치음), ㆆ(여린히읗)")
        st.write("- 두음법칙 없음: 녀자(여자X), 니르다(이르다X)")
        
        st.warning("🎯 암기법: 옛날엔 지금 없는 소리와 글자가 있었다!")

# ===================================
# 6. 어문 규정
# ===================================
elif menu == "6️⃣ 어문 규정":
    st.title("6️⃣ 어문 규정")
    
    tab1, tab2, tab3 = st.tabs(["맞춤법", "표준어", "로마자/외래어"])
    
    with tab1:
        st.header("한글 맞춤법")
        st.write("표준어를 **소리대로** 적되, **어법에 맞도록**")
        st.warning("🎯 암기법: 소리대로! 하지만 뜻이 통하게!")
        
        st.subheader("헷갈리는 맞춤법")
        col1, col2 = st.columns(2)
        with col1:
            st.error("몇일 / 오랫만에 / 안되")
        with col2:
            st.success("며칠 / 오랜만에 / 안돼")
        
        st.info("💡 되/돼 구별법: '해'로 바꿔서 자연스러우면 '돼'!")
        
        st.subheader("띄어쓰기")
        st.write("**조사는 붙이고, 나머지는 띄어쓴다**")
        st.warning("🎯 암기법: 조사는 껌딱지처럼 붙는다!")
    
    with tab2:
        st.header("표준어 규정")
        st.write("교양있는 사람들이 두루 쓰는 **현대 서울말**")
        
        st.info("예: 강남콩(X) → 강낭콩(O)")
        st.info("예: 웃어른(O), 윗어른(X) - 위아래 대립없으면 '웃'")
    
    with tab3:
        st.header("로마자 표기법 & 외래어 표기법")
        
        st.write("**로마자 표기**: 표준발음법에 따라 적음")
        st.info("예: 종로 → Jongno (발음대로!)")
        
        st.write("**외래어 표기**: 이미 정해진 표기법 따름")
        st.info("예: file → 파일(O), 화일(X)")

# ===================================
# 암기법 총정리
# ===================================
elif menu == "🎯 암기법 총정리":
    st.title("🎯 암기법 총정리")
    st.write("### 시험 전날 한눈에 복습하기!")
    
    memo_list = [
        ("모음", "아애어에 오외우위 으이"),
        ("자음 조음방법", "파파마비유"),
        ("품사 9가지", "명대수관부 조동형감"),
        ("문장 성분", "주서목보관독"),
        ("안은 문장", "명관부서인"),
        ("비음화", "콧물 나면 콧소리"),
        ("유음화", "ㄴ이 ㄹ에게 물든다"),
        ("구개음화", "ㅣ 만나면 부드러워짐"),
        ("자음축약", "ㅎ 만나면 세게 숨쉰다"),
        ("높임법", "주체=주인,객체=손님,상대=듣는이"),
        ("피동/사동", "피동=당함,사동=시킴"),
        ("되/돼", "'해'로 바꿔서 되면 '돼'"),
        ("띄어쓰기", "조사는 껌딱지"),
        ("다의어/동음이의어", "다의어=가족,동음이의어=남남"),
    ]
    
    for title, memo in memo_list:
        st.success(f"**{title}**: {memo}")
    
    st.balloons()

# ===================================
# 복습 퀴즈
# ===================================
elif menu == "✏️ 복습 퀴즈":
    st.title("✏️ 국어문법 복습 퀴즈")
    st.write("### 배운 내용을 퀴즈로 확인해봐요!")
    
    quiz_data = [
        {
            "question": "다음 중 단모음이 아닌 것은?",
            "options": ["ㅏ", "ㅑ", "ㅗ", "ㅣ"],
            "answer": "ㅑ",
            "explain": "ㅑ는 이중모음이에요! 단모음은 ㅏㅐㅓㅔㅗㅚㅜㅟㅡㅣ 10개!"
        },
        {
            "question": "'국물'의 올바른 발음은?",
            "options": ["[국물]", "[궁물]", "[구물]", "[국믈]"],
            "answer": "[궁물]",
            "explain": "비음화 현상! ㄱ받침+ㅁ 만나면 ㄱ→ㅇ으로 변해요!"
        },
        {
            "question": "다음 중 파생어는?",
            "options": ["밤나무", "풋사과", "논밭", "손발"],
            "answer": "풋사과",
            "explain": "풋(접두사)+사과(어근) = 파생어! 나머지는 어근+어근인 합성어예요!"
        },
        {
            "question": "'철수가 밥을 먹는다'에서 '밥을'의 문장성분은?",
            "options": ["주어", "목적어", "보어", "서술어"],
            "answer": "목적어",
            "explain": "'~을/를'이 붙으면 목적어! '무엇을' 먹는지 나타내요!"
        },
        {
            "question": "'그가 오기를 기다린다'에서 안긴 문장의 종류는?",
            "options": ["관형절", "부사절", "명사절", "서술절"],
            "answer": "명사절",
            "explain": "'-기'가 붙으면 명사절! '오기'가 명사처럼 쓰였어요!"
        },
        {
            "question": "다음 중 맞춤법이 옳은 것은?",
            "options": ["몇일", "며칠", "멷일", "몇일"],
            "answer": "며칠",
            "explain": "'몇일'은 틀린 표기! '며칠'이 표준어예요!"
        },
        {
            "question": "'할아버지께서 오신다'는 어떤 높임법인가?",
            "options": ["객체높임", "주체높임", "상대높임", "모두해당"],
            "answer": "주체높임",
            "explain": "'-시-'와 '께서'는 문장의 주어(할아버지)를 높이는 주체높임법!"
        },
        {
            "question": "'먹다→먹히다'는 무엇에 해당하는가?",
            "options": ["사동", "피동", "높임", "시제"],
            "answer": "피동",
            "explain": "'-히-'가 붙어서 남에게 당하는 뜻이 되면 피동!"
        },
        {
            "question": "훈민정음의 자음은 무엇을 본떠 만들었는가?",
            "options": ["동물모양", "발음기관모양", "글자모양", "자연현상"],
            "answer": "발음기관모양",
            "explain": "자음은 발음기관(혀,입술 등)의 모양을 상형해서 만들었어요!"
        },
        {
            "question": "'국밥'의 올바른 발음은?",
            "options": ["[국밥]", "[국빱]", "[구밥]", "[궁밥]"],
            "answer": "[국빱]",
            "explain": "된소리되기 현상! ㄱ받침 뒤에서 예사소리가 된소리로 변해요!"
        }
    ]
    
    # 퀴즈 순서를 섞어서 보여주기
    if 'quiz_order' not in st.session_state:
        st.session_state.quiz_order = list(range(len(quiz_data)))
        random.shuffle(st.session_state.quiz_order)
    
    if 'quiz_index' not in st.session_state:
        st.session_state.quiz_index = 0
    
    if 'answered' not in st.session_state:
        st.session_state.answered = False
    
    # 진행 상황 표시
    progress = st.session_state.quiz_index / len(quiz_data)
    st.progress(progress)
    st.write(f"**진행: {st.session_state.quiz_index} / {len(quiz_data)}**")
    
    if st.session_state.quiz_index < len(quiz_data):
        current_q = quiz_data[st.session_state.quiz_order[st.session_state.quiz_index]]
        
        st.write("---")
        st.subheader(f"Q{st.session_state.quiz_index + 1}. {current_q['question']}")
        
        selected = st.radio("답을 골라보세요:", current_q['options'], key=f"q_{st.session_state.quiz_index}")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ 정답 확인", key=f"check_{st.session_state.quiz_index}"):
                st.session_state.answered = True
                st.session_state.total += 1
                if selected == current_q['answer']:
                    st.session_state.score += 1
                    st.success(f"🎉 정답이에요! {current_q['explain']}")
                else:
                    st.error(f"❌ 틀렸어요. 정답은 '{current_q['answer']}'입니다.")
                    st.info(current_q['explain'])
        
        with col2:
            if st.session_state.answered:
                if st.button("➡️ 다음 문제", key=f"next_{st.session_state.quiz_index}"):
                    st.session_state.quiz_index += 1
                    st.session_state.answered = False
                    st.rerun()
    
    else:
        st.write("---")
        st.balloons()
        st.title("🎊 퀴즈 완료!")
        
        percentage = (st.session_state.score / st.session_state.total) * 100 if st.session_state.total > 0 else 0
        
        st.write(f"### 최종 점수: {st.session_state.score} / {st.session_state.total} ({percentage:.0f}점)")
        
        if percentage >= 80:
            st.success("🏆 훌륭해요! 국어문법 마스터!")
        elif percentage >= 60:
            st.info("👍 잘했어요! 조금만 더 복습하면 완벽해요!")
        else:
            st.warning("💪 다시 한번 복습해볼까요? 할 수 있어요!")
        
        if st.button("🔄 퀴즈 다시 풀기"):
            st.session_state.quiz_index = 0
            st.session_state.answered = False
            st.session_state.score = 0
            st.session_state.total = 0
            st.session_state.quiz_order = list(range(len(quiz_data)))
            random.shuffle(st.session_state.quiz_order)
            st.rerun()
