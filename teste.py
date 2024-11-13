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
st.write("Satisfação: ", color)

st.info(f"A satisfação foi de: {color}", icon=":material/thumb_up:" )

st.write("******************")

#criando elementos gráficos
'''Informar como colher os dados através de variáveis'''
x = st.checkbox('Sim')
st.write(x)

#fazer o mesmo com alguns dos comandos abaixo
st.title(x)
st.button('Clique')
st.radio('Selecione seu gênero',['Masculino','Feminino'])
st.selectbox('Selecione seu gênero',['Masculino','Feminino'])
st.multiselect('Escolha um departamento',['DCS', 'DE', 'DIR'])
st.select_slider('Selecione uma resposta', ['Ruim', 'Bom', 'Excelente'])
st.slider('Selecione um número', 0,50)
st.number_input('Selecione um número', 0,10)
st.text_input('Endereço de e-mail')
st.date_input('Data de viagem')
st.time_input('Tempo de escola')
st.text_area('Descrição')
st.file_uploader('Atualize uma foto')
st.color_picker('Escolha sua cor favorita')

#mensagens de status
st.success("Você conseguiu!")
st.error("Erro!")
st.warning("Advertência")
st.info("Esta é uma informação")

st.write("**********************")
#criando uma aplicação simples
import streamlit as st
#import no requirements.txt
import pandas as pd

df = pd.DataFrame({
    'nomeServidor': ['Adriana', 'Monica', 'Samara'],
    'salario': [1200,300,5000]
})

st.write("Criando uma tabela!")
#tabelas interativas
st.write(df)
#inserindo um selectbox
opcao = st.selectbox(
    'Qual servidor você gostaria de selecionar?',
     df['nomeServidor'])

#LEMBRETE: O formato de print é diferente do fstring de Python
st.write('Você selecionou: ', opcao)

dfFiltrado = df.loc[df['nomeServidor'] == opcao]
st.write(dfFiltrado)
