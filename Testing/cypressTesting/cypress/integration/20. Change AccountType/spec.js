beforeEach(() => {
    cy.visit('/login')
    cy.get('[data-cy=phone-number]').type('0912121212')
    cy.get('[data-cy=password]').type('12341234')
    cy.get('[data-cy=login]').click()
    cy.location().should((loc) => {
        expect(loc.pathname).to.eq('/')
    })
    cy.visit('/setting')
})

it('049. Check change account type', () => {
    cy.get('[data-cy=old-password]').type('12341234')
    cy.get('[data-cy=usertype]').select('Economist')
    cy.get('[data-cy=update]').click()
    cy.get('[data-cy=message]').contains('Account updated!')
})