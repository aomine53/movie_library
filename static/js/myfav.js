
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie("csrftoken");

document.getElementById("createplaylist").addEventListener("click", () => {
    $("#addmodel").modal("show");
});
document.getElementById('close').addEventListener('click', () => {
    $('#addmodel').modal('hide')
})
document.getElementById('add').addEventListener('click', () => {
    let names = document.getElementById('fav_name').value;
    let isprivates = document.getElementById('isprivate').checked;
    $.ajax({
        method: "POST",
        url: "api/createfavoritelist",
        async: true,
        data: {
            csrfmiddlewaretoken: csrftoken,
            name: names,
            isprivate: isprivates,
        },
        success: function (result, status, xhr) {
            console.log(result);
            $('#addmodel').modal('hide')
            alert(result.message);
            window.location = window.location.href + "?eraseCache=true";
        },
        error: function (error_data) {
            console.log("error");
            alert("error");
            console.log(error_data);
        },
    });
})