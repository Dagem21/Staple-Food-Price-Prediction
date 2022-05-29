beforeEach(() => {
    cy.visit('/login')
    cy.get('[data-cy=phone-number]').type('0911111111')
    cy.get('[data-cy=password]').type('12341234')
    cy.get('[data-cy=login]').click()
    cy.location().should((loc) => {
        expect(loc.pathname).to.eq('/')
    })
    cy.visit('/users')
})

it('030. Check admin with full privilege cant be removed', () => {
    cy.get('[data-cy=delete-1]').should('not.exist')
})