beforeEach(() => {
    cy.visit('/')
})

it('037. Check search with invalide inputs', () => {
    cy.get('[data-cy=search]').type('Tf')
    cy.get('[data-cy=search-btn]').click()
    cy.get('[data-cy=no-result]').contains('No search results were found!')
})

it('038. Check search with empty search field', () => {
    cy.get('[data-cy=search-btn]').click()
    cy.get('input:invalid').should('have.length', 1)
})