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

it('043. Check update password with valid inputs', () => {
    cy.get('[data-cy=old-password]').type('12341234')
    cy.get('[data-cy=new-password]').type('12345678')
    cy.get('[data-cy=confirm-password]').type('12345678')
    cy.get('[data-cy=update]').click()
    cy.get('[data-cy=message]').contains('Account updated!')
})