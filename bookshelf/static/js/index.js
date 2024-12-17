function Move (event) {

    const TagList = document.getElementById ("TagList");
    const w = TagList.clientWidth;
    const over = TagList.scrollWidth - w;

    let dx_obj = {}
    if (event.id == "LeftArrow") {
        dx_obj = {"comp": x => {return x > 0}, "dx": -100, "born": 0};

    } else if (event.id == "RightArrow") {
        dx_obj = {"comp": x => {return x < over}, "dx": 100, "born": over};
    }

    Has_Not_Achieved_Born = dx_obj ["comp"] (TagList.scrollLeft += dx_obj ["dx"]);

    if(Has_Not_Achieved_Born) {
        TagList.scrollLeft += dx_obj ["dx"];

    } else {
        TagList.scrollLeft = dx_obj ["born"];
    }
}

