window.fbAsyncInit = function() {
      FB.init({
        appId            : '421719991556493',
        autoLogAppEvents : true,
        xfbml            : true,
        version          : 'v2.10'
      });
      FB.AppEvents.logPageView();
};
(function(d, s, id){
       var js, fjs = d.getElementsByTagName(s)[0];
       if (d.getElementById(id)) {return;}
       js = d.createElement(s); js.id = id;
       js.src = "//connect.facebook.net/en_US/sdk.js";
       fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));



function share(link){
  FB.ui({
    method:'share',
    href:link
  });
}

var idx=window.location.toString().indexOf("#_=_");
if (idx>0) {
  window.location = window.location.toString().substring(0, idx);
}