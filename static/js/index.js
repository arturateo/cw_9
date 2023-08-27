async function makeRequest(url, method = 'GET') {
    let headers = {};
    let response;
    if (method !== "GET") {
        headers = {
            'Authorization': `Token ${getCookie("token")}`,
            "Content-Type": "application/json",
        }
    }

    if (["POST", "PATCH", "PUT"].includes(method)) {
        response = await fetch(url, {
            "method": method,
            "headers": headers,
        });
    }
    else {
        response = await fetch(url, {
            "method": method,
            "headers": headers,
        });
    }

    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        throw error;
    }
}

async function onClickPhoto(event) {
    event.preventDefault();
    let target = event.target;
    let target_parent = target.parentElement
    let url = target_parent.href;
    let photoId = target_parent.dataset.photoId

    let method = "POST"
    if (target.classList.value.includes("fa-solid")) {
        method = "DELETE"
    }
    console.log(method)

    let response = await makeRequest(url, method);
    if (target.classList.value.includes("fa-regular")) {
        target.classList = "fa-solid fa-heart fa-2xl";
        target_parent.href = `/api/v1/favorites-photo/${photoId}/unfavorite/`
    } else {
        target.classList = "fa-regular fa-heart fa-2xl";
        target_parent.href = `/api/v1/favorites-photo/${photoId}/favorite/`
    }
    console.log(response)
}

async function onClickAlbum(event) {
    event.preventDefault();
    let target = event.target;
    let target_parent = target.parentElement
    let url = target_parent.href;
    let albumId = target_parent.dataset.albumId

    let method = "POST"
    if (target.classList.value.includes("fa-solid")) {
        method = "DELETE"
    }
    console.log(method)

    let response = await makeRequest(url, method);
    if (target.classList.value.includes("fa-regular")) {
        target.classList = "fa-solid fa-heart fa-2xl";
        target_parent.href = `/api/v1/favorites-albums/${albumId}/unfavorite/`
    } else {
        target.classList = "fa-regular fa-heart fa-2xl";
        target_parent.href = `/api/v1/favorites-albums/${albumId}/favorite/`
    }
    console.log(response)
}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function onLoad() {
    let favoritePhotos = document.getElementsByClassName("favoritesPhoto")
    for (let favoritePhoto of favoritePhotos) {
        favoritePhoto.addEventListener("click", onClickPhoto)
    }
    let favoriteAlbums = document.getElementsByClassName("favoritesAlbum")
    for (let favoriteAlbum of favoriteAlbums) {
        favoriteAlbum.addEventListener("click", onClickAlbum)
    }
}

window.addEventListener('load', onLoad)