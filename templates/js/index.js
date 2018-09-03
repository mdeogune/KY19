$(document).ready(function(){
	
	 $(window).on("load", function() {
         function hidePreloader() {
             var preloader = $('.spinner-wrapper');
			 $(".spinner").animate({left: '100%'},3000,function(){
             preloader.fadeOut(200);
			 });
         }
         hidePreloader();
     });
	 if ( $(window).width() > 1100) { 
    $("#aboutus-pull").click(function(){
        $(".page").animate({left: '-49.5%'},100);
		$(".pull").animate({opacity:'1'},50);
        $("#aboutus").animate({left: '20%'});
		$(this).animate({opacity:'0'},50);

    });
	
    $("#whyca-pull").click(function(){
        $(".page").animate({left: '-49.5%'},100);
		$(".pull").animate({opacity:'1'},50);
        $("#whyca").animate({left: '20%'});
		$(this).animate({opacity:'0'},50);

    });
	
	 $("#duties-pull").click(function(){
        $(".page").animate({left: '-49.5%'},100);
		$(".pull").animate({opacity:'1'},50);
        $("#duties").animate({left: '20%'});
		$(this).animate({opacity:'0'},50);

    });
	
	 $("#perks-pull").click(function(){
        $(".page").animate({left: '-49.5%'},100);
		$(".pull").animate({opacity:'1'},50);
        $("#perks").animate({left: '20%'});
		$(this).animate({opacity:'0'},50);

    });
	
	 $("#tnc-pull").click(function(){
        $(".page").animate({left: '-49.5%'},100);
		$(".pull").animate({opacity:'1'},50);
        $("#tnc").animate({left: '20%'});
		$(this).animate({opacity:'0'},50);

    });
	
	$("#contactus-pull").click(function(){
        $(".page").animate({left: '-49.5%'},100);
		$(".pull").animate({opacity:'1'},50);
        $("#contactus").animate({left: '20%'});
		$(this).animate({opacity:'0'},50);

    });
	
    $(".close").click(function(){
        $(".page").animate({left: '-49.5%'},100);
		$(".pull").animate({opacity:'1'},50);
		$(".login-modal-overlay").fadeOut(200);
    });
}

	if ( $(window).width() < 1100 && $(window).width() > 500) {      
     $("#aboutus-pull").click(function(){
        $(".page").animate({left: '-65%'},100);
		$(".pull").animate({opacity:'1'},50);
        $("#aboutus").animate({left: '20%'});
		$(this).animate({opacity:'0'},50);

    });
	
    $("#whyca-pull").click(function(){
        $(".page").animate({left: '-65%'},100);
		$(".pull").animate({opacity:'1'},50);
        $("#whyca").animate({left: '20%'});
		$(this).animate({opacity:'0'},50);

    });
	
	 $("#duties-pull").click(function(){
        $(".page").animate({left: '-65%'},100);
		$(".pull").animate({opacity:'1'},50);
        $("#duties").animate({left: '20%'});
		$(this).animate({opacity:'0'},50);

    });
	
	 $("#perks-pull").click(function(){
        $(".page").animate({left: '-65%'},100);
		$(".pull").animate({opacity:'1'},50);
        $("#perks").animate({left: '20%'});
		$(this).animate({opacity:'0'},50);

    });
	
	 $("#tnc-pull").click(function(){
        $(".page").animate({left: '-65%'},100);
		$(".pull").animate({opacity:'1'},50);
        $("#tnc").animate({left: '20%'});
		$(this).animate({opacity:'0'},50);

    });
	
	$("#contactus-pull").click(function(){
        $(".page").animate({left: '-65%'},100);
		$(".pull").animate({opacity:'1'},50);
        $("#contactus").animate({left: '20%'});
		$(this).animate({opacity:'0'},50);

    });
	
    $(".close").click(function(){
        $(".page").animate({left: '-65%'},100);
		$(".pull").animate({opacity:'1'},50);
		$(".login-modal-overlay").fadeOut(200);
    }); 
} 


	if ( $(window).width() < 500) {   
	  
     $("#aboutus-pull").click(function(){
        $(".page").animate({left: '-83%'},100);
		$(".pull").animate({opacity:'1'},50);
        $("#aboutus").animate({left: '15%'});
		$(this).animate({opacity:'0'},50);

    });
	
    $("#whyca-pull").click(function(){
        $(".page").animate({left: '-83%'},100);
		$(".pull").animate({opacity:'1'},50);
        $("#whyca").animate({left: '15%'});
		$(this).animate({opacity:'0'},50);

    });
	
	 $("#duties-pull").click(function(){
        $(".page").animate({left: '-83%'},100);
		$(".pull").animate({opacity:'1'},50);
        $("#duties").animate({left: '15%'});
		$(this).animate({opacity:'0'},50);

    });
	
	 $("#perks-pull").click(function(){
        $(".page").animate({left: '-83%'},100);
		$(".pull").animate({opacity:'1'},50);
        $("#perks").animate({left: '15%'});
		$(this).animate({opacity:'0'},50);

    });
	
	 $("#tnc-pull").click(function(){
        $(".page").animate({left: '-83%'},100);
		$(".pull").animate({opacity:'1'},50);
        $("#tnc").animate({left: '15%'});
		$(this).animate({opacity:'0'},50);

    });
	
	$("#contactus-pull").click(function(){
        $(".page").animate({left: '-83%'},100);
		$(".pull").animate({opacity:'1'},50);
        $("#contactus").animate({left: '15%'});
		$(this).animate({opacity:'0'},50);

    });
	
    $(".close").click(function(){
        $(".page").animate({left: '-83%'},100);
		$(".pull").animate({opacity:'1'},50);
		$(".login-modal-overlay").fadeOut(200);
    }); 
} 
})

 // Show overlay & Open modal
  
  $( ".login-modal-overlay" ).click(function() {
    $(this).fadeOut(200);
  });
  $( "#login" ).click(function() {
    $("#login-modal-overlay").fadeIn(200);
  });
  $( "#register" ).click(function() {
    $("#register-modal-overlay").fadeIn(200);
  });
  $(".login-modal").click(function(event) {
    event.stopPropagation();
  });
  
  
  // Input s

  $('input').blur(function() {
    var $this = $(this);
    if ($this.val())
      $this.addClass('used');
    else
      $this.removeClass('used');
  });
  
  
