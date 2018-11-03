$(document).ready(function() {

  var curPage = 1;
  var numOfPages = $(".skw-page").length;
  var animTime = 1000;
  var scrolling = false;
  var pgPrefix = ".skw-page-";
  var $body = $('body');
$body.removeClass().addClass('page-1');
  function pagination() {
    scrolling = true;

    
  //  $(pgPrefix + (curPage - 1)).addClass("inactive");
   // $(pgPrefix + (curPage + 1)).removeClass("active");
   $(pgPrefix + (1)).removeClass("active");
   $(pgPrefix + (2)).removeClass("active");
   $(pgPrefix + (3)).removeClass("active");
   $(pgPrefix + (4)).removeClass("active");
   $(pgPrefix + (5)).removeClass("active");
   $(pgPrefix + (6)).removeClass("active");
   $(pgPrefix + (7)).removeClass("active");
   $(pgPrefix + (8)).removeClass("active");
       $(pgPrefix + (8)).addClass("inactive");
	   $(pgPrefix + (1)).addClass("inactive");
	          $(pgPrefix + (2)).addClass("inactive");
	   $(pgPrefix + (3)).addClass("inactive");
	          $(pgPrefix + (4)).addClass("inactive");
	   $(pgPrefix + (5)).addClass("inactive");
	          $(pgPrefix + (6)).addClass("inactive");
	   $(pgPrefix + (7)).addClass("inactive");
    
	
	
	
	    $(pgPrefix + (curPage - 1)).addClass("inactive");
    $(pgPrefix + (curPage + 1)).removeClass("active");
	$(pgPrefix + curPage).removeClass("inactive").addClass("active");
	$body.removeClass().addClass('page-'+curPage);

    setTimeout(function() {
      scrolling = false;
    }, animTime);
  };

  function navigateUp() {
    if (curPage === 1) return;
    curPage--;
    pagination();
  };

  function navigateDown() {
    if (curPage === numOfPages) return;
    curPage++;
    pagination();
  };

  $(document).on("mousewheel DOMMouseScroll", function(e) {
    if (scrolling) return;
    if (e.originalEvent.wheelDelta > 0 || e.originalEvent.detail < 0) {
      navigateUp();
    } else { 
      navigateDown();
    }
  });

  $(document).on("keydown", function(e) {
    if (scrolling) return;
    if (e.which === 38) {
      navigateUp();
    } else if (e.which === 40) {
      navigateDown();
    }
  });
  

      $("#page1").click(function(){
        curPage = 1;
		pagination();
    });
	
	$("#page2").click(function(){
        curPage = 2;
		pagination();
    });
	$("#page3").click(function(){
        curPage = 3;
		pagination();
    });
	$("#page4").click(function(){
        curPage = 4;
		pagination();
    });
	$("#page5").click(function(){
        curPage = 5;
		pagination();
    });
	$("#page6").click(function(){
        curPage = 6;
		pagination();
    });
	$("#page7").click(function(){
        curPage = 7;
		pagination();
    });
	$("#page8").click(function(){
        curPage = 8;
		pagination();
    });
	
	
	
	
	
	
	
	
	
	
	
	
  

});
