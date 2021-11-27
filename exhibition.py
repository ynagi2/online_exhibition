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
    st.title("withコロナ時代のライブ新様式")
    texts_dir = "./text/"
    text_files = sorted(os.listdir(texts_dir))
    sections = ("はじめに", "1章 コロナ禍以前・通常のライブ", "2章 コロナ禍の無観客・配信ライブ", "3章　有観客ライブの新様式", "おわりに")
    add_selectbox = st.sidebar.selectbox("章立て", sections)
    chapter = sections.index(add_selectbox)
    show_chapter(texts_dir, text_files, chapter)
    members = ("システム情報工学研究群　社会工学学位プログラム　山田直輝", "人文社会科学研究群　国際日本研究プログラム　接暁岩", "人文社会科学研究群　人文学位プログラム　塩見葵", "人間総合科学研究科　芸術専攻　常包美穂", "システム情報工学研究群　社会工学学位プログラム　山田直輝")
    st.markdown("---")
    member = "文責：" + members[chapter]
    st.markdown(member)
    st.markdown("ページ制作：人間総合科学研究群　情報学学位プログラム　柳田雄輝")
    st.markdown("2021年11月　「人文知コミュニケーション：人文社会科学と自然科学の壁を超える」C班")


if __name__ == '__main__':
    main()