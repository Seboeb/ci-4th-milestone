def create_search_label(ticket):
    """
    Creates a search label or tag for the ticket
    """
    search_field = 'features ' + ticket.ticket_id + ' ' + ticket.user.first_name + \
        ' ' + ticket.user.last_name + ' ' + ticket.title
    return search_field.lower()
