const ticketListRender = require('../../dev_panel/templates/handlebars/ticket_list.hbs');

exports.loadMoreTickets = (start, appType, query) => {

  fetch(window.location.origin + '/dashboard/?app=' + appType, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then(res => res.json())
    .then(resData => {
      const tickets = JSON.parse(resData.data);

      // Check if bug report or not
      tickets.map(ticket => {
        if (ticket.fields.ticket_type == 1) {
          ticket.bug = true;
        } else {
          ticket.bug = false
        }
      });


      const htmlString = ticketListRender(tickets);
      const loadMore = $('.load-more');
      $('.load-more').remove();
      $('.list').append(htmlString);
      $('.list').append(loadMore);
    });

}