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

function restart(pid) {
    fetch("https://mason-server.tailff82ee.ts.net/process/pm2/update/", {
        method: "POST",
        body: JSON.stringify({
            task: "restart",
            id: pid
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
    })
}

function stop(pid) {            
    fetch("https://mason-server.tailff82ee.ts.net/process/pm2/update/", {
        method: "POST",
        body: JSON.stringify({
            task: "stop",
            id: pid
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

function start(pid) {            
    fetch("https://mason-server.tailff82ee.ts.net/process/pm2/update/", {
        method: "POST",
        body: JSON.stringify({
            task: "start",
            id: pid
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

function deleteProcess(pid) {
    fetch("https://mason-server.tailff82ee.ts.net/process/pm2/update/", {
        method: "POST",
        body: JSON.stringify({
            task: "delete",
            id: pid
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