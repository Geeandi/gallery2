//alert("heyyyy...")
/*

x Break down page to modules

x Create a Navigation bar

x Create a login / register page.

x Display public albums on home page.

x Display all my albums ofter login.

x Upload images page.

x Edit / comment uploaded images in the album.

x Share a link / share album with other authorized registered users.

x Download album as Zip

x Download single image.



*/
let btns = document.getElementsByClassName("imginfo")
let modalbutton = document.getElementsByClassName("modal_button")
let modalimage = document.getElementById("my_image")
let modaltext = document.getElementById("modaltext")
var source;
var alt;

const arr = Array.from(btns);
let number_of_photos = arr.length;
let current_photo = 1;
arr.forEach(listener);

const modal_button_array = Array.from(modalbutton);
modal_button_array.forEach(modal_button_listener);

function listener(btn) {
        btn.addEventListener("click", (e) => {
        var trgt = e.target;
        current_photo = parseInt(trgt.accessKey);
        //var link = trgt.src.split("/");
        //t = link[link.lenght -1];
        //source = link[link.length - 1];
        source = trgt.src;
        modalimage.src = source;
        modaltext.innerText = trgt.alt;
        //alt = trgt.alt;
        //console.log(trgt)
    });
}

function modal_button_listener(btn) {
    btn.addEventListener("click", (e) => {
        let curr_btn = e.target.value;
        if(curr_btn == "previous") {
            if(current_photo > 0) {
                //console.log("you clicked the previous button....");
                let prev_img = arr[current_photo-1].children[0];
                modalimage.src = prev_img.src;
                modaltext.innerText = prev_img.alt;
                current_photo--;
            }
        } else if (curr_btn == "next") {
            if(current_photo < number_of_photos-1) {
                //console.log("you clicked the next button....");
                let next_img = arr[current_photo+1].children[0];
                modalimage.src = next_img.src;
                modaltext.innerText = next_img.alt;
                current_photo++;
            }
        }
    });
}

function saveImageInfo() {
    var x = this;
    console.log(e.target);
}