it('028. Check add admin with valide inputs as an unauthorized admin', () => {
    cy.visit('/login')
    cy.get('[data-cy=phone-number]').type('0911111114')
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=login]').click()
    cy.visit('/addAdmin')
    cy.location().should((loc) => {
        expect(loc.pathname).to.eq('/')
    })
})
