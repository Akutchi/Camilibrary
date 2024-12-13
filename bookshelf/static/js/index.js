localStorage ["Tags"] = JSON.stringify({"active": []})

function ToogleTag (event) {

    clickedTag = event.id;

    if (localStorage ["Tags"] != undefined) {

        Tags = JSON.parse (localStorage ["Tags"]);

        if (!Tags ["active"].includes (clickedTag)) {
            Tags ["active"].push (clickedTag);
            TagObject = document.getElementById (clickedTag);
            TagObject.style.backgroundColor = "#d3d3d3";

        } else {
            Tags ["active"] = Tags ["active"].filter (item => item !== clickedTag);
            TagObject = document.getElementById (clickedTag);
            TagObject.style.backgroundColor = "#FFFFFF";
        }
        localStorage ["Tags"] = JSON.stringify (Tags);

    } else {

        localStorage ["Tags"] = JSON.stringify ({"active": [clickedTag]})
    }

    console.log (localStorage ["Tags"]);

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

    console.log (localStorage ["Tags"]);
}