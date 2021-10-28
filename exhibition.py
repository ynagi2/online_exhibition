import streamlit as st
import pandas as pd
from PIL import Image


def main():
    st.title('コロナ禍におけるライブコンサートの変化（仮）')
    # st.table(pd.DataFrame({
    #     'first column': [1, 2, 3, 4],
    #     'second column': [10, 20, 30, 40]
    # }))
    sections = ("はじめに", "1章 コロナ以前", "2章 オンライン", "3章 後の対面", "おわりに")
    add_selectbox = st.sidebar.selectbox("章立て", sections)
    if add_selectbox == "はじめに":
        st.markdown('# はじめに\nhogehoge')
    elif add_selectbox == "1章 コロナ以前":
        concert_tuple = ("あいうえお", "abcde")
        st.markdown("# コロナ以前のはなし\n")
        concert = st.selectbox("知りたい公演", concert_tuple)
        st.write('公演:', concert)
    elif add_selectbox == "2章 オンライン":
        image = Image.open("./job_gakugeiin_woman.png")
        st.image(image, caption="画像はこんな感じ(いらすとや より．実際はちゃんと出典を書きます)")



if __name__ == '__main__':
    main()