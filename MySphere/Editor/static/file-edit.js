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

function saveFile() {
    var filename = document.getElementById("file-name").value;
    filename = filename.replaceAll(" ", "-");

    content = editor.getValue()
    

    fetch("https://mason-server.tailff82ee.ts.net/edit/edit-saveFile/", {
    method: "POST",
    body: JSON.stringify({
        filename: filename,
        content: content
    }),
    headers: {
        "Content-type": "application/json; charset=UTF-8",
        'X-CSRFToken': csrftoken,
    }
    })
    .then((response) => response.json())
    .then((json) => {
        console.log(json);
        alert(json['message'])
    });
}

function runFile() {
    var filename = document.getElementById("file-name").value;

    content = editor.getValue()
    

    fetch("https://mason-server.tailff82ee.ts.net/edit/runFile/", {
    method: "POST",
    body: JSON.stringify({
        filename: filename
    }),
    headers: {
        "Content-type": "application/json; charset=UTF-8",
        'X-CSRFToken': csrftoken,
    }
    })
    .then((response) => response.json())
    .then((json) => {
        console.log(json);
        if (json['result'] === 0) {
            alert(`${filename} successfully run`)
        }
        else {
            alert(`ERROR: ${filename} did not successfully run`)
        }
    });
}