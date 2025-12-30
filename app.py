import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="자리 이동 방지 시스템",
    layout="wide"
)

CSV_FILE = "seats.csv"

# CSV 불러오기
df = pd.read_csv(CSV_FILE)

st.title("📌 자리 이동 방지 시스템")
st.write("자리를 이동한 학생의 좌석을 클릭하세요")

# 분단별 줄 수 (네가 말한 조건 그대로)
section_rows = {
    1: 5,
    2: 6,
    3: 5
}

# 분단별 출력
for section in [1, 2, 3]:
    st.subheader(f"{section}분단")

    max_rows = section_rows[section]

    for row in range(1, max_rows + 1):
        cols = st.columns(2)

        for i in range(2):
            seat_id = f"{section}-{row}-{i+1}"

            seat = df[df["seat_id"] == seat_id]
            if seat.empty:
                continue

            name = seat.iloc[0]["name"]
            blocked = seat.iloc[0]["blocked"]

            # 표시용 아이콘
            label = f"🔴 {name}" if blocked == 1 else f"⚪ {name}"

            if cols[i].button(label, key=seat_id):
                df.loc[df["seat_id"] == seat_id, "blocked"] = 1
                df.to_csv(CSV_FILE, index=False)
                st.rerun()
