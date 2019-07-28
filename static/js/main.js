const modal = require('./modal');
const devPanel = require('./devPanel');
const ticket = require('./ticket');
const forms = require('./forms');

// Initialize input and textarea counters
forms.initCounter();
forms.initFormChecks();

// ----------------------------------------------------------------------------- EXPORTS
exports.openModal = modal.openModal;
exports.closeModal = modal.closeModal;
exports.loadMoreTickets = devPanel.loadMoreTickets;
exports.searchInitialTickets = devPanel.searchInitialTickets;
exports.showMenu = devPanel.showMenu;
exports.closeMenu = devPanel.closeMenu;
exports.toggleUpvote = ticket.toggleUpvote;
exports.toggleWatchlist = ticket.toggleWatchlist;