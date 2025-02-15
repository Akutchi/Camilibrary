const Menu = document.getElementById ("menu");
Menu.style.fontSize = "0px";

function ToggleMenu () {

    const Menu = document.getElementById ("menu");

    if (Menu.style.width == "0rem" || Menu.style.width == "") {

        Menu.style.transition = "1s ease-in-out";

        Menu.style.width = "8rem";
        Menu.style.fontSize = "16px";
        Menu.style.visibility = "visible";

    } else {

        Menu.style.width = "0rem";
        Menu.style.fontSize = "0px";
        Menu.style.visibility = "hidden";
    }
}

// from https://docs.djangoproject.com/en/3.2/ref/csrf/#how-to-use-it
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

function CreateList (List) {

    const ParentDiv = document.createElement ("div");

    for (Book of List ["info"]) {

        const div = document.createElement ("div");

        const p = document.createElement ("p");
        p.innerHTML = Book.title;

        const img = document.createElement ("img");
        img.setAttribute ('src', 'static/' + Book.image);

        div.append (img, p);
        ParentDiv.append (div);
    }

    return ParentDiv;
}

async function BookSearch () {

    inputContent = document.getElementById ("SearchBar").value;

    Req = {

        method  : "POST",
        headers : {
            'Content-Type' : "application/json",
            'Accept' : "application/json",
            'X-CSRFToken': getCookie('csrftoken')
        },
        body : JSON.stringify (inputContent)
    }

    const List = await fetch ("http://localhost:8000/search", Req)
    .then (response => {return response.json ()});
    document.getElementById ("SearchWrapper").replaceChildren (CreateList (List));

}
