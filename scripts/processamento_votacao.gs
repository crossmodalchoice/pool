function processarVotacao() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Votos');
  var dados = sheet.getDataRange().getValues();

  var votos = {}; // Armazena os votos de cada token
  var totalEleitores = dados.length - 1;

  // Processar cada linha de votos
  for (var i = 1; i < dados.length; i++) {
    var voto = dados[i];
    var tokenVotado = voto[1];  // Supondo que a coluna 2 tenha os tokens votados
    
    if (!votos[tokenVotado]) {
      votos[tokenVotado] = 0;
    }
    votos[tokenVotado]++;
  }

  // Aplicar o método STV (Single Transferable Vote)
  var vencedores = calcularVencedoresSTV(votos, totalEleitores);

  return vencedores;
}

function calcularVencedoresSTV(votos, totalEleitores) {
  var vencedores = [];
  var quota = Math.floor(totalEleitores / 2) + 1;

  for (var token in votos) {
    if (votos[token] >= quota) {
      vencedores.push(token);
    }
  }

  return vencedores;
}