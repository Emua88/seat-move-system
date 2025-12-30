import streamlit as st
import pandas as pd

st.set_page_config(page_title="자리 이동 방지 시스템", layout="wide")

CSV_FILE = "seats.csv"

# CSV 불러오기
df = pd.read_csv(CSV_FILE)

st.title("📌 자리 이동 방지 시스템")
st.write("자리를 이동한 학생의 좌석을 클릭하세요 (다시 누르면 취소)")

# ===============================
# 교실 구조 설정
# ===============================
# 실제 책상 대형처럼:
# [1분단]   [2분단]   [3분단]
# 1·3분단: 5줄 / 2분단: 6줄
rows_by_section = [5, 6, 5]

# 전체 교실을 가로로 배치
classroom_cols = st.columns(3)

for section_index in range(3):
    with classroom_cols[section_index]:
        max_rows = rows_by_section[section_index]

        for row in range(1, max_rows + 1):
            seat_cols = st.columns(2)

            for seat_num in range(2):
                seat_id = f"{section_index + 1}-{row}-{seat_num + 1}"

                seat_data = df[df["seat_id"] == seat_id]
                if seat_data.empty:
                    continue

                name = seat_data.iloc[0]["name"]
                blocked = seat_data.iloc[0]["blocked"]

                # 버튼 표시
                label = f"🔴 {name}" if blocked == 1 else f"⚪ {name}"

                if seat_cols[seat_num].button(label, key=seat_id):
                    # 🔁 토글 (0 ↔ 1)
                    new_value = 0 if blocked == 1 else 1
                    df.loc[df["seat_id"] == seat_id, "blocked"] = new_value
                    df.to_csv(CSV_FILE, index=False)
                    st.rerun()

            if cols[i].button(label, key=seat_id):
                df.loc[df["seat_id"] == seat_id, "blocked"] = 1
                df.to_csv(CSV_FILE, index=False)
                st.rerun()
