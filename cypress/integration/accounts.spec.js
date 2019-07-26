/// <reference types="cypress" />

import Chance from 'chance';
const chance = new Chance();

describe('Registration and login', () => {
  const email = chance.email();
  const pass = 'Mypassword123';

  beforeEach(() => {
    cy.viewport('macbook-13')
    cy.visit('http://localhost:8080/accounts/logout');
    cy.visit('http://localhost:8080');
  });

  it('it registers a new user', () => {
    cy.visit('http://localhost:8080/accounts/register');

    // Fill in the form
    cy.get('input[name=first_name]').type('John');
    cy.get('input[name=last_name]').type('Doe');
    cy.get('input[name=email]').type(email);
    cy.get('input[name=password1]').type(pass);
    cy.get('input[name=password2]').type(pass);
    cy.get('button[type=submit]').click();

    // Go to homepage and receive message
    cy.url().should('eq', 'http://localhost:8080/');
    cy.get('.message-container').children().should('contain', 'You have been registered!');
  });

  it('should log the user in', () => {
    cy.login()
  });

  it('cannot register a person with existing email', () => {
    cy.fixture('user').then(user => {
      cy.visit('http://localhost:8080/accounts/register');

      // Fill in the form
      cy.get('input[name=first_name]').type('John');
      cy.get('input[name=last_name]').type('Doe');
      cy.get('input[name=email]').type(user.email);
      cy.get('input[name=password1]').type(user.password);
      cy.get('input[name=password2]').type(user.password);
      cy.get('button[type=submit]').click();

      cy.contains('Email address must be unique').and('be.visible');
    });
  });

  after(() => {
    cy.visit('http://localhost:8080/accounts/logout');
  });
});