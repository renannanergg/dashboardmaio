import streamlit as st
import pandas as pd

with st.container():
    st.subheader('LA PARK ESTACIONAMENTO')
    st.title('Movimento Avulsos de Maio')
    st.write('Gráficos com informações sobre o movimento de veículos avulsos e valores registrados no mês de Maio.')

#Se quiser adicionar link
#st.write('Deseja entrar em contato? [Clique aqui](LINK)')

#Lendo arquivo excel 
def carregar_dados():
    dados=pd.read_excel('MOV MES MAIO.xlsx')
    return dados
df=carregar_dados()

#Conteúdo do site e interface com gráficos
with st.container():
    #Converter o arquivo em CSV
    def convert_df(df):
        return df.to_csv().encode("utf-8")

    csv = convert_df(df)
    #Download da planilha
    st.download_button(
        label="Download informações",
        data=csv,
        file_name="movimento_maio",
        mime="text/csv",
    )

    tab1,tab2,tab3,tab4= st.tabs(["Veículos por semana","Valores por semana","Pagamento cartão/pix","Pagamento em dinheiro"])

    with tab1:
        st.header("Veículos por semana:")
        st.area_chart(df,x='SEMANAS',y='VEÍCULO POR SEMANA')
        with st.expander("Ver detalhes"):
            st.write(
            '''O Gráfico acima nos informa a quantidade de veículos estacionados por cada semana do mês,
            Totalizando 295 Veículos.
            
            ''')
    with tab2:
        st.header("Valores por semana")
        st.area_chart(df,x='SEMANAS',y='TOTAL POR SEMANA',color='#ffaa0088')
        with st.expander("Ver detalhes"):
            st.write(
            '''O Gráfico acima nos informa os valores recebidos em cada semana do mês,
            Totalizando R$2.417,00
            ''')

    with tab3:
        st.header("Pagamento cartão/pix")
        st.bar_chart(df,x='TOTAL CARTAO/PIX',y='TOTAL (R$)',horizontal=True)
        with st.expander("Ver detalhes"):
            st.write(
            """O Gráfico acima nos informa sobre os valores recebidos via cartão ou pix,
            Totalizando R$1.485,00
            """)

    with tab4:
        st.header("Pagamento dinheiro")
        st.bar_chart(df,x='TOTAL DINHEIRO',y='TOTAL (R$)',horizontal=True)
        with st.expander("Ver detalhes"):
            st.write(
            """O Gráfico acima nos informa sobre os valores recebidos em dinheiro,
            Totalizando R$932,00
            """)