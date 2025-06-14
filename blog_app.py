import streamlit as st
import plotly.express as px
import altair as alt
import pandas as pd

# 사이드바 요약 정보
st.sidebar.title("🧾 경영학도 염지호의 요약 정보")
st.sidebar.text("안녕하세요. 통계와 빅데이터 분석으로 리스크를 관리하는 예비전문가 염지호입니다.")
st.sidebar.markdown("**전공:** 경영학과  \n**관심:** 금융, 회계, 빅데이터")
st.sidebar.divider()



#응원해주세요!!
st.image("assets/profile.jpg", caption="지호의 이미지")
if st.button("염지호를 응원해주세요! 🙌"):
    st.write("정말 감사합니다! 🙇‍♂️")
st.caption("아이고야 힘들다")
st.divider()



# 프로필 섹션
st.title("염지호 | 경영학 전공 이력서 📄")
st.markdown("**홍익대학교 경영대학 경영학과 (B831158)**")
st.markdown("**졸업예정: 2026년 2월**")
st.text("나이: 26세")
st.text("병역사항: 대한민국 육군 병장 만기전역")
st.divider()


# 자격사항 섹션
st.header("📚 보유 자격증")
st.subheader("자격증 및 어학 점수 현황")
st.markdown("- 공인회계사(CPA)")
st.markdown("- 투자관리운용사")
st.markdown("- 재경관리사")
st.markdown("- TOEIC: 890점")
st.divider()


# 희망 진로 섹션
st.header("💼 희망 진로")
st.subheader("관심 있는 직무")
st.markdown("- 금융공기업 경제직렬 조사역")
st.markdown("- 은행권 채권운용역")
st.markdown("- 금융사 자산운용역")



career_labels = ["금융공기업 조사역", "은행권 채권운영역", "금융사 자산운용역"]
career_values = [60, 30, 10]  # 비율은 예시입니다. 원하시면 조정 가능해요

fig = px.pie(
    names=career_labels,
    values=career_values,
    title="염지호의 희망 진로 선호도",
    color_discrete_sequence=px.colors.sequential.RdBu
)

st.header("📈 희망 진로 선호도")
st.plotly_chart(fig)
st.divider()




# 관심 분야 섹션
st.header("📊 관심 분야")
st.subheader("주요 관심 분야 및 학습내용")
interests = [
    "통계학", "빅데이터", "리스크 관리",
    "재무회계", "재무관리", "세무관리", "원가관리",
    "파이썬프로그래밍","R-프로그래밍","계량경제학"
]
for item in interests:
    st.markdown(f"- {item}")
st.divider()


st.header("💡 기술 역량 분포")
skill_data = pd.DataFrame({
    '기술': ['Python', 'R-프로그래밍', 'Excel 분석', 'Java'],
    '역량 점수': [60, 70, 80, 20]
})

bar_chart = alt.Chart(skill_data).mark_bar(color='steelblue').encode(
    x='기술',
    y='역량 점수'
).properties(
    title='염지호의 기술 역량 분포'
)

st.altair_chart(bar_chart, use_container_width=True)
st.divider()



# 엑셀, R-프로그래밍으로 회귀분석 포트폴리오  섹션
st.header("📂 엑셀·R-프로그래밍으로 진행한 회귀분석 포트폴리오")
st.caption("연습용 데이터 WAGE2.csv를 이용하여 아이큐와 교육연수가 임금에 미치는 영향을 회귀분석해보겠습니다.")

st.subheader("1번: 엑셀을 이용하여 회귀분석하기")
st.markdown("##### 📊 WAGE2 데이터 미리보기")
df = pd.read_csv("assets/WAGE2.csv")
subset_df = pd.concat([df.head(5), df.tail(1)])
st.dataframe(subset_df)
st.markdown("##### 📈 회귀분석 결과 (엑셀 출력)")
st.image("assets/엑셀회귀분석데이터.png", caption="WAGE2.csv 회귀분석 요약결과 (엑셀)")
"""
:blue[IQ와 educ의 p-값이 모두 무시할 정도로 작다. 따라서 IQ와 educ는 모두 wage에 통계적으로 유의미한 영향을 끼친다.]
"""

st.subheader("2번: R-프로그래밍으로 회귀분석하기")
st.markdown("##### 회귀식 작성하기")
st.latex(r"\text{wage} = \beta_0 + \beta_1 \cdot IQ_i + \beta_2 \cdot educ_i + \varepsilon")
st.markdown("##### 두 개의 산포도 그림")
st.markdown("- 종속변수: **wage**, 독립변수: **IQ**")
st.markdown("- 종속변수: **wage**, 독립변수: **educ**")
st.markdown("##### R-프로그래밍으로 다중회귀분석 진행하기")
st.code("""
# WAGE2.csv 불러오기
wage_data <- read.csv("WAGE2.csv")

# 다중회귀분석 실행
reg_model <- lm(wage ~ IQ + educ, data = wage_data)

# 결과 출력
summary(reg_model)
""", language='r')

# 스카웃 제의하기  섹션
st.header("💌 스카웃 제의하기")
st.subheader("방문해주셔서 감사합니다. 제안하실 연봉을 입력해주세요.")

salary = st.slider("연봉 제안 (만원 단위)", 2000, 8000, 4000)
st.write(f"💰 제안하신 연봉: {salary}만원")

company = st.text_input("귀사의 사명을 알려주세요:")
email = st.text_input("담당자님의 이메일을 알려주세요:")

if email and ("@" not in email or ".com" not in email):
    st.warning("이메일 형식에 맞지 않습니다.")
    st.error("형식에 맞지 않은 이메일, 다시 확인해주세요")
elif company and email:
    st.success(f"📨 {company}담당자님 제안주셔서 감사합니다. 담당자님 이메일 확인: {email}")
