localStorage ["Tags"] = JSON.stringify({"active": []})

const TagList = document.getElementById ("TagList");
TagList.classList.toggle ("Right_Blur", true);

function ToogleTag (event) {

    clickedTag = event.id;
    TagObject = document.getElementById (clickedTag);

    if (localStorage ["Tags"] == undefined) {

        localStorage ["Tags"] = JSON.stringify ({"active": [clickedTag]});
        TagObject.style.backgroundColor = "#d3d3d3";

        return;
    }

    Tags = JSON.parse (localStorage ["Tags"]);

    if (!Tags ["active"].includes (clickedTag)) {

        Tags ["active"].push (clickedTag);
        TagObject.style.backgroundColor = "#d3d3d3";

    } else {

        Tags ["active"] = Tags ["active"].filter (item => item !== clickedTag);
        TagObject.style.backgroundColor = "#FFFFFF";
    }

    localStorage ["Tags"] = JSON.stringify (Tags);

}

function ClearTags () {

    if (localStorage ["Tags"] == undefined) {
        return;
    }

    Tags = JSON.parse (localStorage ["Tags"]);
    if (Tags ["active"] != []) {
        for (T of Tags ["active"]) {
            TagObject = document.getElementById (T);
            TagObject.style.backgroundColor = "#FFFFFF";
        }
    }
    localStorage ["Tags"] = JSON.stringify ({"active": []});
}

function ToogleBlurryEnd () {

    const TagList = document.getElementById ("TagList");
    const w = TagList.clientWidth;
    const over = TagList.scrollWidth - w;

    TagList.classList.toggle ("Left_Blur", false);
    TagList.classList.toggle ("Right_Blur", false);
    TagList.classList.toggle ("Middle_Blur", true);

    if(TagList.scrollLeft == over) {

        TagList.classList.toggle ("Middle_Blur", false);
        TagList.classList.toggle ("Left_Blur", true);
        TagList.classList.toggle ("Right_Blur", false);


    } else if(TagList.scrollLeft == 0) {

        TagList.classList.toggle ("Middle_Blur", false);
        TagList.classList.toggle ("Left_Blur", false);
        TagList.classList.toggle ("Right_Blur", true);

    }
}