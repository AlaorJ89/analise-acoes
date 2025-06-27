# %%
import requests
import pandas as pd

API_KEY = 'DIGITE SEU API'
query = 'ações bolsa de valores'
url = f'https://newsapi.org/v2/everything?q={query}&language=pt&sortBy=publishedAt&apiKey={API_KEY}'

response = requests.get(url)
data = response.json()

# Verifica se deu certo
if data['status'] == 'ok':
    noticias = []
    for article in data['articles']:
        noticias.append({
            'titulo': article['title'],
            'descricao': article['description'],
            'conteudo': article['content'],
            'data': article['publishedAt'],
            'fonte': article['source']['name'],
            'url': article['url']
        })

    df = pd.DataFrame(noticias)
    print(df.head())
else:
    print('Erro ao buscar notícias:', data)

# %%
import nltk
nltk.download('vader_lexicon')

# %%
from nltk.sentiment.vader import SentimentIntensityAnalyzer

analisador = SentimentIntensityAnalyzer()

# Aplica análise de sentimento
df['sentimento'] = df['descricao'].fillna('').apply(lambda x: analisador.polarity_scores(x)['compound'])

# Exibe as notícias com os sentimentos
print(df[['titulo', 'sentimento']].head())

# %%
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Inicializa o analisador
analisador = SentimentIntensityAnalyzer()

# Aplica análise de sentimento e calcula o compound
df['sentimento'] = df['descricao'].fillna('').apply(lambda x: analisador.polarity_scores(x)['compound'])

# Função para classificar o sentimento
def classificar_sentimento(score):
    if score >= 0.05:
        return 'Positiva'
    elif score <= -0.05:
        return 'Negativa'
    else:
        return 'Neutra'

# Aplica a classificação de sentimento
df['classificacao_sentimento'] = df['sentimento'].apply(classificar_sentimento)

# Exibe as primeiras notícias com suas classificações
print(df[['titulo', 'sentimento', 'classificacao_sentimento']].head())

# %%
import requests
import pandas as pd
import yfinance as yf
import os
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Baixa recursos do nltk, se necessário
nltk.download('vader_lexicon', quiet=True)

def buscar_noticias(api_key, query='ações bolsa de valores'):
    url = f'https://newsapi.org/v2/everything?q={query}&language=pt&sortBy=publishedAt&apiKey={api_key}'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Erro ao conectar com a NewsAPI: {e}")
        return pd.DataFrame()

    if data.get('status') == 'ok':
        noticias = [
            {
                'titulo': art['title'],
                'descricao': art['description'],
                'conteudo': art['content'],
                'data': art['publishedAt'],
                'fonte': art['source']['name'],
                'url': art['url']
            }
            for art in data['articles']
        ]
        return pd.DataFrame(noticias)
    else:
        print("Erro ao buscar notícias:", data)
        return pd.DataFrame()

def analisar_sentimentos(df):
    analisador = SentimentIntensityAnalyzer()
    df['descricao'] = df['descricao'].fillna('')
    df['sentimento'] = df['descricao'].apply(lambda x: analisador.polarity_scores(x)['compound'])

    def classificar(score):
        if score >= 0.05:
            return 'Positiva'
        elif score <= -0.05:
            return 'Negativa'
        else:
            return 'Neutra'

    df['classificacao_sentimento'] = df['sentimento'].apply(classificar)
    return df

def obter_precos(acao):
    dados = yf.download(acao, period='30d', interval='1d')
    if dados.empty:
        raise ValueError("Não foi possível obter dados para o ticker informado.")
    preco_atual = dados['Close'].iloc[-1].item()
    media_preco = dados['Close'].mean().item()
    return preco_atual, media_preco

def recomendar(sentimento, preco_atual, media_preco):
    if sentimento == 'Positiva' and preco_atual < media_preco:
        return 'Comprar'
    elif sentimento == 'Negativa' and preco_atual > media_preco:
        return 'Vender'
    else:
        return 'Manter'

def main():
    print("Análise de Ações baseada em Notícias e Preços")
    ticker = input("Digite o ticker da ação (ex: PETR4 ou AERI3): ").strip().upper()
    if not ticker.endswith('.SA'):
        ticker += '.SA'

    api_key = 'SUA CHAVE API AQUI'  # Substitua por sua chave da NewsAPI.org

    df_noticias = buscar_noticias(api_key)
    if df_noticias.empty:
        print("Nenhuma notícia encontrada ou erro na API.")
        return

    df_analisado = analisar_sentimentos(df_noticias)
    sentimento_geral = df_analisado['classificacao_sentimento'].value_counts().idxmax()

    try:
        preco_atual, media_preco = obter_precos(ticker)
    except ValueError as e:
        print(e)
        return

    decisao = recomendar(sentimento_geral, preco_atual, media_preco)

    print("\nResumo da Análise:")
    print(f"Ticker: {ticker}")
    print(f"Preço atual: R$ {preco_atual:.2f}")
    print(f"Média 30 dias: R$ {media_preco:.2f}")
    print(f"Sentimento geral das notícias: {sentimento_geral}")
    print(f"\n>>> Recomendação: {decisao.upper()} <<<")

if __name__ == '__main__':
    main()



