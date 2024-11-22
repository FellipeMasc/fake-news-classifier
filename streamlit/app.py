import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from text_analysis import (
    clean_text,
    get_top_words,
    calculate_sentiment,
    generate_wordcloud,
    get_top_ngrams,
    vocabulary_diversity,
    plot_top_words,
)
from other_analysis import (
    distribution_by_subject,
    temporal_analysis,
    text_length_analysis,
    subject_text_length_correlation,
    correlation_matrix_analysis,
)

# Configurar a página
st.set_page_config(page_title="Fake vs True News Analysis", layout="wide")

# Título
st.title("Fake vs True News Analysis")

# Carregar os arquivos automaticamente
@st.cache_data
def load_data():
    fake_data = pd.read_csv("Fake.csv")
    true_data = pd.read_csv("True.csv")
    return fake_data, true_data

df_fake, df_true = load_data()

# Limpar os textos (aplica apenas uma vez)
@st.cache_data
def preprocess_data(df_fake, df_true):
    df_fake['clean_text'] = df_fake['text'].apply(clean_text)
    df_true['clean_text'] = df_true['text'].apply(clean_text)
    return df_fake, df_true

df_fake, df_true = preprocess_data(df_fake, df_true)

# Configurar a barra lateral
st.sidebar.header("Escolha a Análise")
analysis_option = st.sidebar.selectbox(
    "Selecione uma análise:",
    [
        "Palavras Mais Frequentes",
        "Análise de Sentimento",
        "Nuvem de Palavras",
        "N-Gramas",
        "Diversidade de Vocabulário",
        "Análise de Distribuição de Notícias por Assunto",
        "Análise Temporal",
        "Análise de Comprimento de Texto",
        "Correlação Entre Assunto e Comprimento do Texto",
        "Matriz de Correlação",
    ],
)

# Executar a análise escolhida
if analysis_option == "Palavras Mais Frequentes":
    st.subheader("Palavras Mais Frequentes")
    fake_top_words = get_top_words(df_fake['clean_text'])
    true_top_words = get_top_words(df_true['clean_text'])

    st.write("Fake News:")
    fake_df = plot_top_words(fake_top_words, "Fake News")
    st.bar_chart(fake_df.set_index('Word'))

    st.write("True News:")
    true_df = plot_top_words(true_top_words, "True News")
    st.bar_chart(true_df.set_index('Word'))

elif analysis_option == "Análise de Sentimento":
    st.subheader("Análise de Sentimento")
    df_fake['sentiment'] = calculate_sentiment(df_fake['clean_text'])
    df_true['sentiment'] = calculate_sentiment(df_true['clean_text'])

    st.write("Sentimento Médio - Fake News:", df_fake['sentiment'].mean())
    st.write("Sentimento Médio - True News:", df_true['sentiment'].mean())

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    ax[0].hist(df_fake['sentiment'], bins=30, color='red', alpha=0.7)
    ax[0].set_title("Sentimento - Fake News")
    ax[1].hist(df_true['sentiment'], bins=30, color='blue', alpha=0.7)
    ax[1].set_title("Sentimento - True News")
    st.pyplot(fig)

elif analysis_option == "Nuvem de Palavras":
    st.subheader("Nuvem de Palavras")
    fake_wordcloud = generate_wordcloud(df_fake['clean_text'])
    true_wordcloud = generate_wordcloud(df_true['clean_text'])

    st.write("Fake News:")
    st.image(fake_wordcloud.to_array())

    st.write("True News:")
    st.image(true_wordcloud.to_array())

elif analysis_option == "N-Gramas":
    st.subheader("N-Gramas")
    n = st.slider("Escolha o número de palavras no n-grama:", 2, 5, 2)
    fake_ngrams = get_top_ngrams(df_fake['clean_text'], ngram_range=(n, n))
    true_ngrams = get_top_ngrams(df_true['clean_text'], ngram_range=(n, n))

    st.write("Fake News N-Gramas:")
    st.write(pd.DataFrame(fake_ngrams, columns=["N-Grama", "Frequência"]))

    st.write("True News N-Gramas:")
    st.write(pd.DataFrame(true_ngrams, columns=["N-Grama", "Frequência"]))

elif analysis_option == "Diversidade de Vocabulário":
    st.subheader("Diversidade de Vocabulário")
    fake_diversity = vocabulary_diversity(df_fake['clean_text'])
    true_diversity = vocabulary_diversity(df_true['clean_text'])

    st.write("Diversidade de Vocabulário - Fake News:", fake_diversity)
    st.write("Diversidade de Vocabulário - True News:", true_diversity)

elif analysis_option == "Análise de Distribuição de Notícias por Assunto":
    st.subheader("Análise de Distribuição de Notícias por Assunto")
    distribution_by_subject(df_fake, df_true)

elif analysis_option == "Análise Temporal":
    st.subheader("Análise Temporal")
    temporal_analysis(df_fake, df_true)

elif analysis_option == "Análise de Comprimento de Texto":
    st.subheader("Análise de Comprimento de Texto")
    text_length_analysis(df_fake, df_true)

elif analysis_option == "Correlação Entre Assunto e Comprimento do Texto":
    st.subheader("Correlação Entre Assunto e Comprimento do Texto")
    subject_text_length_correlation(df_fake, df_true)

elif analysis_option == "Matriz de Correlação":
    st.subheader("Matriz de Correlação")
    correlation_matrix_analysis(df_fake, df_true)

else:
    st.subheader("Análise não reconhecida.")
    st.write("Selecione uma análise válida na barra lateral.")
