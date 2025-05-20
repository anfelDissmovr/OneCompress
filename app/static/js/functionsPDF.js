document.addEventListener('DOMContentLoaded', function() {
    const pdfSplit = document.getElementById('button_SliptPdf');
    const formPdf = document.getElementById('formPdf')

    function handleSlipt() {
        fetch("/pdfCompress/spliting", { 
            method: 'POST'
        })
        .then(response => response.json())
        .then(data => {
            if (data.form === false) {
                formPdf.style.display = 'none';
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
    }

    pdfSplit.addEventListener('click', handleSlipt);
});
