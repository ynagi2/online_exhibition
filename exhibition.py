import streamlit as st
import os
import re
import base64


def show_chapter(texts_dir, text_files, idx):
    content = ""
    with open(texts_dir + text_files[idx]) as f:
        for line in f:
            if re.search(r'^fig', line):
                st.markdown(content + "\n")
                content = ""
                image_name = line.strip()
                with open("./images/" + image_name + ".png", "rb") as im:
                    image = im.read()
                data_url = base64.b64encode(image).decode("utf-8")
                image_source = '<img src="data:./images/' + image_name + '/png;base64,' + data_url + '\" width="400" style="display: block; margin: auto;">'
                st.markdown(image_source, unsafe_allow_html=True)
            else:
                content += line
    st.markdown(content + "\n")


def main():
    st.title("コロナ禍におけるライブコンサートの変化（仮）")
    texts_dir = "./text/"
    text_files = sorted(os.listdir(texts_dir))
    sections = ("はじめに", "1章 コロナ禍以前・通常のライブ", "2章 コロナ禍の無観客・配信ライブ", "3章 後の対面", "おわりに")
    add_selectbox = st.sidebar.selectbox("章立て", sections)
    show_chapter(texts_dir, text_files, sections.index(add_selectbox))


if __name__ == '__main__':
    main()