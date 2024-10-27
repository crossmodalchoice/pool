function gerarRelatorio() {
  var sheetResultados = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Resultados');
  var sheetVotos = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Votos');
  
  var resultados = processarVotacao();
  
  sheetResultados.clear();  // Limpar resultados anteriores
  sheetResultados.appendRow(['Token', 'Votos']);
  
  for (var token in resultados) {
    sheetResultados.appendRow([token, resultados[token]]);
  }
  
  SpreadsheetApp.getUi().alert('Relatório de votação gerado com sucesso!');
}