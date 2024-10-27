function atualizarGoogleSite() {
  var site = SitesApp.getSite('URL_DO_SITE_GOOGLE');
  var paginaResultados = site.getChildByName('Resultados');
  
  var resultados = processarVotacao();
  
  var conteudo = 'Resultados da votação:\n';
  for (var token in resultados) {
    conteudo += 'Token: ' + token + ' - Votos: ' + resultados[token] + '\n';
  }
  
  paginaResultados.setHtmlContent('<pre>' + conteudo + '</pre>');
  Logger.log('Site atualizado com sucesso!');
}