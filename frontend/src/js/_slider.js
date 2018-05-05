/* Slider box (work in progress)
 * 03/09/2015 by Andrew Errico
 */
$(function() {

    // slider type
    $t = "fade"; // opitions are fade and slide

  	//variables
    $f = 500,  // fade in/out speed
    $s = 1000,  // slide transition speed (for sliding carousel)
    $d = 7000;  // duration per slide

    $n = $('.slide-entry').length; //number of slides
    $w = $('.slide-entry').width(); // slide width
  	$c = $('.slider-box').width(); // container width
   	$ss = $n * $w; // slideshow width


      function timer() {
        $('.timer').animate({"width":$w}, $d);
        $('.timer').animate({"width":0}, 0);
    }


  // fading function
    function fadeInOut() {
      timer();
        $i = 0;
        var setCSS = {
            'position' : 'absolute',
            'top' : '0',
            'left' : '0'
        }

        $('.slide-entry').css(setCSS);

        //show first item
        $('.slide-entry').eq($i).show();


        setInterval(function() {
          timer();
            $('.slide-entry').eq($i).fadeOut($f);
            if ($i == $n - 1) {
                $i = 0;
            } else {
                $i++;
            }
            $('.slide-entry').eq($i).fadeIn($f, function() {
                $('.timer').css({'width' : '0'});
            });

        }, $d);

    }

    function slide() {
      timer();
        var setSlideCSS = {
            'float' : 'left',
            'display' : 'inline-block',
          	'width' : $c
        }
        var setSlideShowCSS = {
            'width' : $ss // set width of slideshow container
        }
        $('.slide-entry').css(setSlideCSS);
        $('.slideshow').css(setSlideShowCSS);


        setInterval(function() {
            timer();
            $('.slideshow').animate({"left": -$w}, $s, function(){
                // to create infinite loop
                $('.slideshow').css('left',0).append( $('.slide-entry:first'));
            });
        }, $d);

    }

    if ($t == "fade") {
        fadeInOut();

    } if ($t == "slide") {
        slide();

    } else {

    }
});
