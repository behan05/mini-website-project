$('document').ready(function() {
    $('section article').each(function() {
        $(this).on('touchstart', function() {
            $(this).addClass('active')
        });
        $(this).on('touchend', function() {
            $(this).remveClass('active')
        });
    });
    $('#menu').on('click', function(e) {
        e.preventDefault();
        $(this).find('i').addClass('fa-spin');
        setTimeout(function() {
            $('#menu i').removeClass('fa-spin');
        }, 1000);
        $('#sidenav').addClass('open');
        $('body').addClass('open-overlay').prepend('<div class="overlay"></div>');
        $('.overlay, .close').on('click', function(e) {
            $(this).addClass('fa-spin');
            e.preventDefault();
            $('#sidenav').removeClass('open');
            $('body').removeClass('open-overlay');
            $('.overlay').remove();
            setTimeout(function() { $('.close').removeClass('fa-spin') }, 1000);
        });
    });
});