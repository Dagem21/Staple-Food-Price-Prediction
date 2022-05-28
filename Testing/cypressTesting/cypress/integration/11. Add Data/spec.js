beforeEach(() => {
    cy.visit('/login')
    cy.get('[data-cy=phone-number]').type('0911111111')
    cy.get('[data-cy=password]').type('12341234')
    cy.get('[data-cy=login]').click()
    cy.location().should((loc) => {
        expect(loc.pathname).to.eq('/')
    })
    cy.visit('/addData')
})

it('032. Check add data with valide inputs', () => {
    cy.get('[data-cy=month]').click().type('2019-01-15')
    cy.get('[data-cy=location]').select('Addis Ababa')
    cy.get('[data-cy=datatype]').select('Weather Data')
    cy.get('[data-cy=dataitem]').select('Precipitation')
    cy.get('[data-cy=value]').type('12.13456')
    cy.get('[data-cy=record]').click()
    cy.get('[data-cy=message]').contains('Data recorded!')

})