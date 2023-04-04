$(function () {
    $('[data-link="anchor"]').on("click", function (e) {
        e.preventDefault();
        var id = $(this).attr('href'),
            top = $(id).offset().top - 35;
        $('body,html').animate({ scrollTop: top }, 1000);
    });
});

$(function () {
    let menu = $('[data-menu="mob"]'),
        btnMenu = $('[data-btn="menu"]');
    let btn_close = $('.btn-close')
    btn_close.on('click', function (e) {
        btnMenu.toggleClass('active');
    })
    btnMenu.on('click', function (e) {
        btnMenu.toggleClass('active');
        // menu.toggleClass('active');
        // $('.header').toggleClass('active');
    });
});

$(function () {
    let mobMenu = document.querySelector('.mob-menu')
    window.onload = () => {
       if (window.innerWidth < 1200) {
           mobMenu.classList.add('active')
       } else {
           mobMenu.classList.remove('active')
       }
    }
    addEventListener('resize', function (e) {
       if (window.innerWidth < 1200) {
           mobMenu.classList.add('active')
       } else {
           mobMenu.classList.remove('active')
       }
    });
});