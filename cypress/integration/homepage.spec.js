/// <reference types="cypress" />

import Chance from 'chance';
const chance = new Chance();

describe('Homepage', () => {

  const email = chance.email();

  beforeEach(() => {
    cy.visit('http://localhost:8080');
  });

  it('has a title', () => {
    cy.contains('The Tasting Experience');
  });

  it('subscribes a user', () => {
    cy.get('input[name=email]').type(email);
    cy.get('button[type=submit]').click();

    cy.contains('Thank you for your email subscription');
  });
});