'''
SUML Task 4.1
s18465
'''
import pickle
from datetime import datetime
import streamlit as st

startTime = datetime.now()

FILENAME = "model.sv"
model = pickle.load(open(FILENAME, 'rb'))

pclass_d = {0: "Pierwsza", 1: "Druga", 2: "Trzecia"}
embarked_d = {0: "Cherbourg", 1: "Queenstown", 2: "Southampton"}
sex_d = {0: "Female", 1: "Male"}

IMG_SUCCESS = "https://www.pigeonforgetncabins.com/wp-content/uploads/2015/06/experience-at-titanic-pigeon-forge.jpg"
IMG_FAIL = "https://upload.wikimedia.org/wikipedia/commons/6/6e/St%C3%B6wer_Titanic.jpg"


def main():
    st.set_page_config(page_title="Task 4.1 | s18465")
    overview = st.container()
    left, right = st.columns(2)
    prediction = st.container()

    # st.image("https://upload.wikimedia.org/wikipedia/commons/6/6e/St%C3%B6wer_Titanic.jpg")

    with overview:
        st.title("Task 4.1 - s18465")

    with left:
        sex_radio = st.radio("Płeć", list(sex_d.keys()),format_func=lambda x: sex_d[x])
        embarked_radio = st.radio("Port zaokrętowania", list(embarked_d.keys()), index=2, format_func=lambda x: embarked_d[x])
        pclass_radio = st.radio("Select a class", list(pclass_d.keys()), format_func=lambda x: pclass_d[x])

    with right:
        age_slider = st.slider("Wiek", value=1, min_value=0, max_value=80)
        sibsp_slider = st.slider("Liczba rodzeństwa i/lub partnera", min_value=0, max_value=8)
        parch_slider = st.slider("Liczba rodziców i/lub dzieci", min_value=0, max_value=6)
        fare_slider = st.slider("Cena biletu", min_value=0, max_value=513, step=1)

    data = [[pclass_radio, sex_radio,  age_slider, sibsp_slider, parch_slider, fare_slider, embarked_radio]]
    survival = model.predict(data)
    s_confidence = model.predict_proba(data)

    with prediction:
        st.subheader("Czy taka osoba przeżyłaby katastrofę?")
        st.subheader(("Tak" if survival[0] == 1 else "Nie"))
        st.write("Pewność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100))
        st.image(IMG_SUCCESS if survival[0] == 1 else IMG_FAIL)


if __name__ == "__main__":
    main()
