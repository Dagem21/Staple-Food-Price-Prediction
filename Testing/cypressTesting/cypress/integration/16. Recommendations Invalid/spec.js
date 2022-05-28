beforeEach(() => {
    cy.visit('/login')
    cy.get('[data-cy=phone-number]').type('0912121212')
    cy.get('[data-cy=password]').type('12341234')
    cy.get('[data-cy=login]').click()
    cy.location().should((loc) => {
        expect(loc.pathname).to.eq('/')
    })
    cy.visit('/recommendations')
})

it('040. Check recommendations with invalide location', () => {
    cy.get('[data-cy=search]').type('Addis{enter}')
    cy.get('[data-cy=no-result]').contains('Unknown location. Try again with a different location!')
})

it('041. Check recommendations with empty location', () => {
    cy.get('[data-cy=search]').type('{enter}')
    cy.get('input:invalid').should('have.length', 1)
})