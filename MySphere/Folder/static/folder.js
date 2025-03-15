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

function makeFolder(path) {
    let folder = document.getElementById("folder-name").value
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