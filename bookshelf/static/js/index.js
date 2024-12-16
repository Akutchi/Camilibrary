localStorage ["Tags"] = JSON.stringify({"active": []})

const Right_Blur = document.getElementById ("RightBlurDiv");
Right_Blur.classList.toggle ("Right_Blur", true);

function ToogleBlurryEnd () {

    const TagList = document.getElementById ("TagList");
    const w = TagList.clientWidth;
    const over = TagList.scrollWidth - w;

    const Left_Blur = document.getElementById ("LeftBlurDiv");
    const Right_Blur = document.getElementById ("RightBlurDiv");


    if(TagList.scrollLeft == over) {
        Left_Blur.classList.toggle ("Left_Blur", true);
        Right_Blur.classList.toggle ("Right_Blur", false);


    } else if(TagList.scrollLeft == 0) {
        Left_Blur.classList.toggle ("Left_Blur", false);
        Right_Blur.classList.toggle ("Right_Blur", true);

    } else {
        Left_Blur.classList.toggle ("Left_Blur", true);
        Right_Blur.classList.toggle ("Right_Blur", true);
    }
}