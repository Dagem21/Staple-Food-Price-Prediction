beforeEach(() => {
    cy.visit('/login')
    cy.get('[data-cy=phone-number]').type('0913131313')
    cy.get('[data-cy=password]').type('12341234')
    cy.get('[data-cy=login]').click()
    cy.location().should((loc) => {
        expect(loc.pathname).to.eq('/')
    })
    cy.visit('/notifications')
})

it('042. Check notifications can be deleted', () => {
    cy.get('[data-cy=delete-1]').click()
    cy.get('[data-cy=delete-1]').should('not.exist')
})