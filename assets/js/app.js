/* Google Analytics */

(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-1520906-4', 'pajamaninja.com');
ga('send', 'pageview');

$( document ).ready(function() {

    // PJAX

    $(document).pjax('a[data-pjax]', '#content');

    $(document).on('pjax:timeout', function() {
        return false;
    });

    $(document).on('pjax:send', function() {
        $('#content').fadeTo(100, 0.5);
        $('#main-menu li a').removeClass('active');
        $('#spinner').css('display','block').animate({'opacity':1},100,'swing');
    });

    $(document).on('pjax:success', function() {
        $('#content').fadeTo(0, 0, function(){$(this).fadeTo(500, 1, show_active_nav)});
        $('#spinner').animate({'opacity':0},100,'swing',function (){$(this).css('display','none')});
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
});
