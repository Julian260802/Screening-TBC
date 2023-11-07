import streamlit as st

def main():
    st.title("Aplikasi Skrining TBC")
    st.write("Silakan jawab beberapa pertanyaan untuk menentukan Indikasi Anda terkena TBC.")

    answer1 = st.selectbox("1. Apakah Anda saat ini sedang batuk lebih dari 2 minggu?", ("Ya", "Tidak"))
    answer2 = st.selectbox("2. Apakah Anda pernah mengidap TBC sebelumnya?", ("Ya", "Tidak"))
    answer3 = st.selectbox("3. Apakah Anda mengalami demam lebih dari 2 minggu?", ("Ya", "Tidak"))
    answer4 = st.selectbox("4. Apakah Anda mengalami turunnya berat badan yang drastis?", ("Ya", "Tidak"))
    answer5 = st.selectbox("5. Apakah Anda berkeringat di malam hari tanpa sebab?", ("Ya", "Tidak"))

    result = tbc_screening(answer1, answer2, answer3, answer4, answer5)

    if "Terkonfirmasi TBC" in result:
        st.error(f"Hasil Skrining TBC: {result}")
    else:
        st.success(f"Hasil Skrining TBC: {result}")

def tbc_screening(answer1, answer2, answer3, answer4, answer5):
    if answer1 == "Ya" and answer2 == "Ya" and answer3 == "Ya" and answer4 == "Ya" and answer5 == "Ya":
        return "Terkonfirmasi TBC"
    else:
        return "Tidak Terkonfirmasi TBC"

if __name__ == "__main__":
    main()
