

$(document).ready(function(){
  $(".button-collapse").sideNav();
  $(".dropdown-button").dropdown();
  $(".collapsible").collapsible();
  $('.modal').modal();

  // if ($(window).width() < 992){
  //   $('.recent-side-nav-mobile').sideNav({
  //     menuWidth: '300px'
  //   });
  // }
  // else{
  //   $('.recent-side-nav').sideNav({
  //     menuWidth: 800,
  //     edge: 'right'
  //   });
  // }
  $('.main-side-nav').sideNav();
  // $('.nagrania-side-nav').sideNav({ edge: 'right'});

  $(function() {
    $('.card').hover(
        function() {
            $(this).find('> .card-image > img.activator').click();
        }, function() {
            $(this).find('> .card-reveal > .card-title').click();
        }
    );
  });

  $(function() {
    $('a[href*="#"]:not([href="#"]):not(".disqus")').click(function() {
      if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
        if (target.length) {
          $('html, body').animate({
            scrollTop: target.offset().top - 120
          }, 1000);
          return false;
        }
      }
    });
  });
  $(function() {
    $('a.disqus[href*="#"]:not([href="#"])').click(function() {
      if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
        if (target.length) {
          $('html, body').animate({
            scrollTop: target.offset().top - 210
          }, 1000);
          return false;
        }
      }
    });
  });
  //
  // $(document).ready(function(){
  //     $('ul.tabs').tabs();
  //   });

  $(function(){
    $epList = $('.episodes-list');
    if($epList.length){
      $epList.scroll();
      $epList.animate({
        scrollTop: $epList.scrollTop() + $('.current-episode').position().top
      })
    }
  });

  $(function(){
    $epToggle = $('.episodes-list-toggle');
    $epToggle.click(function(e){
      e.preventDefault();
      $('.episodes-list').slideToggle();
      $epToggle.children('i').toggleClass('fa-caret-down');
      $epToggle.children('i').toggleClass('fa-caret-up');
    });
  });

  $('.hero-carousel').carousel({fullWidth: true});
  $('.recent-episodes-carousel').carousel({fullWidth: true});

  setInterval(function(){
    $('.hero-carousel').carousel('next');
    $('.recent-episodes-carousel').carousel('next');
  }, 7000);

  $('.scrollspy').scrollSpy();

  $('.table-of-contents').pushpin({
    top: 0,
    offset: 70
  });

});
