import streamlit as st
from PIL import Image

def main():
    st.header("My art")

    video_file_path = "D:\som\som.mp4.mp4"
    st.video(video_file_path)

    html_content = """
        <div style='text-align: center;'>
            <h5>Video Art</h5>
    """
    st.write(html_content, unsafe_allow_html=True)

    st.markdown(" ")
    tab1, tab2, tab3, tab4, tab5, tab6, tab7= st.tabs(["All Show","Jiab Prachakul", "Alex Face", "Vincent van Gogh", "ไอซ์-รัตตา อนันต์ภาดา", "Peakkyboo", "Give me museums"])

    st.markdown(" ")
    with tab1:
        st.subheader("All Album")
        st.markdown(" ")
        col1, col2, col3 = st.columns(3)

        original1 = Image.open("Alex02.jpg")
        col1.image(original1, caption="Alex Face", use_column_width=True)

        original2 = Image.open("van09.jpg")
        col2.image(original2, caption="Vincent van Gogh", use_column_width=True)

        original3 = Image.open("p02.jpg")
        col3.image(original3, caption="Peakkyboo", use_column_width=True)

        col4, col5, col6 = st.columns(3)

        col4.markdown(" ")
        
        original4 = Image.open("jiab05.webp")
        col4.image(original4, caption="Jiab Prachakul", use_column_width=True)

        col5.markdown(" ")

        original5 = Image.open("ai04.jpg")
        col5.image(original5, caption="ไอซ์-รัตตา อนันต์ภาดา", use_column_width=True)

        col6.markdown(" ")

        original6 = Image.open("g12.jpg")
        col6.image(original6, caption="Give me museums", use_column_width=True)

        col7, col8, col9 = st.columns(3)

        col7.markdown(" ")
        
        original7 = Image.open("Alex08.webp")
        col7.image(original7, caption="Alex Face", use_column_width=True)

        col8.markdown(" ")

        original8 = Image.open("van10.webp")
        col8.image(original8, caption="Vincent van Gogh", use_column_width=True)

        col9.markdown(" ")

        original9 = Image.open("p04.jpg")
        col9.image(original9, caption="Peakkyboo", use_column_width=True)

        col10, col11, col12 = st.columns(3)

        col10.markdown(" ")
        
        original10 = Image.open("jiab04.jpg")
        col10.image(original10, caption="Jiab Prachakul", use_column_width=True)

        col11.markdown(" ")

        original11 = Image.open("ai01.webp")
        col11.image(original11, caption="ไอซ์-รัตตา อนันต์ภาดา", use_column_width=True)

        col12.markdown(" ")

        original12 = Image.open("g10.jpeg")
        col12.image(original12, caption="Give me museums", use_column_width=True)
        
    with tab2:
        st.subheader("Artist: Jiab Prachakul")
        st.markdown(" ")
        col1, col2, col3 = st.columns(3)

        original1 = Image.open("jiab01.webp")
        col1.image(original1, caption="Jiab Prachakul", use_column_width=True)

        original2 = Image.open("jiab08.jpg")
        col2.image(original2, caption="Jiab Prachakul", use_column_width=True)

        original3 = Image.open("jiab07.webp")
        col3.image(original3, caption="Jiab Prachakul", use_column_width=True)

        col4, col5, col6 = st.columns(3)

        col4.markdown(" ")
        
        original4 = Image.open("jiab05.webp")
        col4.image(original4, caption="Jiab Prachakul", use_column_width=True)

        col5.markdown(" ")

        original5 = Image.open("jiab06.webp")
        col5.image(original5, caption="Jiab Prachakul", use_column_width=True)

        col6.markdown(" ")

        original5 = Image.open("jiab04.jpg")
        col6.image(original5, caption="Jiab Prachakul", use_column_width=True)

        col7, col8, col9 = st.columns(3)

        col7.markdown(" ")
        
        original7 = Image.open("jiab02.webp")
        col7.image(original7, caption="Jiab Prachakul", use_column_width=True)

        col8.markdown(" ")

        original8 = Image.open("jiab03.jpg")
        col8.image(original8, caption="Jiab Prachakul", use_column_width=True)

        col9.markdown(" ")

        original9 = Image.open("jiab01.webp")
        col9.image(original9, caption="Jiab Prachakul", use_column_width=True)


    with tab3:
        st.subheader("Artist: Alex Face")
        st.markdown(" ")
        col1, col2, col3 = st.columns(3)

        original1 = Image.open("Alex11.jpg")
        col1.image(original1, caption="Alex Face", use_column_width=True)


        original2 = Image.open("Alex10.webp")
        col2.image(original2, caption="Alex Face", use_column_width=True)

        original3 = Image.open("Alex12.jpg")
        col3.image(original3, caption="Alex Face", use_column_width=True)

        col4, col5, col6 = st.columns(3)

        col4.markdown(" ")
        
        original4 = Image.open("Alex09.webp")
        col4.image(original4, caption="Alex Face", use_column_width=True)

        col5.markdown(" ")

        original5 = Image.open("Alex01.jpg")
        col5.image(original5, caption="Alex Face", use_column_width=True)

        col6.markdown(" ")

        original5 = Image.open("Alex03.jpg")
        col6.image(original5, caption="Alex Face", use_column_width=True)

        col7, col8, col9 = st.columns(3)

        col7.markdown(" ")
        
        original7 = Image.open("Alex06.png")
        col7.image(original7, caption="Alex Face", use_column_width=True)

        col8.markdown(" ")

        original8 = Image.open("Alex09.webp")
        col8.image(original8, caption="Alex Face", use_column_width=True)

        col9.markdown(" ")

        original9 = Image.open("Alex08.webp")
        col9.image(original9, caption="Alex Face", use_column_width=True)

    with tab4:
        st.subheader("Artist: Vincent van Gogh")
        st.markdown(" ")
        col1, col2, col3 = st.columns(3)

        original1 = Image.open("van10.webp")
        col1.image(original1, caption="Vincent van Gogh", use_column_width=True)

        original2 = Image.open("van09.jpg")
        col2.image(original2, caption="Vincent van Gogh", use_column_width=True)

        original3 = Image.open("van06.jpg")
        col3.image(original3, caption="Vincent van Gogh", use_column_width=True)

        col4, col5, col6 = st.columns(3)

        col4.markdown(" ")
        
        original4 = Image.open("van11.jpg")
        col4.image(original4, caption="Vincent van Gogh", use_column_width=True)

        col5.markdown(" ")

        original5 = Image.open("van05.webp")
        col5.image(original5, caption="Vincent van Gogh", use_column_width=True)

        col6.markdown(" ")

        original5 = Image.open("van010.jpg")
        col6.image(original5, caption="Vincent van Gogh", use_column_width=True)

        col7, col8, col9 = st.columns(3)

        col7.markdown(" ")
        
        original7 = Image.open("van02.jpg")
        col7.image(original7, caption="Vincent van Gogh", use_column_width=True)

        col8.markdown(" ")

        original8 = Image.open("van03.jpg")
        col8.image(original8, caption="Vincent van Gogh", use_column_width=True)

        col9.markdown(" ")

        original9 = Image.open("van01.jpg")
        col9.image(original9, caption="Vincent van Gogh", use_column_width=True)

    with tab5:
        st.subheader("Artist:ไอซ์-รัตตา อนันต์ภาดา")
        st.markdown(" ")
        col1, col2, col3 = st.columns(3)

        original1 = Image.open("ai01.webp")
        col1.image(original1, caption="ไอซ์-รัตตา อนันต์ภาดา", use_column_width=True)

        original2 = Image.open("ai02.jpg")
        col2.image(original2, caption="ไอซ์-รัตตา อนันต์ภาดา", use_column_width=True)

        original3 = Image.open("ai03.jpg")
        col3.image(original3, caption="ไอซ์-รัตตา อนันต์ภาดา", use_column_width=True)

        col4, col5, col6 = st.columns(3)

        col4.markdown(" ")
        
        original4 = Image.open("ai04.jpg")
        col4.image(original4, caption="ไอซ์-รัตตา อนันต์ภาดา", use_column_width=True)

        col5.markdown(" ")

        original5 = Image.open("ai05.webp")
        col5.image(original5, caption="ไอซ์-รัตตา อนันต์ภาดา", use_column_width=True)

        col6.markdown(" ")

        original5 = Image.open("ai06.jpg")
        col6.image(original5, caption="ไอซ์-รัตตา อนันต์ภาดา", use_column_width=True)

        col7, col8, col9 = st.columns(3)

        col7.markdown(" ")
        
        original7 = Image.open("ai08.jpg")
        col7.image(original7, caption="ไอซ์-รัตตา อนันต์ภาดา", use_column_width=True)

        col8.markdown(" ")

        original8 = Image.open("ai07.jpg")
        col8.image(original8, caption="ไอซ์-รัตตา อนันต์ภาดา", use_column_width=True)

        col9.markdown(" ")

        original9 = Image.open("ai09.jpg")
        col9.image(original9, caption="ไอซ์-รัตตา อนันต์ภาดา", use_column_width=True)

    with tab6:
        st.subheader("Artist: Peakkyboo")
        st.markdown(" ")
        col1, col2, col3 = st.columns(3)

        original1 = Image.open("p01.jpg")
        col1.image(original1, caption="Peakkyboo", use_column_width=True)

        original2 = Image.open("p02.jpg")
        col2.image(original2, caption="Peakkyboo", use_column_width=True)

        original3 = Image.open("p04.jpg")
        col3.image(original3, caption="Peakkyboo", use_column_width=True)

        col4, col5, col6 = st.columns(3)

        col4.markdown(" ")
        
        original4 = Image.open("p06.jpg")
        col4.image(original4, caption="Peakkyboo", use_column_width=True)

        col5.markdown(" ")

        original5 = Image.open("p13.jpg")
        col5.image(original5, caption="Peakkyboo", use_column_width=True)

        col6.markdown(" ")

        original5 = Image.open("p07.jpg")
        col6.image(original5, caption="Peakkyboo", use_column_width=True)

        col7, col8, col9 = st.columns(3)

        col7.markdown(" ")
        
        original7 = Image.open("p08.jpg")
        col7.image(original7, caption="Peakkyboo", use_column_width=True)

        col8.markdown(" ")

        original8 = Image.open("p17.jpg")
        col8.image(original8, caption="Peakkyboo", use_column_width=True)

        col9.markdown(" ")

        original9 = Image.open("p09.jpg")
        col9.image(original9, caption="Peakkyboo", use_column_width=True)

    with tab7:
        st.subheader("Artist: Give me museums")
        st.markdown(" ")
        col1, col2, col3 = st.columns(3)

        original1 = Image.open("g01.jpg")
        col1.image(original1, caption="Give me museums", use_column_width=True)

        original2 = Image.open("g02.png")
        col2.image(original2, caption="Give me museums", use_column_width=True)

        original3 = Image.open("g03.jpg")
        col3.image(original3, caption="Give me museums", use_column_width=True)

        col4, col5, col6 = st.columns(3)

        col4.markdown(" ")
        
        original4 = Image.open("g04.jpg")
        col4.image(original4, caption="Give me museums", use_column_width=True)

        col5.markdown(" ")

        original5 = Image.open("g05.jpg")
        col5.image(original5, caption="Give me museums", use_column_width=True)

        col6.markdown(" ")

        original5 = Image.open("g06.jpg")
        col6.image(original5, caption="Give me museums", use_column_width=True)

        col7, col8, col9 = st.columns(3)

        col7.markdown(" ")
        
        original7 = Image.open("g07.jpg")
        col7.image(original7, caption="Give me museums", use_column_width=True)

        col8.markdown(" ")

        original8 = Image.open("g08.jpg")
        col8.image(original8, caption="Give me museums", use_column_width=True)

        col9.markdown(" ")

        original9 = Image.open("g09.jpg")
        col9.image(original9, caption="Give me museums", use_column_width=True)

if __name__ == "__main__":
    main()

