import gspread
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials

# Autenticação com Google Sheets API
creds = Credentials.from_service_account_file('credentials.json')
client = gspread.authorize(creds)

# Abrir a planilha de votação
spreadsheet = client.open('votacao_fundo_cripto')
sheet = spreadsheet.worksheet('Votos')

# Obter os votos atualizados
votos = sheet.get_all_values()
for linha in votos:
    print(linha)

# Função para adicionar votos
def adicionar_voto(token):
    sheet.append_row([token])
    print(f"Voto para {token} registrado com sucesso!")

# Exemplo de uso
adicionar_voto('Bitcoin')