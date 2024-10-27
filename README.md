
Este projeto tem como objetivo implementar um sistema de governança para um fundo de investimento em criptoativos, permitindo que os participantes votem em tokens para decidir quais ativos serão incluídos no portfólio. A votação utiliza o método STV (Single Transferable Vote), o que garante uma distribuição mais justa dos votos entre os candidatos. O projeto também inclui a geração de relatórios de votação e a atualização automática de um site Google com os resultados.

Pré-requisitos

1. Credenciais do Google Cloud
  Para interação com o Google Sheets e Google Sites, o projeto utiliza a API do Google. O arquivo credentials.json contém as credenciais necessárias para autenticação do serviço. Certifique-se de criar um Service Account no Google Cloud Console e gerar as credenciais adequadas para acesso às APIs.
  
2. Dependências Python
  Para a execução do código no Google Colab, as seguintes bibliotecas são necessárias:
  

gspread
oauth2client
pytest
flake8
Você pode instalar essas dependências com o seguinte comando:

pip install gspread oauth2client pytest flake8

3. Google Apps Script
Os scripts em Google Apps Script são responsáveis pelo processamento da votação, geração de relatórios e atualização do Google Sites. Estes scripts devem ser importados diretamente na interface do Google Apps Script vinculada à planilha do Google Sheets onde os votos serão armazenados.

Funcionalidades

1. Processamento da Votação
  O arquivo processamento_votacao.gs contém a lógica para processar os votos recebidos e aplicar o método STV (Single Transferable Vote). Ele lê os dados da planilha "Votos", conta os votos para cada token, e aplica a fórmula de STV para determinar os vencedores [2].
  
2. Geração de Relatório
  O arquivo relatorio_votacao.gs gera um relatório dos votos processados e insere os resultados na planilha chamada "Resultados". Ele limpa os dados antigos antes de inserir os novos resultados e informa os usuários que o relatório foi gerado com sucesso [1].
  
3. Atualização do Google Sites
  O script atualizar_google_site.gs é usado para atualizar uma página do Google Sites com os resultados da votação. Ele coleta os dados processados e publica o resultado em HTML no site de governança do fundo [3].
  
4. Formulário de Votação
  O arquivo index.html contém o código HTML para uma interface de votação simples. Os eleitores podem escolher o token desejado e submeter seu voto. O formulário está preparado para ser embutido em uma página do Google Sites [4].
  
5. Colab Votação
  O arquivo colab_votacao.ipynb é um script Python para manipular o Google Sheets diretamente a partir do Google Colab. Ele permite adicionar votos manualmente e verificar o status da planilha de votos [4].
  

Como Executar

1. Configurar o Google Sheets e Google Sites
  Crie uma planilha no Google Sheets com duas abas: "Votos" e "Resultados".
  Cole os scripts processamento_votacao.gs, relatorio_votacao.gs e atualizar_google_site.gs no editor de scripts vinculado ao Google Sheets.
  Configure as permissões do Google Cloud para permitir a execução dos scripts com base nas credenciais da conta de serviço.
  
2. Submeter Votos
  Publique a página HTML (index.html) em um Google Site, ou embuta o código HTML diretamente em uma página de governança.
  Os usuários podem submeter seus votos através do formulário. Apenas votos autenticados pelo Google Login (preferencialmente no Google Chrome) serão aceitos.
  
3. Processar Votos e Gerar Relatório
  Execute o script processamento_votacao.gs para processar os votos e calcular os vencedores usando STV.
  Utilize o script relatorio_votacao.gs para gerar um relatório detalhado dos votos.
  O script atualizar_google_site.gs pode ser executado para automaticamente atualizar a página de resultados no Google Sites.
  Testes
  A pasta tests/ contém dois testes principais para garantir a integridade do sistema de votação.
  
4. test_processamento_votacao.py
  Este teste usa o framework unittest. Ele simula uma votação básica para verificar se a função processarVotacao está contando os votos corretamente para cada token [6].
  
5. test_relatorio_votacao.py
  Este teste verifica se o relatório de votação está sendo gerado corretamente e inserido na planilha de resultados. Ele usa unittest.mock para simular as interações com a API do Google Sheets [1].
  

Para rodar os testes, basta executar o seguinte comando:
pytest

Integração com GitHub Actions
O projeto inclui um pipeline de Integração Contínua (CI) para garantir a qualidade do código. O arquivo .github/workflows/ci.yml define o fluxo de trabalho que realiza o linting do código com flake8 e executa os testes automatizados com pytest.

Como configurar o CI:
Certifique-se de ter um arquivo requirements.txt no diretório raiz com as dependências do projeto.
O pipeline será automaticamente acionado para cada push ou pull request na branch main.
Contribuindo
Contribuições são bem-vindas! Siga os seguintes passos para contribuir com o projeto:

Faça um fork do repositório.
Crie uma nova branch para sua feature (git checkout -b feature/nova-feature).
Faça o commit de suas alterações (git commit -m 'Adiciona nova feature').
Faça o push para a branch (git push origin feature/nova-feature).
Abra um Pull Request.
Licença
Este projeto está licenciado sob a MIT License.
