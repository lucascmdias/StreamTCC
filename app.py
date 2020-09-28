import streamlit as st
import pandas as pd
import numpy as np


pd.options.display.max_columns = 20
pd.options.display.max_rows = 9999

#aumento de 2% de conc ou temp - padrão
padrao_conc_metanol = pd.read_csv('dados_conc_metanol_csv.csv', sep = ",")
padrao_conc_tolueno = pd.read_csv('dados_conc_tolueno_csv.csv', sep = ",")
padrao_temp_metanol = pd.read_csv('dados_temp_metanol_csv.csv', sep = ",")
padrao_temp_tolueno = pd.read_csv('dados_temp_tolueno_csv.csv', sep = ",")

#perturbacao8 = pd.read_csv('C:\\Users\\lucas\\Desktop\\dados tcc\\perturbacoes\\perturbacao8\\dados_perturbacao8_csv.csv', sep=',')
#perturbacao9 = pd.read_csv('C:\\Users\\lucas\\Desktop\\dados tcc\\perturbacoes\\perturbacao9\\dados_perturbacao9_csv.csv', sep=',')

dados_padrao_temp_1 = pd.read_csv('dados_padrao1_csv.csv', decimal=',')
dados_padrao_temp_2 = pd.read_csv('dados_padrao2_csv.csv', decimal=',')
temp_perturbacao1 = pd.read_csv('temp_perturbacao1_csv.csv', decimal=',')
temp_perturbacao2 = pd.read_csv('temp_perturbacao2_csv.csv', decimal=',')

#perturbacao7 = pd.read_csv('C:\\Users\\lucas\\Desktop\\dados tcc\\perturbacoes\\perturbacao7\\dados_perturbacao7_csv.csv', sep=',')
#perturbacao10 = pd.read_csv('C:\\Users\\lucas\\Desktop\\dados tcc\\perturbacoes\\perturbacao10\\dados_perturbacao10_csv.csv', sep=',')
#perturbacao11 = pd.read_csv('C:\\Users\\lucas\\Desktop\\dados tcc\\perturbacoes\\perturbacao11\\dados_perturbacao11_csv.csv', sep=',')
#perturbacao12 = pd.read_csv('C:\\Users\\lucas\\Desktop\\dados tcc\\perturbacoes\\perturbacao12\\dados_perturbacao12_csv.csv', sep=',')
#perturbacao13 = pd.read_csv('C:\\Users\\lucas\\Desktop\\dados tcc\\perturbacoes\\perturbacao13\\dados_perturbacao13_csv.csv', sep=',')

#padrao down 2% \/
padrao_down_conc_metanol = pd.read_csv('dados_down_conc_padrao_metanol_csv.csv',sep=',')
padrao_down_conc_tolueno = pd.read_csv('dados_down_conc_padrao_tolueno_csv.csv',sep=',')
padrao_down_temp_metanol = pd.read_csv('dados_down_temp_padrao_metanol_csv.csv',sep=',')
padrao_down_temp_tolueno = pd.read_csv('dados_down_temp_padrao_tolueno_csv.csv',sep=',')

#perturbacoes em queda
perturbacao14 = pd.read_csv('dados_perturbacao14_csv.csv', sep=',')
perturbacao15 = pd.read_csv('dados_perturbacao15_csv.csv', sep=',')
#testes
teste2 = pd.read_csv('teste2_csv.csv', sep=',')
#AGORAVAI
perturbacao16 = pd.read_csv('dados_perturbacao16_csv.csv', sep=',')
identificador16 = pd.read_csv('identificador16_csv.csv', sep=',')



def retornar_porcentagem_mudanca(numero_calculo_mudanca):
    #numero_calculo_mudanca = round(numero_calculo_mudanca, 1)
    if numero_calculo_mudanca == 2.9:
        numero_calculo_mudanca = 3
    elif numero_calculo_mudanca >= 4.3 and numero_calculo_mudanca <= 4.5:
        numero_calculo_mudanca = 5

    # CONTINUAR
    return numero_calculo_mudanca

def arredondar_lista(lista):
    for i in range(0, len(lista)):
        lista[i] = round(lista[i], 8)

def listar_num_dif(string,dataframe):
    a = list(dataframe[string].drop_duplicates())
    for i in range(0,len(a)):
        a[i] = round(a[i],8)

    return a


