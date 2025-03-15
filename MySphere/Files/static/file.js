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