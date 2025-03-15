function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

function uploadFile(path) {
    var fileInput = document.getElementById("upload-file");
    var formData = new FormData();
    
    if (fileInput.files.length === 0) {
        alert("Please select a file before uploading.");
        return;
    }
    
    formData.append("file", fileInput.files[0]); // Append file
    formData.append("csrfmiddlewaretoken", csrftoken); // CSRF token
    formData.append("path", path)

    document.getElementById("loader").style = "display: block;"

    fetch("/upload/file-upload/", {  // Make sure this matches your Django URL
        method: "POST",
        body: formData,
    })
    .then(response => response.json())
    .then(json => {
        console.log(json);
        alert("File Uploaded");
        document.getElementById("loader").style = "display: none;"
    })
    .catch(error => console.error("Error:", error));
}