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

    $('.news_list_item').find('img').each(function(){
            newsImage = $('<img>');
            newsImage.attr('src', $(this).attr('src'));
            newsImage.attr('itemprop', 'image');
            newsImage.addClass('newsImage img img-responsive');
            $(this).parents('.news_list_content').prepend(newsImage);
            $(this).hide();
        });




    $('.news_list_block').find('img').each(function(){
            newsImage = $('<img>');
            newsImage.attr('src', $(this).attr('src'));
            newsImage.attr('itemprop', 'image');
            newsImage.addClass('newsImage img img-responsive');
            $(this).parents('.news_list_content').prepend(newsImage);
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