def listar_columns(dataframe):
    a = list(dataframe.columns)
    return a

def porcent_num(lista_numeros):
    global porcentagem2
    if len(lista_numeros) <= 1:
        porcentagem2 = 0


    elif len(lista_numeros) == 2:
        if lista_numeros[0] == 0:
            a = (lista_numeros[0])/(lista_numeros[1])
            if a < 1:
                porcentagem = (1 - a)
                porcentagem2 = porcentagem * 100
            elif a >= 1:
                porcentagem = (a - 1)
                porcentagem2 = porcentagem * 100
        elif lista_de_colunas != 0:
            a = (lista_numeros[1]) / (lista_numeros[0])
            if a < 1:
                porcentagem = (1 - a)
                porcentagem2 = porcentagem * 100
            elif a >= 1:
                porcentagem = (a - 1)
                porcentagem2 = porcentagem * 100


    elif len(lista_numeros) >= 3:
        for i in range(2,len(lista_numeros)):
            ajuda = lista_numeros[i]/lista_numeros[i-1]
            ajuda = ajuda - 1
            if ajuda < 0:
                ajuda = ajuda*(-1)
            if ajuda < 0.0001:
                continue
            elif ajuda > 0.0001:
                if lista_numeros[i-1] == 0:
                    a = (lista_numeros[i-1]) / (lista_numeros[i])
                    if a < 1:
                        porcentagem = (1 - a)
                        porcentagem2 = porcentagem * 100
                    elif a >= 1:
                        porcentagem = (a - 1)
                        porcentagem2 = porcentagem * 100

                elif lista_numeros[i-1] != 0:
                    a = (lista_numeros[i]) / (lista_numeros[i-1])
                    if a < 1:
                        porcentagem = (1 - a)
                        porcentagem2 = porcentagem * 100
                    elif a >= 1:
                        porcentagem = (a - 1)
                        porcentagem2 = porcentagem * 100

    return round(porcentagem2,9)

def mudanca_valor_aum_dim(lista_numeros):
    global mudanca
    if len(lista_numeros) <= 1:
        mudanca = "inalterado"
    elif len(lista_numeros) == 2:
        if lista_numeros[1] - lista_numeros[0] < 0:
            mudanca = "diminuiu"
        elif lista_numeros[1] - lista_numeros[0] > 0:
            mudanca = "aumentou"
    elif len(lista_numeros) >= 3 and len(lista_numeros) <= 20:
        for i in range(2,len(lista_numeros)):
            ajuda = lista_numeros[i] / lista_numeros[i-1]
            ajuda = ajuda - 1
            if ajuda < 0:
                ajuda = ajuda*(-1)
            if ajuda < 0.0001:
                continue
            elif ajuda > 0.0001:
                if lista_numeros[i] - lista_numeros[i-1] < 0:
                    mudanca = "diminuiu"
                    break
                elif lista_numeros[i] - lista_numeros[i-1] > 0:
                    mudanca = "aumentou"
                    break
    elif len(lista_numeros) > 50:
        if lista_numeros[40] - lista_numeros[0] < 0:
            mudanca = "diminuiu"
        elif lista_numeros[40] - lista_numeros[0] > 0:
            mudanca = "aumentou"


    return mudanca

data = {
        'Reagente': None,
        'Parâmetro de Perturbação' : None ,
        'Previsão' : None,
        'Porcentagem de Mudança' : None
}

