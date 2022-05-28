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

it('039. Check recommendations with valide inputs', () => {
    cy.get('[data-cy=search]').type('Addis Ababa{enter}')
    cy.get('[data-cy=table]').parent()
        .within($tr => {
            cy.get('[data-cy=location]').contains('Addis Ababa')
        })
})