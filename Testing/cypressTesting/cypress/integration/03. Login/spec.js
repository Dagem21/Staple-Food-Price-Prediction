beforeEach(() => {
    cy.visit('/login')
})

it('014. Check login with all valid inputs', () => {
    cy.get('[data-cy=phone-number]').type('0911111111')
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=login]').click()
    cy.location().should((loc) => {
        expect(loc.pathname).to.eq('/')
    })
})