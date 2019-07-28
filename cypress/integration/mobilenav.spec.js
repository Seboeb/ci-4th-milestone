/// <reference types="cypress" />

describe('Mobile dashboard', () => {

  before(() => {
    cy.login();
  });

  beforeEach(() => {
    cy.viewport('iphone-6+');
    Cypress.Cookies.preserveOnce('sessionid');
    cy.visit('http://localhost:8080/dashboard/');
  });

  it('desktop version should not be visible', () => {
    cy.get('section.dashboard-card').should('not.be.visible');
    cy.get('section.watchlist-card').should('not.be.visible');
  });

  it('hamburger button should be visible', () => {
    cy.get('.mobile-menu-btn').should('be.visible');
  });

  it('mobile dashboard should not be visible without button press', () => {
    cy.get('.mobile-menu').should('not.be.visible');
  });

  it('mobile dashboard should be visible with button press', () => {
    cy.get('.mobile-menu-btn').click();
    cy.wait(1000);
    cy.get('.mobile-menu').should('be.visible');
  });

  after(() => {
    cy.visit('http://localhost:8080/accounts/logout');
  });
});