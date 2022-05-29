it('031. Check unauthorized admin cannot remove other users', () => {
    cy.visit('/login')
    cy.get('[data-cy=phone-number]').type('0911111114')
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=login]').click()
    cy.visit('/users')
    cy.location().should((loc) => {
        expect(loc.pathname).to.eq('/')
    })
})