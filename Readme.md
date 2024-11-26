# Fake News Classifier 📰🚨

Este projeto é um sistema de classificação de notícias falsas baseado em aprendizado de máquina, desenvolvido para detectar automaticamente se uma notícia é verdadeira ou falsa com base no texto fornecido. Utiliza técnicas de processamento de linguagem natural (NLP) como **TF-IDF Vectorizer** e algoritmos de classificação como **Logistic Regression**, **Decision Tree** e **Gradient Boosting**.

---

## 📋 Funcionalidades

- Pré-processamento e análise de texto.
- Transformação de texto em representações numéricas usando **TF-IDF**.
- Treinamento e avaliação de modelos de machine learning:
  - **Regressão Logística**
  - **Árvores de Decisão**
  - **Gradient Boosting**
- Interface de usuário interativa utilizando **Streamlit**.
- Suporte a validação cruzada para comparar modelos.
- Configuração para treinamento eficiente e generalização.

---

## 📁 Estrutura do Projeto

```
fake-news-classifier/
├── data/
│   ├── Fake.csv        # Dataset de notícias falsas
│   ├── True.csv        # Dataset de notícias verdadeiras
│
├── models/
│   ├── logistic_model.pkl        # Modelo treinado de Regressão Logística
│   ├── decision_tree_model.pkl   # Modelo treinado de Árvore de Decisão
│   └── gradient_boosting_model.pkl # Modelo treinado de Gradient Boosting
│
├── notebooks/
│   ├── data_exploration.ipynb    # Análise exploratória de dados
│   └── model_training.ipynb      # Treinamento dos modelos
│
├── streamlit/
│   └── app.py                    # Interface interativa com Streamlit
│
├── requirements.txt              # Dependências do projeto
├── README.md                     # Documentação do projeto
└── main.py                       # Script principal
```

---

## 🚀 Tecnologias Utilizadas

- **Linguagem:** Python
- **Bibliotecas principais:**
  - Scikit-learn (modelos de machine learning)
  - Pandas e NumPy (manipulação de dados)
  - Streamlit (interface de usuário)
  - Matplotlib e Seaborn (visualização de dados)
- **Outros:**
  - Docker (containerização)
  - Prisma (gerenciamento de banco de dados)

---

## 🛠️ Como Rodar o Projeto

### Pré-requisitos

- Python 3.8 ou superior
- Pip ou Gerenciador de Pacotes Conda
- Docker (opcional para implantação)

### Passos

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/FellipeMasc/fake-news-classifier.git
   cd fake-news-classifier
   ```

2. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a interface com Streamlit:**

   ```bash
   streamlit run streamlit/app.py
   ```

4. **(Opcional) Execute com Docker:**
   ```bash
   docker build -t fake-news-classifier .
   docker run -p 8501:8501 fake-news-classifier
   ```

---

## 📊 Avaliação de Modelos

### Modelos Treinados

| Modelo              | Acurácia | Precision | Recall | F1-Score |
| ------------------- | -------- | --------- | ------ | -------- |
| Regressão Logística | 94.2%    | 93.8%     | 94.5%  | 94.1%    |
| Árvore de Decisão   | 88.5%    | 87.0%     | 88.0%  | 87.5%    |
| Gradient Boosting   | 96.0%    | 95.5%     | 96.2%  | 95.8%    |

O **Gradient Boosting** obteve o melhor desempenho geral, capturando relações mais complexas nos dados.

---

## 📂 Datasets

- **Origem:** Kaggle (Notícias verdadeiras e falsas)
- **Formato:** Arquivos CSV com as seguintes colunas:
  - `title`: Título da notícia
  - `text`: Texto completo da notícia
  - `label`: 1 para notícias verdadeiras, 0 para falsas

---

## 🌐 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um **Pull Request** ou relatar problemas no repositório.

---

## 📜 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
