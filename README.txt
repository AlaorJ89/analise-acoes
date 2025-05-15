Análise de Ações baseada em Notícias e Preços
Este projeto realiza uma análise automatizada de ações da bolsa de valores brasileira, combinando sentimento de notícias com o preço histórico da ação.

-- Como funciona
O usuário informa o ticker da ação (ex: PETR4, AERI3).

O sistema busca notícias recentes sobre o mercado usando a NewsAPI.

As descrições das notícias são analisadas com NLP (análise de sentimento).

O script consulta os últimos 30 dias de preços da ação via yfinance.

Uma recomendação é exibida: Comprar, Vender ou Manter.

-- Lógica da Recomendação
Comprar: Sentimento positivo + preço abaixo da média.

Vender: Sentimento negativo + preço acima da média.

Manter: Qualquer outro caso.

-- Configuração

Instale as dependências executando:

```bash
pip install -r requirements.txt

-- Como usar
Clone este repositório:

bash
Copy
Edit
git clone https://github.com/seu-usuario/analise-acoes.git
cd analise-acoes
Instale as dependências:

bash
Copy
Edit
pip install -r requirements.txt
Crie uma conta gratuita na NewsAPI e pegue sua chave.

Abra o arquivo analise_acoes.py e substitua MINHA_CHAVE pela sua chave real da NewsAPI:

python
Copy
Edit
api_key = 'SUA_CHAVE_AQUI'
Execute o script:

bash
Copy
Edit
python analise_acoes.py

-- Tecnologias utilizadas
Python

Pandas

yfinance

NLTK (VADER)

NewsAPI

-- Observações
A NewsAPI tem limite de requisições no plano gratuito.

Os dados da yfinance são apenas para fins educacionais e podem conter imprecisões.


Versão em inglês disponível: README_en.md