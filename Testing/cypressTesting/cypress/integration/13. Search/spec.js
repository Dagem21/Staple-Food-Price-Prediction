beforeEach(() => {
    cy.visit('/')
})

it('036. Check search with valide inputs', () => {
    cy.get('[data-cy=search]').type('Teff')
    cy.get('[data-cy=search-btn]').click()
    cy.get('[data-cy=table]').parent()
        .within($tr => {
            cy.get('[data-cy=food-name]').contains('Teff')
        })
})