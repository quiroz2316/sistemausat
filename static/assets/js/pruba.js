var elemento = document.getElementById("adelante");
var contador = 1;
var limit = 5;
var offset = 0;
var comboBox = document.getElementById("valor22");
comboBox.addEventListener("change", function () {
  limit = comboBox.value;
  var pElement = document.getElementById("contador");
  if (pElement.textContent.includes('1')) {
    $.ajax({
      url: "/semestres/b",
      type: "POST",
      data: { limit: limit, offset: offset },
      dataType: "html",
      success: function (response) {
        $("#contenido-dinamico").html(response);
      }
    });
    setTimeout(estadop, 30);
  } else {
    contador = 1;
    pElement.textContent = contador;
    $.ajax({
      url: "/semestres/b",
      type: "POST",
      data: { limit: limit, offset: 0 },
      dataType: "html",
      success: function (response) {
        $("#contenido-dinamico").html(response);
      }
    });
    setTimeout(estadop, 30);
  }



});
function mostrar(limit) {
  comboBox.value = limit
  $.ajax({
    url: "/semestres/b",
    type: "POST",
    data: { limit: limit, offset: offset },
    dataType: "html",
    success: function (response) {
      $("#contenido-dinamico").html(response);
    }
  });
  setTimeout(estadop, 30);
}
elemento.onclick = function () {
  var botonElement = document.getElementById("adelante");
  var pElement = document.getElementById("contador");

  var tabla = document.getElementById("tabla");
  var numeroFilas = tabla.rows.length;

  var cantidad = document.getElementById("cant").value;
  alert(parseInt(pElement.textContent, 10))
  if (parseInt(pElement.textContent, 10) <= cantidad/(numeroFilas-1)) {
    limit = comboBox.value;
    offset = limit * contador;
    contador++;
    pElement.textContent = contador;
    $.ajax({
      url: "/semestres/b",
      type: "POST",
      data: { limit: limit, offset: offset },
      dataType: "html",
      success: function (response) {
        $("#contenido-dinamico").html(response);
      }
    });
    setTimeout(estadop, 30);
  }



}
var elemento1 = document.getElementById("atras");
elemento1.onclick = retroceder;
function retroceder() {
  var botonElement = document.getElementById("atras");
  var pElement = document.getElementById("contador");
  limit = comboBox.value;

  if (contador == 1) {
    offset = 0;
    pElement.textContent = 1;
  } else if (contador > 1) {
    contador--;
    offset = (offset) - limit;
    pElement.textContent = contador;
  }
  var tabla = document.getElementById("tabla");
  var numeroFilas = tabla.rows.length;

  $.ajax({
    url: "/semestres/b",
    type: "POST",
    data: { limit: limit, offset: offset },
    dataType: "html",
    success: function (response) {
      $("#contenido-dinamico").html(response);
    }

  });



  setTimeout(estadop, 30);

}
function enviar_modal(id) {
  var ids = id
  var inputid = document.getElementById("idrecibir");
  inputid.value = ids;
  //alert(ids + " - " + inputid.value);
}



var estados = document.getElementById('estado');
var estado = document.getElementById('boton-estado');
// Código que deseas ejecutar para cada fila

function estadop() {
  var tabla = document.getElementById("tabla");
  var numeroFilas = tabla.rows.length;
  for (var i = 0; i < numeroFilas; i++) {
    var fila = tabla.rows[i + 1]; // El índice comienza en 0, por lo que la segunda fila tiene el índice 1
    var celda = fila.cells[6];
    var celda2 = fila.cells[3];
    var input = celda.querySelector("input");
    var valor = input.value;
    var formulario = document.createElement('form');
    var input = document.createElement('input');
    input.setAttribute('type', 'hidden');
    input.value = valor;
    input.name = "id";

    var boton = document.createElement("button");
    formulario.appendChild(input);
    formulario.appendChild(boton);
    if (celda2.textContent.includes('No vigente')) {
      boton.innerText = "Dar Alta";
      formulario.method = "POST";
      formulario.action = "/daralta_semestre";
      celda.appendChild(formulario);

    } else {
      boton.innerText = "Dar Baja";
      formulario.method = "POST";
      formulario.action = "/darbaja_semestre";
      celda.appendChild(formulario);

    }
  }
  alert(numeroFilas);
}
window.onload = estadop;


function cargarSemestreEditar(id, nom, fechaIn, fechaFin, est){
  document.getElementById("idEditar").value = id;
  document.getElementById("edit1").value = nom;
  var f1 = fechaIn.split("-");
  document.getElementById("edit2").value = f1[2]+"-"+f1[1]+"-"+f1[0];
  var f2 = fechaFin.split("-");
  document.getElementById("edit3").value = f2[2]+"-"+f2[1]+"-"+f2[0];
  document.getElementById("edit4").value = est;
}