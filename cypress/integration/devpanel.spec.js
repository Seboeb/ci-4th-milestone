/// <reference types="cypress" />

import Chance from 'chance';
const chance = new Chance();

describe('Development Panel', () => {

  before(() => {
    cy.login();
  });

  beforeEach(() => {
    Cypress.Cookies.preserveOnce('sessionid');
    cy.visit('http://localhost:8080/dashboard/');
  });

  it('should bring the user to the dev panel', () => {
    // Check user name
    cy.fixture('user').then(user => {
      cy.get('.dashboard-card').should('contain', user.firstName).should('contain', user.lastName);
    });
  });

  it('should open the feature request modal', () => {
    cy.get('#new_feature').should('not.be.visible');
    cy.contains('New feature request').click();
    cy.get('#new_feature').should('be.visible');
  });

  it('should open the bug report modal', () => {
    cy.get('#new_bug_report').should('not.be.visible');
    cy.contains('New bug report').click();
    cy.get('#new_bug_report').should('be.visible');
  });

  it('should create a new bug report and open it', () => {
    const title = chance.sentence({ words: 5 });
    const description = chance.sentence({ words: 25 });

    // Open modal
    cy.contains('New bug report').click();

    // Fill in the form
    cy.get('#bug-report-form').within(() => {
      cy.get('input[type="radio"]').check('recipe_community', { force: true });
      cy.get('input[name=title]').type(title);
      cy.get('textarea[name=description]').type(description);
      cy.get('button[type=submit]').click();
    })

    // Find and open new ticket
    cy.get('button').contains('Recipe community').click();
    cy.get('.controls').within(() => {
      cy.get('input[type=text]').type(title.slice(0, 5));
    })
    cy.wait(500);
    cy.get('.list').within(() => {
      cy.contains(title).click();
      cy.url().should('contain', 'tickets/');
      cy.contains(title);
    });
  });

  it('should create a new feature request and open it', () => {
    const title = chance.sentence({ words: 5 });
    const description = chance.sentence({ words: 25 });

    // Open modal
    cy.contains('New feature request').click();

    // Fill in the form
    cy.get('#feature-request-form').within(() => {
      cy.get('input[type="radio"]').check('finder_app', { force: true });
      cy.get('input[name=title]').type(title);
      cy.get('textarea[name=description]').type(description);
      cy.get('button[type=submit]').click();
    });

    // Find and open new ticket
    cy.get('.controls').within(() => {
      cy.get('input[type=text]').type(title.slice(0, 5));
    });
    cy.wait(500);
    cy.get('.list').within(() => {
      cy.contains(title).click();
      cy.url().should('contain', 'tickets/');
      cy.contains(title);
    })
  });

  after(() => {
    cy.visit('http://localhost:8080/accounts/logout');
  });
});