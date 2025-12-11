import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

# URL da planilha
URL = "https://docs.google.com/spreadsheets/d/1Mj-4LejLhf_c6UxCpeR7I9MhLWiDq0Vwkp7btajN1hg/edit"

# Nome da aba
ABA = "Solicitaçôes Pendentes"

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credenciais.json", scopes=scopes)
client = gspread.authorize(creds)

def carregar_dados():
    sheet = client.open_by_url(URL).worksheet(ABA)
    dados = sheet.get_all_records()
    df = pd.DataFrame(dados)
    return df

# ---------------- INTERFACE -----------------
st.title("Painel de Solicitações Pendentes")

if st.button("Carregar dados"):
    df = carregar_dados()
    st.success("Dados carregados com sucesso!")
    st.dataframe(df, use_container_width=True)
