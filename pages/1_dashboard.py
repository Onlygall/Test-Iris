# Halaman 4: Foto Bunga
elif page == "🌸 Foto Bunga":
    st.title("🌸 Foto Jenis Bunga Iris")
    st.markdown("Berikut adalah gambar dari tiga spesies bunga Iris:")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_setosa_2.jpg", caption="Setosa", use_column_width=True)

    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_versicolor_3.jpg", caption="Versicolor", use_column_width=True)

    with col3:
        st.image("https://upload.wikimedia.org/wikipedia/commons/6/60/Iris_virginica.jpg", caption="Virginica", use_column_width=True)

