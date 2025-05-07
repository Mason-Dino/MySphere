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

function deleteFile(path, filename) {
    if (confirm(`Do you want to delete ${filename}?`)) {
        fetch("https://mason-server.tailff82ee.ts.net/files/delete/", {
            method: "POST",
            body: JSON.stringify({
                path: path,
                file: filename
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8",
                'X-CSRFToken': csrftoken,
            }
            })
            .then((response) => response.json())
            .then((json) => {
                console.log(json);
                var oldURL = document.referrer;
                oldURL += "?refresh=true"

                window.location.href = oldURL

            })
            .catch(error => alert("Error:", error));
    }
}

function deleteFolder(path, shortPath) {
    if (confirm(`Do you want to delete ${shortPath} folder`)) {
        fetch("https://mason-server.tailff82ee.ts.net/folder/delete-folder/", {
            method: "POST",
            body: JSON.stringify({
                path: path
            }),
            headers: {
            "Content-type": "application/json; charset=UTF-8",
            'X-CSRFToken': csrftoken,
            }
        })
        .then((response) => response.json())
        .then((json) => {
            console.log(json);
            var oldURL = document.referrer;
            oldURL += "?refresh=true"

            window.location.href = oldURL
        })
    }
}

function renameFile(path, filename) {
    console.log(path, filename)

    newName = prompt(`What is the new name for ${filename}`)

    fetch("https://mason-server.tailff82ee.ts.net/files/rename/", {
        method: "POST",
        body: JSON.stringify({
            path: path,
            file: filename,
            newName: newName
        }),
        headers: {
        "Content-type": "application/json; charset=UTF-8",
        'X-CSRFToken': csrftoken,
        }
    })
    .then((response) => response.json())
    .then((json) => {
        console.log(json);
        var oldURL = document.referrer;
        oldURL += "?refresh=true"

        window.location.href = oldURL
    })
}

function menu() {
    if (document.getElementById("add-menu").style['display'] === "block") {
        document.getElementById("add-menu").style = "display: none";
    }
    else {
        document.getElementById("add-menu").style = "display: block"
    }
}

function makeFolderMenu(path) {
    folder = prompt("Name of Folder: ")
    folder = String(folder).replaceAll(" ", "-")

    if (folder == '') {
        alert("Folder not made.")
        return
    }
    
    fetch("https://mason-server.tailff82ee.ts.net/folder/make-folder/", {
        method: "POST",
        body: JSON.stringify({
            path: path,
            name: folder
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8",
            'X-CSRFToken': csrftoken,
        }
        })
        .then((response) => response.json())
        .then((json) => {
            console.log(json);
            location.reload();
        });
}

function openFileBox(path) {
    let input = document.getElementById("file-input-menu")
    input.onchange = function () {
        if (input.files.length > 0) {
            console.log("hey")
            uploadFileMenu(path)
        }
    }

    input.click()
}

function uploadFileMenu(path) {
    var fileInput = document.getElementById("file-input-menu");
    var formData = new FormData();
    
    if (fileInput.files.length === 0) {
        alert("Please select a file before uploading.");
        return;
    }

    for (const file of fileInput.files) {
        formData.append("files[]", file); // Match the Django view's getlist('files[]')
    }
    
    formData.append("csrfmiddlewaretoken", csrftoken); // CSRF token
    formData.append("path", path)

    document.getElementById("loader").style = "display: block;"
    document.getElementById("add-menu").style = "display: none;"

    fetch("/upload/file-upload/", {  // Make sure this matches your Django URL
        method: "POST",
        body: formData,
    })
    .then(response => response.json())
    .then(json => {
        console.log(json);
        alert("File Uploaded");
        document.location.href += '?refresh=true';
        document.getElementById("loader").style = "display: none;"
    })
    .catch(error => console.error("Error:", error));
}

/*
function openFolderBox(path) {
    let input = document.getElementById("folder-input-menu")
    input.onchange = function () {
        if (input.files.length > 0) {
            uploadFolderMenu(path)

            for (file of input.files) {
                console.log(file)
            }
        }
    }

    input.click()
}

function uploadFolderMenu(path) {
    const input = document.getElementById("folder-input-menu"); // <input type="file" multiple>
    const formData = new FormData();
    for (const file of input.files) {
        formData.append("files[]", file); // Match the Django view's getlist('files[]')
    }
    formData.append("path", "/your/target/path");
    formData.append("csrfmiddlewaretoken", csrftoken);

    fetch("/upload/file-upload/", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(json => console.log(json))
    .catch(err => console.error(err));

}
    */