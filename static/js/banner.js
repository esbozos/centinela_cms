jQuery(document).ready(function ($) {

    var slideCount = $('#banner ul li').length;
	var slideWidth = $('#banner ul li').width();
	var slideHeight = $('#banner ul li').height();
	var sliderUlWidth = slideCount * slideWidth;

	if (slideCount > 1){
	$('#banner li').hide();
	$('#banner li.active').show();
   setInterval(function () {
        moveRight();
    }, 5000);
    }




	$('#banner').css({ width: '100%', maxHeight: '250px' });

    $('#banner ul li:last-child').prependTo('#banner ul');

    function moveLeft() {
        $('#banner ul').animate({
            left: + slideWidth
        }, 200, function () {
            $('#banner ul li:last-child').prependTo('#banner ul');
            $('#banner ul').css('left', '');
        });
    };

    function moveRight() {

        $('#banner ul').animate({
            left: - slideWidth
        }, 800, function () {
            var li = $('#banner ul li:first-child').appendTo('#banner ul');
            $('#banner li.active').removeClass('active');
            li.addClass('active');
            li.show();
            li.siblings().hide();
            $('#banner ul').css('left', '');

         });
    };

    $('a.control_prev').click(function () {
        moveLeft();
    });

    $('a.control_next').click(function () {
        moveRight();
    });

});
