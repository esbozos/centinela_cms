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