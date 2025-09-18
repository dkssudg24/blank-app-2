import streamlit as st

st.title("Streamlit 요소 데모")

st.header("텍스트 요소")
st.write("이것은 일반 텍스트입니다.")
st.markdown("**마크다운** _스타일링_ 지원!")

st.header("입력 요소")
name = st.text_input("이름을 입력하세요:")
age = st.number_input("나이", min_value=0, max_value=120, value=25)
agree = st.checkbox("동의합니다")

st.header("버튼 & 상호작용")
if st.button("인사하기"):
    st.success(f"안녕하세요, {name if name else '방문자'}님!")

st.header("데이터프레임")
import pandas as pd
data = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
st.dataframe(data)

st.header("차트")
st.line_chart(data)

st.header("이미지")
st.image("https://static.streamlit.io/examples/cat.jpg", caption="귀여운 고양이")

st.header("슬라이더")
value = st.slider("값을 선택하세요", 0, 100, 50)
st.write(f"선택한 값: {value}")
