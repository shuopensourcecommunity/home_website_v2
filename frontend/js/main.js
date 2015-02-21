/*
  只是为了发布第一版，以下代码没什么用，随便删 = =
*/

$(function() {
    console.log('(*´∀`)~♥ 上海大学开源社区');

    var showAboutUs = function() {
    	var offset = -472 / 2;

    	$('.wrapper').delay(800).animate({
    		height: 472,
    		marginTop: offset
    	}, 500, function () {
    		$('#about-us').fadeIn(500);
    	});
    };

    var theater = new TheaterJS();

    theater.describe('comingSoon', {
    	speed: 0.6,
    	accuracy: 0.7,
    	invincibility: 2
    }, '#coming-soon');

    theater
    	.write('comingSoon:NEW WEBSITE COMING SOON...')
    	.write(showAboutUs);
});