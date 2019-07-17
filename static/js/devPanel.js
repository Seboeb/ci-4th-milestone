const ticketListRender = require('../../dev_panel/templates/handlebars/ticket_list.hbs');

exports.loadMoreTickets = (start, appType, query) => {
  fetch(window.location.origin + '/dashboard/?app=' + appType + '&start=' + start, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then(res => res.json())
    .then(resData => {

      const tickets = resData.data;

      // Check if bug report or not
      tickets.map(ticket => {
        if (ticket.ticket_type == 'bug_report') {
          ticket.bug = true;
        } else {
          ticket.bug = false
        }
      });

      const htmlString = ticketListRender(tickets);
      const loadMore = $('.load-more');
      $('.load-more').remove();
      $('.list').append(htmlString);

      if (resData.load_more) {
        $(loadMore).children().attr('onclick', `TE.loadMoreTickets(${start + 10}, "${appType}");`)
        $('.list').append(loadMore);
      }

      history.replaceState({}, "query", `?app=${appType}&limit=${start + 9}`);
    });

}