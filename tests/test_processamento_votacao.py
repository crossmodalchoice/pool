import unittest
from scripts.processamento_votacao import processarVotacao

class TestProcessamentoVotacao(unittest.TestCase):

    def test_votacao_basica(self):
        # Simulação de dados de votação
        dados_mock = [
            ["Eleitor", "Voto"],
            ["João", "Bitcoin"],
            ["Maria", "Ethereum"],
            ["Ana", "Bitcoin"]
        ]

        # Simular função de planilha que retorna os dados
        def mock_getDataRange():
            return dados_mock

        # Substituir a função de planilha real pela função mock
        SpreadsheetApp = unittest.mock.Mock()
        SpreadsheetApp.getActiveSpreadsheet.return_value.getSheetByName.return_value.getDataRange.return_value.getValues = mock_getDataRange

        # Chamar a função que está sendo testada
        resultados = processarVotacao()

        # Verificar o resultado esperado
        self.assertEqual(resultados['Bitcoin'], 2)
        self.assertEqual(resultados['Ethereum'], 1)

if __name__ == '__main__':
    unittest.main()