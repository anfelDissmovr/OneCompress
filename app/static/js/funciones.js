document.addEventListener('DOMContentLoaded', function() {
    // Referencias a los elementos
    const openPopupBtn = document.getElementById('boton-ejecutar');
    const closePopupBtn = document.getElementById('closePopupBtn');
    const popup = document.getElementById('popup');

    // Abrir el pop-up cuando se hace clic en el botón
    openPopupBtn.addEventListener('click', function() {
        fetch('/compressing', {
            method: 'POST',
        })
        .then(response => response.json())
        .then(data => {
            if (data.show_popup) {
                // Mostrar el pop-up si el servidor lo indica
                popup.style.display = 'flex';
            }
        })
        .catch(error => console.error('Error:', error));
    });

    // Cerrar el pop-up
    closePopupBtn.addEventListener('click', function() {
        popup.style.display = 'none'; // Oculta el pop-up
    });

    // Cerrar el pop-up si el usuario hace clic fuera del contenido
    popup.addEventListener('click', function(event) {
        if (event.target === popup) {
            popup.style.display = 'none'; // Ocultar el pop-up si se hace clic fuera
        }
    });
});


/* funcion para mostrar imagenes */

function showImage() {
    fetch('/showImgenes')
}