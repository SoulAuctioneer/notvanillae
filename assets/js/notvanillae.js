$( document ).ready(function() {

    // PJAX

    $(document).pjax('a[data-pjax]', '#content');

    $(document).on('pjax:timeout', function() {
        return false;
    });

    $(document).on('pjax:send', function() {
        $('#content').fadeTo(0, 0.3);
        $('#primary_nav').find('li a').removeClass('active');
        $('#spinner').css('display','block').animate({'opacity':1},100,'swing');
    });

    $(document).on('pjax:success', function() {
        $('#content').fadeTo('slow', 1, show_active_nav);
        $('#spinner').animate({'opacity':0},100,'swing',function (){$(this).css('display','none')});
    });

    $(document).on('pjax:complete', function() {
        if (window.ga) {
            ga('set', 'location', window.location.href);
            ga('send', 'pageview');
        }
    });

    function show_active_nav() {
        $('#header-nav-menu-' + active_nav).addClass('active');
        switch (active_nav) {
            case 'presentations':
                $('#header-nav-menu-home').removeClass('active');
                break;
            default:
                $('#header-nav-menu-presentations').removeClass('active');
        }
    }


    // Signed-in notice
    $.ajax({
        url: url_canonical_secure + '/signin_notice',
        success: function(data) {
            $('#signin_notice').html(data).fadeTo(500, 1);
        }
    });


    // Socialite
    Socialite.load($('#footer-share'));


    // External scripts are loaded asynchronously. Execute dependent functions
    $.each(deferred_functions, function(index, value) {
        value();
    });

});
