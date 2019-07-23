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