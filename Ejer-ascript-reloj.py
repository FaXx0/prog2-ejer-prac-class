function onopen() { 
  DocumentApp.getUi() 
    .createMenu('
 ⚙
 Mis Funciones') 
    .addItem('
 🕒
 Insertar Fecha y Hora', 'insertarFechaYHora') 
    .addToUi(); 
} 

function insertarFechaYHora() { 
  var body = DocumentApp.getActiveDocument().getBody(); 
  var fecha = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), 
"yyyy-MM-dd HH:mm:ss"); 
  var parrafo = body.appendParagraph("Fecha y hora actual: " + fecha); 

  // Aplicar formato Arial tamaño 16 
  parrafo.setFontFamily("Arial"); 
  parrafo.setFontSize(16); 
} 