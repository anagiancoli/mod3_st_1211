import streamlit as st
st.write("Sou Servidor Público!")

st.title("Este é o título do app")
st.header("Este é o subtítulo")
st.subheader("Este é o terceiro subtítulo")
st.markdown("Este é texto")
st.caption("Esta é a a legenda")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')


color = st.select_slider(
    "Selecione a satifstação: ",
    options=[0, 25, 50, 75, 100],
)
st.write("My favorite color is", color)