def verificar_tipo_perturbacao(dataframe_perturbacao,dataframe_padrao1,dataframe_padrao2,dataframe_padrao3,dataframe_padrao4):
    verificacao1 = []
    verificacao2 = []
    verificacao3 = []
    verificacao4 = []
    verif_porc = []
    lista_porc = []

    for i in range(0,dataframe_padrao1.shape[0]):
        if dataframe_perturbacao.loc[i,"string"] == dataframe_padrao1.loc[i,"string"]:
            verificacao1.append(1)
        else:
            verificacao1.append(0)

    if sum(verificacao1) == dataframe_perturbacao.shape[0]:
        #st.markdown("o tipo de perturbacao foi padrao1 - metanol")

        data['Reagente'] = "metanol"

        verif_porc.append('concentracao')
        f1 = (dataframe_perturbacao.loc[:,"porcentagem"].sum())/(dataframe_padrao1.loc[:,"porcentagem"].sum())
        f1 = f1*2
        f1 = round(f1,0)
        verif_porc.append(f1)
        #st.markdown("a porcentagem de mudanca foi de {} %".format(f1))
        #st.markdown(verif_porc)
        #print("\n")



    for i in range(0,dataframe_padrao2.shape[0]):
        if dataframe_perturbacao.loc[i,"string"] == dataframe_padrao2.loc[i,"string"]:
            verificacao2.append(1)
        else:
            verificacao2.append(0)

    if sum(verificacao2) == dataframe_perturbacao.shape[0]:
        #st.markdown("o tipo de perturbacao foi padrao2 - tolueno")
        data['Reagente'] = "tolueno"
        verif_porc.append('concentracao')
        f2 = (dataframe_perturbacao.loc[:, "porcentagem"].sum()) / (dataframe_padrao2.loc[:, "porcentagem"].sum())
        f2 = f2 * 2
        f2 = round(f2, 0)
        verif_porc.append(f2)
        #st.markdown("a porcentagem de mudanca foi de {} %".format(f2))
        #st.markdown(verif_porc)
        #print("\n")

    for i in range(0,dataframe_padrao3.shape[0]):
        if dataframe_perturbacao.loc[i,"string"] == dataframe_padrao3.loc[i,"string"]:
            verificacao3.append(1)
        else:
            verificacao3.append(0)

    if sum(verificacao3) == dataframe_perturbacao.shape[0]:
        #print("o tipo de perturbacao foi padrao3\n")
        verif_porc.append('temperatura')
        #st.markdown(verif_porc)

    for i in range(0,dataframe_padrao4.shape[0]):
        if dataframe_perturbacao.loc[i,"string"] == dataframe_padrao4.loc[i,"string"]:
            verificacao4.append(1)
        else:
            verificacao4.append(0)

    if sum(verificacao4) == dataframe_perturbacao.shape[0]:
        #print("o tipo de perturbacao foi padrao 4\n")
        verif_porc.append('temperatura')
        #st.markdown(verif_porc)


    return verif_porc

def verficar_perturbacao_temp(dataframe_perturbacao,dataframe_perturbacao_df):
    if dataframe_perturbacao.loc[dataframe_perturbacao.shape[0] -1,'T_dec'] > dataframe_perturbacao.loc[0,'T_dec']:
        #st.markdown("perturbacão na temperatura do tolueno")
        perturbacao = "tolueno"

    if dataframe_perturbacao.loc[dataframe_perturbacao.shape[0] -1,'T_dec'] < dataframe_perturbacao.loc[0,'T_dec']:
        if dataframe_perturbacao_df.loc[11,'porcentagem'] > 2.5:
            #st.markdown("perturbacão na temperatura do tolueno")
            perturbacao = "tolueno"
        else:
            #st.markdown("perturbacão na temperatura do metanol")
            perturbacao = "metanol"

    return perturbacao


def criar_listas_(dataframe,listadecolunas):
    lista_porcent_mudanca = []
    lista_string_mudanca = []
    lista_numeros = []
    global dicionario
    if len(listadecolunas) == 3:
        for i in range(1, len(listadecolunas)):
            numeros = listar_num_dif(listadecolunas[i], dataframe)
            lista_numeros.append(numeros)
            # print(porcent_num(numeros))
            lista_porcent_mudanca.append(porcent_num(numeros))
            # print(mudanca_valor_aum_dim(numeros))
            # print(lista_porcent_mudanca)
            lista_string_mudanca.append(mudanca_valor_aum_dim(numeros))
            # print(lista_string_mudanca)
            # print(numeros)
            dicionario = {'numeros': lista_numeros, 'porcentagem': lista_porcent_mudanca,
                          'string': lista_string_mudanca}
    else:
        for i in range(1, len(listadecolunas) - 1):
            numeros = listar_num_dif(listadecolunas[i], dataframe)
            lista_numeros.append(numeros)
            # print(porcent_num(numeros))
            lista_porcent_mudanca.append(porcent_num(numeros))
            # print(mudanca_valor_aum_dim(numeros))
            # print(lista_porcent_mudanca)
            lista_string_mudanca.append(mudanca_valor_aum_dim(numeros))
            # print(lista_string_mudanca)
            # print(numeros)
            dicionario = {'numeros': lista_numeros, 'porcentagem': lista_porcent_mudanca,
                          'string': lista_string_mudanca}


   # print(lista_string_mudanca)

    return dicionario

