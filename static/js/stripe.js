$(function () {
  $("#payment-form").submit(function () {
    var form = this;
    let submit = true;

    // Clear error box
    $('#credit-card-errors').empty().hide();

    // Check if an amount is selected
    if ($(form).find('input:checked').length == 0) {
      $("#credit-card-errors").append(`<div id="payment-error-message">Please select an amount.</div>`);
      $("#credit-card-errors").show();
      submit = false;
    }

    if ($(form).find('input:checked').attr('id') === 'custom' && $('#custom_amount').val().length == 0) {
      $("#credit-card-errors").append(`<div id="payment-error-message">Please provide a custom amount.</div>`);
      $("#credit-card-errors").show();
      submit = false;
    }

    if (!submit) {
      return false;
    }


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

        $(form).find(':submit').attr('disabled', 'disabled');
        form.submit();
      } else {
        $("#credit-card-errors").append(`<div id="payment-error-message">${response.error.message}</div>`);
        $("#credit-card-errors").show();
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



