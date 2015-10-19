//TODO: closure compiler to minify js
$(document).ready(function() {
// se eliminan las propiedades de las imagenes de los post y se agregan clases, para ajustarlas al diseño del template.
    // Reemplazo de imagenes en homepage
    $('#news .news_list_item').find('img').each(function(){
        newsImage = $('<div>');
        newsImage.attr('itemprop', 'image');
        newsImage.attr('style', 'background: url(' + $(this).attr('src') + ') no-repeat center center; background-size: cover;')
        newsImage.addClass('newsImage');
        $(this).parents('.news_list_content').prepend(newsImage);
        $(this).remove();
    });

    $('iframe').each(function(){
        $(this).addClass('embed-responsive-item');
    });

    $('.news_list_item .content').find('img').each(function(){
            newsImage = $('<img>');
            newsImage.attr('src', $(this).attr('src'));
            newsImage.attr('itemprop', 'image');
            newsImage.addClass('newsImage img img-responsive');
            //$(this).parents('.news_list_content').prepend(newsImage);
            $(this).hide();
        });

    $('.news_list_block .content').find('img').each(function(){
            newsImage = $('<img>');
            newsImage.attr('src', $(this).attr('src'));
            newsImage.attr('itemprop', 'image');
            newsImage.addClass('newsImage img img-responsive');
            //$(this).parents('.news_list_content').prepend(newsImage);
            $(this).hide();
        });


    // activa el slider
    //$('.carousel').carousel();
    $('#carousel').find('img').each(function(){
        var urlImg = $(this).attr('src');
        var styles = {
            background: 'url(' + urlImg + ')',
            backgroundSize: 'cover',
            backgroundPosition: '50% 50%'
            };
        $(this).parent().css(styles);
        $(this).hide();
    });
    $('#carousel').find('.item').first().addClass('active');
    resize();
});

$(window).resize(function() {
    resize();
});

function resize(){
    var h = $(window).height();
    ch = h - 100;
    wr = h;
    $('#carousel').css({height: ch + 'px'});
    $('#carousel .item').css({height: ch + 'px'});
    $('.wraper').css({minHeight: wr + 'px'});
};


jQuery(document).ready(function ($) {


    var slideCount = $('#banner-content div').length;
	if (slideCount > 1){
	$('.banner-item').hide();
	$('.banner-item.active').show();
   setInterval(function () {
        moveRight();
    }, 5000);
    }


	$('#banner').css({ width: '100%', maxHeight: '250px' });

    $('#banner-content.banner-item:last').prependTo('#banner-content');

    function moveLeft() {
        $('#banner ul').animate({
            left: + slideWidth
        }, 200, function () {
            $('#banner ul li:last-child').prependTo('#banner ul');
            $('#banner ul').css('left', '');
        });
    };

    function moveRight() {
        var slideWidth = $('#banner').width();
        var slideHeight = $('#banner').height();
        $('.banner-item.active').animate({
            left: - slideWidth
        }, 800, function () {
            var div = $('#banner-content div:first-child');
            div.appendTo('#banner-content');

            $('.banner-item.active').removeClass('active');
            div.siblings().hide();
            div.addClass('active');
            div.show();
         });
    };

    $('a.control_prev').click(function () {
        moveLeft();
    });

    $('a.control_next').click(function () {
        moveRight();
    });

});

$(document).ready(function() {
   $('.content').find('img').each(function(){
        var max = $(this).parents('.content').width();
        var oldStyle = $(this).attr('style');
        $(this).attr('style', oldStyle + '; height: auto; margin: 10px;');
        $(this).addClass('img img-responsive img-thumbnail');
    });

    $('table').each(function(){
        $(this).addClass('table table-bordered table-striped table-hover');
    });
});
