exports.toggleUpvote = ticketId => {
  fetch(window.location.origin + '/tickets/upvote/' + ticketId, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then(res => res.json())
    .then(resData => {
      if (resData.status !== 'ok') {
        console.error('Something went wrong while toggling upvote')
        return
      }

      // Set class
      if (resData.state === 'on') {
        $('.upvote').addClass('active');
      } else if (resData.state === 'off') {
        $('.upvote').removeClass('active');
      }

      // Update ticket
      $('.upvotes').html(resData.upvotes);

    })
}

exports.toggleWatchlist = ticketId => {
  fetch(window.location.origin + '/tickets/watchlist/' + ticketId, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then(res => res.json())
    .then(resData => {
      if (resData.status !== 'ok') {
        console.error('Something went wrong while toggling watchlist')
        return
      }

      if (resData.state === 'on') {
        $('.watchlist').addClass('active');
      } else if (resData.state === 'off') {
        $('.watchlist').removeClass('active');
      }
    })
}