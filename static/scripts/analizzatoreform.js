document.addEventListener("DOMContentLoaded", function(){
    //....
    var formfield =  document.getElementById("formfield")
    var btnavvia = document.getElementById("avvia");
    var btndisplay = document.getElementById("btn-display");
    var btntxt = document.getElementById('btn-txt');
    var preloaderdisp = document.getElementById('preloader-display');
    var fileInput = document.getElementById("fileInput");
    
    btnavvia.addEventListener("click", function () {
        // Disable the button
        if (fileInput.files.length > 0){
            btndisplay.classList.add('disabled')
            btntxt.style.display = "none";
            // Show the preloader
            preloaderdisp.style.display = 'inline-block';
        }
    })
    
    var btnexport = document.getElementById("btn-export");
    var btntxtexp = document.getElementById('btn-txt-exp');
    var preloaderexp = document.getElementById('preloader-export');
    
    btnexport.addEventListener("click", function () {
        // Disable the button
        if (fileInput.files.length > 0){
            // btnexport.disabled = true;
            btnexport.classList.add('disabled')
            btntxtexp.style.display = "none";
            // Show the preloader
            preloaderexp.style.display = 'inline-block';
            // Check for download completion every second
            // fetch('/analizzatore/',
            // {
            //     method: 'POST',
            //     // body: formData,
            // }).then(response => { 
            //     console.log("deu0")
            //     console.log(response)
            //     if (response.headers.get('X-Download-Complete') === 'true') {
            //         // The Excel file is ready for download
            //         // You can trigger the download process here
            //         // For example, create a download link or open a modal with a download button
            //         console.log("deu")
            //     } else {
                    
            //         // Handle other cases (e.g., loading spinner, error message)
            //     }
            // })
            // .catch(error => {
            //     // Handle any errors during the fetch request
            //     console.error('Error fetching Excel file:', error);
            // });
            // const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            // setInterval(function () {
            //     if (document.head.querySelector('meta[name="X-Download-Complete"]')) {
                    
            //         // Download is complete
            //         console.log("Download is complete!");
            //     } else {
            //         // Download is not complete yet
            //         console.log(document.head);
            //         console.log("Download is not complete yet.");
            //     }
            // }, 500);
        }
    })
    // window.addEventListener('', () => {
    //     // Lógica para esconder o modal aqui
    //     console.log("Download completed");
    // });
    // Check if the custom header is present
    // var metadata = document.head.querySelector('meta');
    
    // if (response.headers.get('X-Download-Complete')) {
    //     window.location.reload();
    // }

    // const isDownloadComplete = document.head.querySelector('meta[name="X-Download-Complete"]');

    // // Reload the page if the header is found
    // if (isDownloadComplete) {
    //     window.location.reload();
    // }
})


// function changeButton(){
//     var btndisplay = document.getElementById("btn-display");
//     var btntxt = document.getElementById('btn-txt');
//     var preloaderdisp = document.getElementById('preloader-display');
//     console.log("Hello")
//     // Disable the button
//     btndisplay.disabled = true;
//     btntxt.style.display = "none";
//     // Show the preloader
//     preloaderdisp.style.display = 'inline-block';
//     return submit()
// }

// // btndisplay.addEventListener("click", function () {
//     //     // Disable the button
//     //     btndisplay.disabled = true;
//     //     // Show the preloader
//     //     preloader.style.display = 'block';
//     // })
// formfield.addEventListener("submit", function (event) {
//     event.preventDefault()

//     const selectedFile = fileInput.files[0];
//     const formData = new FormData();
//     formData.append("file", selectedFile);
//     const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
//     formData.append("csrfmiddlewaretoken", csrfToken);
//     formData.append("action", "display");
//     fetch("", {
//         method: "POST",
//         body: formData,
//         mode: "no-cors",
//     })

//     // Disable the button
//     btndisplay.disabled = true;
//     btntxt.style.display = "none";
//     // Show the preloader
//     preloaderdisp.style.display = 'inline-block';
// })