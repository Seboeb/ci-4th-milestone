exports.openModal = modelId => {

  const modal = $('#' + modelId);

  $(modal).css({ display: 'flex' })
}

exports.closeModal = modelId => {
  const modal = $('#' + modelId);

  $(modal).css({ display: 'none' })
}