def verificar_aum_or_dim_perturbacao(perturbacao,identificador):
    lista_diminuiu = []
    lista_aumentou = []
    lista_inalterado = []
    ponto = 1
    status = None
    definitivo = None

    for i in range(0, perturbacao.shape[0]):
        if perturbacao.loc[i,"string"] == "diminuiu":
            lista_diminuiu.append(ponto)
        elif perturbacao.loc[i,"string"] == "aumentou":
            lista_aumentou.append(ponto)
        elif perturbacao.loc[i,"string"] == "inalterado":
            lista_inalterado.append(ponto)
    if sum(lista_aumentou) >=7 or sum(lista_diminuiu) >=7:
        status = "concentracao"
    if sum(lista_inalterado) >=5:
        status = "temperatura"

    if status == "temperatura":
        if identificador.loc[0,"string"] == "aumentou":
            definitivo = "aumentou"
        if identificador.loc[0,"string"] == "diminuiu":
            definitivo = "diminuiu"

    if status == "concentracao":
        if identificador.loc[1,"string"] == "aumentou":
            definitivo = "aumentou"
        if identificador.loc[1,"string"] == "diminuiu":
            definitivo = "diminuiu"

    return definitivo


#LISTAS NECESSARIAS
lista_de_colunas = listar_columns(padrao_conc_metanol)
lista_de_colunas2 = listar_columns(perturbacao16)
lista_de_colunas_teste = listar_columns(teste2)
lista_de_colunas_identificador = listar_columns(identificador16)

#PADROES FIXADOS
pad_conc_metanol = criar_listas_(padrao_conc_metanol,lista_de_colunas)
pad_conc_tolueno = criar_listas_(padrao_conc_tolueno,lista_de_colunas)
pad_temp_metanol = criar_listas_(padrao_temp_metanol,lista_de_colunas)
pad_temp_tolueno = criar_listas_(padrao_temp_tolueno,lista_de_colunas)
pad_down_conc_metanol = criar_listas_(padrao_down_conc_metanol,lista_de_colunas2)
pad_down_conc_tolueno = criar_listas_(padrao_down_conc_tolueno,lista_de_colunas2)
pad_down_temp_metanol = criar_listas_(padrao_down_temp_metanol,lista_de_colunas2)
pad_down_temp_tolueno = criar_listas_(padrao_down_temp_tolueno,lista_de_colunas2)
t_teste2 = criar_listas_(teste2,lista_de_colunas_teste)

#identificador
i_d16 = criar_listas_(identificador16,lista_de_colunas_identificador)
#CHEET
perturbacao_15 = criar_listas_(perturbacao15,lista_de_colunas2)
perturbacao_16 = criar_listas_(perturbacao16,lista_de_colunas2)


#FORMAÇÕES DO DATAFRAME DOS PADROES
df_pad_conc_metanol = pd.DataFrame(pad_conc_metanol)
df_pad_conc_tolueno = pd.DataFrame(pad_conc_tolueno)
df_pad_temp_metanol = pd.DataFrame(pad_temp_metanol)
df_pad_temp_tolueno = pd.DataFrame(pad_temp_tolueno)
df_pad_down_conc_metanol = pd.DataFrame(pad_down_conc_metanol)
df_pad_down_conc_tolueno = pd.DataFrame(pad_down_conc_tolueno)
df_pad_down_temp_metanol = pd.DataFrame(pad_down_temp_metanol)
df_pad_down_temp_tolueno = pd.DataFrame(pad_down_temp_tolueno)
#------------------------------------------------------------------------#


df_perturbacao15 = pd.DataFrame(perturbacao_15)
df_perturbacao16 = pd.DataFrame(perturbacao_16)

df_teste2 = pd.DataFrame(t_teste2)

#AGORAVAI?
df_id16 = pd.DataFrame(i_d16)



#head and images
st.title('Lógica Fuzzy no Processo da Produção de Estireno')
#st.image(image = 'fuzzy.png',format="PNG")
st.image(image = 'gif1.gif',output_format="GIF")

st.set_option('deprecation.showfileUploaderEncoding', False)

