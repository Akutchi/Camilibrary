function Move (event) {

    let dx = 0;
    if (event.id == "LeftArrow") {
        dx = -100;

    } else if (event.id == "RightArrow") {
        dx = 100;
    }

    const TagList = document.getElementById ("TagList");
    const w = TagList.clientWidth;
    const over = TagList.scrollWidth - w;

    if(TagList.scrollLeft+dx < over) {
        TagList.scrollLeft += dx;

    } else {
        TagList.scrollLeft = over;

    }

    if(TagList.scrollLeft+dx > 0) {
        TagList.scrollLeft += dx;

    } else {
        TagList.scrollLeft = 0;
    }
}

