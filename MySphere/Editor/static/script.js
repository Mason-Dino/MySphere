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
    filename = filename.replaceAll(".", "-");
    filename = filename.replaceAll(" ", "-");
    filename = `${filename}.sh`

    content = editor.getValue()
    

    fetch("https://mason-server.tailff82ee.ts.net/edit/saveFile/", {
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