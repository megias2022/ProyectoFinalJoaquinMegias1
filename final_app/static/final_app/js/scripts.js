/*!
* Start Bootstrap - Blog Home v5.0.8 (https://startbootstrap.com/template/blog-home)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-blog-home/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
<script>
  // Obtenemos el elemento del DOM
  var element = document.getElementById("miElemento");

  // Definimos la función para cambiar el color de fondo
  function cambiarColor() {
    element.style.backgroundColor = "red";
  }

  // Asignamos la función como manejador de eventos para el clic
  element.addEventListener("click", cambiarColor);
</script>