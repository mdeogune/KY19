  $(document).ready(function() {

  $("#user-update").validate({

    rules: {

      college: "required",
      mobile_number: {
        required: true,
        minlength: 10,
        maxlength: 10,
      },
      whatsapp_number:{
        required: true,
        minlength: 10,
        maxlength: 10,
      }, 
      pincode: {
        required: true,
        minlength: 6,
        maxlength: 6,
      },
      reason:{
        required: true,
      },
    },

    submitHandler: function(form) {
    }
  });

}); 