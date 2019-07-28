exports.openModal = modelId => {
  const modal = $('#' + modelId);

  $(modal).css({ display: 'flex' });

  $('body').addClass('no-scroll');
}

exports.closeModal = modelId => {
  const modal = $('#' + modelId);

  $(modal).css({ display: 'none' });

  $('body').removeClass('no-scroll');
}