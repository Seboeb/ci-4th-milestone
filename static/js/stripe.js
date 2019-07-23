$(function () {
  $("#payment-form").submit(function () {
    var form = this;
    console.log(this)
    var card = {
      number: $("#credit_card_number").val(),
      expMonth: $("#expiry_month").val(),
      expYear: $("#expiry_year").val(),
      cvc: $("#cvv").val()
    };

    Stripe.createToken(card, function (status, response) {
      if (status === 200) {
        $("#credit-card-errors").hide();
        $("#stripe_id").val(response.id);

        // Prevent the credit card details from being submitted
        // to our server
        $("#credit_card_number").removeAttr('name');
        $("#cvv").removeAttr('name');
        $("#expiry_month").removeAttr('name');
        $("#expiry_year").removeAttr('name');

        form.submit();
        console.log('submitting!!')
      } else {
        $("#stripe-error-message").text(response.error.message);
        $("#credit-card-errors").show();
        $("#validate_card_btn").attr("disabled", false);
      }
    });
    return false;
  });
});

// Custom amount donation eventlistener
$(document).ready(function () {
  $('input[id=custom]').change(
    function () {
      if (this.checked) {
        $('#custom_amount_container').show();
      }
    });

  $('input[type=radio]').change(
    function () {
      if ($(this).attr('id') != 'custom' && $('#custom_amount_container').is(':visible')) {
        $('#custom_amount_container').hide();
      }
    });

})



