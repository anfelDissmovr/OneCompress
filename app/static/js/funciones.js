document.addEventListener('DOMContentLoaded', function() {
    // Referencias a los elementos del DOM
    const openPopupBtn = document.getElementById('boton-ejecutar');
    const popup = document.getElementById('popup');
    const popupMessage = document.getElementById("popupMessage");
    const popupImage = document.querySelector('#popup img'); 
    const btnOops = document.querySelector('.oops')
    const btnSuccessfully = document.querySelector('.successfully')

    // Función para manejar la solicitud de compresión y mostrar el pop-up
    function handleCompression() {
        fetch('/compressing', {
            method: 'POST',
        })
        .then(response => response.json())
        .then(data => {
            if (data.show_popup) {
                // Cambiar el texto del <h2> con el mensaje que llega desde Flask
                popupMessage.textContent = data.message;

                // Cambiar la imagen dependiendo del mensaje
                if (data.message.includes('Successfully ')) {
                    popupImage.src = '../../static/img/download.png'; // Imagen de éxito
                } else if (data.message.includes('Oops')) {
                    popupImage.src = '../../static/img/alarm.png'; // Imagen de advertencia
                    btnOops.style.display= 'flex';
                    btnSuccessfully.style.display = 'none'
                    
                } 
                // Mostrar el pop-up
                popup.style.display = 'flex';
            }
        })
        .catch(error => console.error('Error:', error));
    }

    // Abrir el pop-up cuando se hace clic en el botón
    openPopupBtn.addEventListener('click', handleCompression);

    // Cerrar el pop-up si el usuario hace clic fuera del contenido
    popup.addEventListener('click', function(event) {
        if (event.target === popup) {
            popup.style.display = 'none'; // Ocultar el pop-up si se hace clic fuera
        }
    });
});
