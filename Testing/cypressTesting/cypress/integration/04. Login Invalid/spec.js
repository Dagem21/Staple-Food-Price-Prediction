beforeEach(() => {
    cy.visit('/login')
})

it('015. Check login with invalid phone number', () => {
    cy.get('[data-cy=phone-number]').type('091111')
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=login]').click()
    cy.get('[data-cy=error]').contains('Please provide a valid phone number!')
})

it('016. Check login with unregistered phone number', () => {
    cy.get('[data-cy=phone-number]').type('0911111133')
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=login]').click()
    cy.get('[data-cy=error]').contains('Unknown phone number or password!')
})

it('017. Check login with empty phone number', () => {
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=login]').click()
    cy.get('input:invalid').should('have.length', 1)
})

it('018. Check login with valid phone number but wrong password', () => {
    cy.get('[data-cy=phone-number]').type('0911111111')
    cy.get('[data-cy=password]').type('1234')
    cy.get('[data-cy=login]').click()
    cy.get('[data-cy=error]').contains('Unknown phone number or password!')
})

it('019. Check login with valid phone number but empty password', () => {
    cy.get('[data-cy=phone-number]').type('0911111111')
    cy.get('[data-cy=login]').click()
    cy.get('input:invalid').should('have.length', 1)
})