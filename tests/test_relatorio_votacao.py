import unittest
from scripts.relatorio_votacao import gerarRelatorio
from unittest.mock import MagicMock

class TestRelatorioVotacao(unittest.TestCase):

    def test_geracao_relatorio(self):
        # Mockar os resultados da votação
        resultados_mock = {
            "Bitcoin": 3,
            "Ethereum": 2
        }

        # Criar mocks para as funções de planilha
        sheetResultados = MagicMock()
        SpreadsheetApp = unittest.mock.Mock()
        SpreadsheetApp.getActiveSpreadsheet.return_value.getSheetByName.return_value = sheetResultados

        # Substituir a função processarVotacao com valores mockados
        processarVotacao = MagicMock(return_value=resultados_mock)

        # Chamar a função de geração de relatório
        gerarRelatorio()

        # Verificar se os resultados foram corretamente inseridos na planilha
        sheetResultados.appendRow.assert_any_call(['Token', 'Votos'])
        sheetResultados.appendRow.assert_any_call(['Bitcoin', 3])
        sheetResultados.appendRow.assert_any_call(['Ethereum', 2])

if __name__ == '__main__':
    unittest.main()