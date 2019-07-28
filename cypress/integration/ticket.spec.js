/// <reference types="cypress" />

import Chance from 'chance';
const chance = new Chance();


describe('Ticket view', () => {

  before(() => {
    cy.login();
  });

  beforeEach(() => {
    Cypress.Cookies.preserveOnce('sessionid');
    cy.visit('http://localhost:8080/dashboard/');
    cy.get('.ticket-list-item').first().click();
  });

  it('should show a ticket view', () => {
    cy.url().should('contain', 'tickets');
  });

  it('should make a comment', () => {
    const comment = chance.sentence({ word: 20 });

    // Make and submit comment
    cy.get('#comment-form').within(($form) => {
      cy.get('textarea').type(comment);
      cy.get('button[type=submit]').click();
    })
    cy.contains(comment);
  });

  it('should add the ticket to the watchlist', () => {
    // Click watchlist button twice
    cy.get('button.watchlist').click();
    cy.get('button.watchlist').should('have.class', 'active');
    cy.get('button.watchlist').click();
    cy.get('button.watchlist').should('not.have.class', 'active');
  });

  it('should make a donation for a feature request', () => {
    // Go to dev panel
    cy.visit('http://localhost:8080/dashboard/');

    // Search and select a feature request
    cy.get('.controls').within(() => {
      cy.get('input[type=text]').type('feature');
    });
    cy.wait(500);
    cy.get('.ticket-list-item').first().click();

    // make donation
    cy.contains('Donate').click();
    cy.get('#payment-form').within(($form) => {
      cy.root().should('be.visible');
      cy.get('[type=radio]').check('custom', { force: true });
      cy.get('input[name="custom_amount"]').type(25.49);
      cy.get('input[name="credit_card_number"]').type(4242424242424242);
      cy.get('input[name="cvv"]').type(111);
      cy.get('select[name="expiry_year"]').select('2020');
      cy.get('button[type=submit]').click();
    });
    cy.wait(2000);
    cy.contains('You have successfully paid!');

  });

  after(() => {
    cy.visit('http://localhost:8080/accounts/logout');
  });

});