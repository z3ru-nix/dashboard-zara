import pandas as pd
import streamlit as st
import plotly.express as px

#config Pagina
st.set_page_config(
    page_title="Dashboard da Zara",
    layout="wide"
)

st.title("Dashboard de Análise de Roupas")
st.markdown("**Explore** os Dados de Produtos da Zara")

@st.cache_data
def load_data():
    df = pd.read_csv("zara.csv", sep=";")
    return df

df = load_data()

# ---
# Side bar filters
# ---
section = st.sidebar.multiselect(
    "Selecione a Seção",
    options=df['section'].unique(),
    default=df['section'].unique()
)

promotion = st.sidebar.multiselect(
    "Selecione a Promoção",
    options=df['Promotion'].unique(),
    default=df['Promotion'].unique()
)

# ---
# Filtering the dataframe
# ---
df_filtered = df[
    df["section"].isin(section) &
    df["Promotion"].isin(promotion)
]

# ---
# Main content
# ---
st.subheader("Principais métricas")
col1, col2, col3 = st.columns(3)
col1.metric("Total de produtos", len(df_filtered))
col2.metric("Soma de preços total", round(df_filtered['price'].sum(), 2))
col3.metric("Média de preços", round(df_filtered["price"].mean(), 2))

price_distribution = px.histogram(
    df_filtered,
    x="price",
    nbins=50,
    title="Distribuição de Preços",
    template="plotly_white"
)
st.plotly_chart(price_distribution)

st.dataframe(df_filtered)