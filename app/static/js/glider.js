var sliders = document.querySelectorAll('.glider');
var dots = document.querySelectorAll('.dots');

for (var i = 0; i < sliders.length; i++) {
    var glide = new Glider(sliders[i], {
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: dots[i],
        draggable: true
    });
}

glide.mount();