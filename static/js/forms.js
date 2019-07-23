exports.initCounter = () => {
  // --------------------------------------------------------------------------- TEXTAREAS
  $('textarea').on('change keyup paste click', function () {
    const dataLength = $(this).attr('data-length');

    if (dataLength) {
      const counter = $(this).siblings('.counter');
      $(counter).html(`${$(this).val().length}/${dataLength}`);

      if ($(this).val().length > dataLength) {
        $(this).addClass('red')
        $(this).siblings('.counter').addClass('red')
      } else {
        $(this).removeClass('red')
        $(this).siblings('.counter').removeClass('red')
      }
    }
  });

  // --------------------------------------------------------------------------- TEXTINPUT
  $('input[type=text').on('change keyup paste click', function () {
    const dataLength = $(this).attr('data-length');

    if (dataLength) {
      const counter = $(this).siblings('.counter');
      $(counter).html(`${$(this).val().length}/${dataLength}`);

      if ($(this).val().length > dataLength) {
        $(this).addClass('red')
        $(this).siblings('.counter').addClass('red')
      } else {
        $(this).removeClass('red')
        $(this).siblings('.counter').removeClass('red')
      }
    }
  });
}

exports.initFormChecks = () => {
  // --------------------------------------------------------------------------- COMMENTS
  $("#comment-form").submit(function () {
    const form = this;
    const textarea = $('#comment-form').find('textarea');
    const dataLength = $(textarea).attr('data-length');

    if (!dataLength) {
      $("#comment-error-message").text('Something went wrong checking length');
      $("#comment-error-container").show();
      return false;
    }

    if ($(textarea).val().length > dataLength) {
      $("#comment-error-message").text('Your comment is too long. Please adjust.');
      $("#comment-error-container").show();
      return false;
    }

    $(form).find(':submit').attr('disabled', 'disabled');

    form.submit();
  });


  // --------------------------------------------------------------------------- TICKET
  function ticketFormValidation() {
    const form = this;
    const inputs = $(form).find('[data-length]');

    // Clear error box
    $(form).find('#form-error-container').empty().hide();

    // Validation
    let submit = true;
    $(inputs).each(function (index) {
      const dataLength = $(this).attr('data-length');

      if (!dataLength) {
        $(form).find("#form-error-container").append(`<div id="form-error-message">Something went wrong checking length</div>`);
        $(form).find("#form-error-container").show();
        submit = false;
        return;
      }

      if ($(this).val().length == 0) {
        let name = $(this).attr('name');
        name = name.charAt(0).toUpperCase() + name.slice(1);
        $(form).find("#form-error-container").append(`<div id="form-error-message">${name} is required.</div>`);
        $(form).find("#form-error-container").show();
        submit = false;
        return;
      }
      else if ($(this).val().length > dataLength) {
        let name = $(this).attr('name');
        name = name.charAt(0).toUpperCase() + name.slice(1);
        $(form).find("#form-error-container").append(`<div id="form-error-message">${name} is too long. Please adjust.</div>`);
        $(form).find("#form-error-container").show();
        submit = false;
        return;
      }

    })

    if (!submit) {
      return false;
    }

    $(form).find(':submit').attr('disabled', 'disabled');
    form.submit();

  }

  $("#bug-report-form").submit(ticketFormValidation);
  $("#feature-request-form").submit(ticketFormValidation);
  $("#edit-ticket-form").submit(ticketFormValidation);


  // --------------------------------------------------------------------------- PAYMENT
  /*
  * THIS FORM VALIDATION CAN BE FOUND IN THE STRIPE.JS FILE
  */

}