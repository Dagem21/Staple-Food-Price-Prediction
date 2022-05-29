beforeEach(() => {
    cy.visit('/register')
})

it.skip('001. registers users as Farmer', () => {
    cy.get('[data-cy=phone-number]').type('0911111111')
    cy.get('[data-cy=username]').type('user123')
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=confirm-password]').type('12345678')
    cy.get('[data-cy=usertype]').select('Farmer')
    cy.get('[data-cy=register]').click()
    cy.get('[data-cy=message]').contains('Registration completed!')
})


it.skip('002. registers users as Economist', () => {
    cy.get('[data-cy=phone-number]').type('0911111112')
    cy.get('[data-cy=username]').type('user123')
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=confirm-password]').type('12345678')
    cy.get('[data-cy=usertype]').select('Economist')
    cy.get('[data-cy=register]').click()
    cy.get('[data-cy=message]').contains('Registration completed!')
})