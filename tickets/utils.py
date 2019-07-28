def create_search_label(ticket):
    """
    Creates a search label or tag for the ticket
    """
    ticket_type = 'bugs' if ticket.ticket_type.name == 'bug_report' else 'features'
    search_field = '{0} {1} {2} {3} {4} {5}'.format(
        ticket_type, ticket.ticket_id, 'open', ticket.user.first_name, ticket.user.last_name, ticket.title)
    return search_field.lower()