#buttons
file = st.sidebar.file_uploader('escolha a perturbacao', type='xlsx')
file2 = st.sidebar.file_uploader('escolha o identificador', type='xlsx')

#analise_robusta = st.sidebar.button('analise')
verificar = st.sidebar.button('Verificar')

if file and file2 is not None:
    perturbacao_x = pd.read_excel(file)
    perturbacao_ = criar_listas_(perturbacao_x, lista_de_colunas2)
    df_perturbacao_ = pd.DataFrame(perturbacao_)

    identificador_x = pd.read_excel(file2)
    identificador_ = criar_listas_(identificador_x, lista_de_colunas_identificador)
    df_identificador = pd.DataFrame(identificador_)

    st.header("Dados da Perturbação")

    st.subheader('o Tamanho deste DataFrame para a perturbação')
    st.markdown('{} Linhas e {} Colunas'.format(perturbacao_x.shape[0], perturbacao_x.shape[1]))
    st.markdown('')

    st.subheader("Descrição das colunas abaixo")
    st.markdown('')
    #st.markdown("A coluna Time --> é o tempo em horas")
    #st.markdown("As colunas LiqFrac -->  frações líquidas do reator")
    #st.markdown("As colunas vapFrac --> frações vapores do reator")
    #st.markdown("As colunas P_bar e T_c --> as pressões e temperaturas do reator")
    #st.markdown("A coluna T_dec --> a temperatura do decantador")

    slider1 = st.slider('TAMANHO PARA VISUALIZAÇÃO DAS LINHAS', 1,perturbacao_x.shape[0])
    st.dataframe(perturbacao_x.head(slider1))

    st.subheader('Análises Descritivas')
    st.write(perturbacao_x.describe())
    st.markdown('')

    st.subheader('Gráficos dos dados da Fração Líquida')
    st.line_chart(perturbacao_x[['LiqFrac_H','LiqFrac_MET','LiqFrac_STY','LiqFrac_TOL','LiqFrac_WAT']])
    st.markdown('')

    st.subheader('Gráficos dos dados da Fração Vapor')
    st.line_chart(perturbacao_x[['vapFrac_H', 'vapFrac_MET', 'vapFrac_STY', 'vapFrac_TOL', 'vapFrac_WAT']])
    st.markdown('')

    st.subheader('Gráficos dos dados da Temperatura e Pressão')
    st.line_chart(perturbacao_x[['T_c', 'T_dec', 'P_bar']])
    st.markdown('')

    st.subheader('Tabela dos uniques')
    st.subheader("Descrição das colunas abaixo")
    st.markdown('')
    #st.markdown("A coluna Numeros --> Números diferentes das colunas")
    #st.markdown("As colunas LiqFrac -->  frações líquidas do reator")
    #st.markdown("As colunas vapFrac --> frações vapores do reator")
    #st.markdown("As colunas P_bar e T_c --> as pressões e temperaturas do reator")
    #st.markdown("A coluna T_dec --> a temperatura do decantador")
    df_perturbacao_colunas = df_perturbacao_
    df_perturbacao_colunas['Tipo'] = ['LiqFrac_H','LiqFrac_MET','LiqFrac_STY','LiqFrac_TOL','LiqFrac_WAT',
                                      'vapFrac_H', 'vapFrac_MET', 'vapFrac_STY', 'vapFrac_TOL', 'vapFrac_WAT',
                                      'P_Reator_bar','T_Reator_C']


    st.dataframe(df_perturbacao_colunas)

    if verificar:

        #perturbacao_x = pd.read_csv(file)
        #perturbacao_ = criar_listas_(perturbacao_x, lista_de_colunas2)
        #df_perturbacao_ = pd.DataFrame(perturbacao_)

        #identificador_x = pd.read_csv(file2)
        #identificador_ = criar_listas_(identificador_x, lista_de_colunas_identificador)
        #df_identificador = pd.DataFrame(identificador_)

        ident = verificar_aum_or_dim_perturbacao(df_perturbacao_, df_identificador)


        if ident == "aumentou":
            g = verificar_tipo_perturbacao(df_perturbacao_, df_pad_conc_metanol, df_pad_conc_tolueno,
                                           df_pad_temp_metanol, df_pad_temp_tolueno)
            #st.markdown("houve um aumento na perturbação geral")
            data['Previsão'] = 'Aumento'
            data['Parâmetro de Perturbação'] = g[0]
            if g[0] == 'concentracao':
                data['Porcentagem de Mudança'] = g[1]



            # print("\n")

            if g[0] == 'temperatura':
                verficar_perturbacao_temp(perturbacao_x, df_perturbacao_)
                temp = verficar_perturbacao_temp(perturbacao_x, df_perturbacao_)
                if temp == "metanol":
                    f6 = (df_perturbacao_.loc[:, "porcentagem"].sum()) / (
                        df_pad_temp_metanol.loc[:, "porcentagem"].sum())
                    f6 = f6 * 2
                    f6 = round(f6, 1)

                    data['Reagente'] = temp

                    f7 = retornar_porcentagem_mudanca(f6)

                    data['Porcentagem de Mudança'] = f7

                    st.markdown("a porcentagem de mudanca foi de {} %".format(f7))
                    data['Porcentagem De Mudança'] = f7
                    # print("\n")
                elif temp == "tolueno":
                    f6 = (df_perturbacao_.loc[:, "porcentagem"].sum()) / (
                        df_pad_temp_tolueno.loc[:, "porcentagem"].sum())
                    f6 = f6 * 2
                    f6 = round(f6, 1)

                    data['Reagente'] = temp

                    f7 = retornar_porcentagem_mudanca(f6)
                    if f7 >= 3.7 and f7 <= 4.2:
                        f7 = 4.0
                        data['Porcentagem de Mudança'] = f7
                    if f7 >= 1.8 and f7 <= 2.2:
                        f7 = 2.0
                        data['Porcentagem de Mudança'] = f7
                    if f7 >= 2.8 and f7 <= 3.2:
                        f7 = 3.0
                        data['Porcentagem de Mudança'] = f7
                    st.markdown("a porcentagem de mudanca foi de {} %".format(f7))
                    # print("\n")

        if ident == "diminuiu":
            g = verificar_tipo_perturbacao(df_perturbacao_, df_pad_down_conc_metanol, df_pad_down_conc_tolueno,
                                           df_pad_down_temp_metanol, df_pad_down_temp_tolueno)
            #st.markdown("houve uma diminuição na perturbação geral")
            data['Previsão'] = 'Diminuição'
            data['Parâmetro de Perturbação'] = g[0]
            if g[0] == 'concentracao':
                data['Porcentagem de Mudança'] = g[1]



            if g[0] == 'temperatura':
                verficar_perturbacao_temp(perturbacao_x, df_perturbacao_)
                temp = verficar_perturbacao_temp(perturbacao_x, df_perturbacao_)
                if temp == "metanol":
                    f6 = (df_perturbacao_.loc[:, "porcentagem"].sum()) / (
                        df_pad_down_temp_metanol.loc[:, "porcentagem"].sum())
                    f6 = f6 * 2
                    f6 = round(f6, 1)

                    data['Reagente'] = temp

                    f7 = retornar_porcentagem_mudanca(f6)

                    data['Porcentagem de Mudança'] = f7

                    st.markdown("a porcentagem de mudanca foi de {} %".format(f7))
                    # print("\n")
                elif temp == "tolueno":
                    f6 = (df_perturbacao_.loc[:, "porcentagem"].sum()) / (
                        df_pad_down_temp_tolueno.loc[:, "porcentagem"].sum())
                    f6 = f6 * 2
                    f6 = round(f6, 1)

                    data['Reagente'] = temp

                    f7 = retornar_porcentagem_mudanca(f6)
                    if f7 >= 3.7 and f7 <= 4.2:
                        f7 = 4.0
                        data['Porcentagem de Mudança'] = f7
                    if f7 >= 1.8 and f7 <= 2.2:
                        f7 = 2.0
                        data['Porcentagem de Mudança'] = f7
                    if f7 >= 2.8 and f7 <= 3.2:
                        f7 = 3.0
                        data['Porcentagem de Mudança'] = f7

                    st.markdown("a porcentagem de mudanca foi de {} %".format(f7))
                    # print("\n")

        st.header("Identificação Da Perturbação do Processo de Estireno")

        final_ident = pd.DataFrame(data = data,index=[0], columns=['Reagente','Parâmetro de Perturbação',
                                                                       'Previsão','Porcentagem de Mudança'])
        st.dataframe(final_ident)








