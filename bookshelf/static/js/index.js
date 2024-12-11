function create_div (book_json) {

    div = document.createElement ("div");
    img = document.createElement ("img");
    img.setAttribute ("src", "");
    p = document.createElement ("p");
    p.innerHTML = book_json.Title + " écrit par ";

    div.appendChild (img);
    div.appendChild (p);

    return div;
}

if (localStorage['Page_Number'] == undefined) {
    localStorage['Page_Number'] = 0;
}

window.onscroll = async function(e) {
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {

        Req = {
            method : "POST",
            headers: {
                'Content-Type': 'application/json'
            },
        };

        const Response = await fetch (GET_NEXT_PAGE+(localStorage['Page_Number']+1).toString(), Req);
        localStorage['Page_Number']++;

        for (book in Response) {
            BookDiv = create_div (book);
            Wrapper = document.getElementsByClassName ("BookWrapper")
            Wrapper.appendChild (BookDiv)

        }

    }
};