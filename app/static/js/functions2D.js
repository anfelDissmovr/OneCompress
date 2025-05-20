document.addEventListener("DOMContentLoaded", function () {
  // References
  const btnSettings = document.getElementById("Settings");
  const formSetting = document.getElementById("formSetting");
  const openPopupBtn = document.getElementById("boton-ejecutar");
  const cardImg = document.getElementsByClassName("card-img");
  const popup = document.getElementById("popup");
  const popupMessage = document.getElementById("popupMessage");
  const popupImage = document.querySelector("#popup img");
  const btnOops = document.querySelector(".oops");
  const btnSuccessfully = document.querySelector(".successfully");
  const btnUploadAll = document.getElementById("uploadAll");
  const formUpload = document.getElementById("formUpload");
  const optionsModal = document.getElementById("OptionsModal");
  const MessageUploadContainer = document.getElementById("upload_Message");
  const MessageUpload = document.getElementById("response_storage");
  const imgRespone = document.getElementById("response_img");
  const containerUploadBnt = document.getElementById("ContainerUploadStogare");
    const uploadingBnt = document.getElementById("uploadingBnt");

  // Functions
  if (btnSettings) {
    let loadedCount = 0;
    Array.from(cardImg).forEach((img) => {
      if (img.complete) {
        loadedCount++;
      } else {
        img.addEventListener("load", () => {
          loadedCount++;
          checkAllLoaded();
        });
      }
    });
    checkAllLoaded();

    console.log(loadedCount);
    console.log(cardImg.length);

    function checkAllLoaded() {
      if (loadedCount === cardImg.length) {
        openPopupBtn.classList.replace(
          "btn-compress",
          "btn-compressNoAnimation"
        );
        openPopupBtn.textContent = "Compress Image";
      }
    }
  }

  //hide or show settings
  function handleSettings() {
    formSetting.style.display =
      formSetting.style.display === "block" ? "none" : "block";
  }

  //close PopUp when click outside
  function handlePopup(event) {
    if (event.target === popup) {
      popup.style.display = "none";
    }
  }

  //Activate  Compress 2D
  function handleCompression() {
    openPopupBtn.textContent = "⌛Compressing...";
    openPopupBtn.classList.replace("btn-compressNoAnimation", "btn-compress");

    fetch("/compressing", {
      method: "POST",
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.show_popup) {
          openPopupBtn.textContent = "Compressed";
          openPopupBtn.classList.replace(
            "btn-compress",
            "btn-compressNoAnimation"
          );
          popupMessage.textContent = data.message;
          if (data.message.includes("Successfully ")) {
            popupImage.src = "../../static/img/download.png";
            btnSuccessfully.style.display = "flex";
            btnOops.style.display = "none";
          } else if (data.message.includes("Oops")) {
            popupImage.src = "../../static/img/alarm.png";
            btnOops.style.display = "flex";
            btnSuccessfully.style.display = "none";
          }
          popup.style.display = "flex";
        }
      })
      .catch((error) => console.error("Error:", error));
  }

  //Show or hide popup Upload Storage
  function handleUpload() {
    optionsModal.style.display = "none";
    formUpload.style.display = "block";
  }

  //Handel Upload Storage
  function handleFormUploadSubmit(e) {

    // btn-Upload.classList.replace('btn-Upload','btn-compress')
    
    
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);
    containerUploadBnt.style.display = 'none'
    uploadingBnt.style.display='block'

    

    fetch(form.action, {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        // Ocultar los otros modales
        formUpload.style.display = "none";
        optionsModal.style.display = "none";
       

        // Mostrar el mensaje del resultado
        popup.style.display = "flex";
        MessageUploadContainer.style.display = "block";
        MessageUpload.textContent = data.message;
        if (data.message.includes("complete")) {
          imgRespone.src = "../../static/img/verify.png";
        } else {
          imgRespone.src = "../../static/img/cancel.png";
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        MessageUpload.textContent = "An unexpected error occurred.";
        popup.style.display = "block";
        MessageUpload.style.display = "block";
      });
  }

  // Listeners
  btnSettings?.addEventListener("click", handleSettings);
  openPopupBtn?.addEventListener("click", handleCompression);
  popup?.addEventListener("click", handlePopup);
  btnUploadAll?.addEventListener("click", handleUpload);
  formUpload?.addEventListener("submit", handleFormUploadSubmit);
  formCompress?.addEventListener("submit", handleFormCompressSubmit);
});
