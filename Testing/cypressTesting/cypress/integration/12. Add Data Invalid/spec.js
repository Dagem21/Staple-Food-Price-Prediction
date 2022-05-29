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

it('033. Check add data with Data class and Data type that doesnt match', () => {
    cy.get('[data-cy=month]').click().type('2019-01-15')
    cy.get('[data-cy=location]').select('Addis Ababa')
    cy.get('[data-cy=datatype]').select('Weather Data')
    cy.get('[data-cy=dataitem]').select('Diesel Price')
    cy.get('[data-cy=value]').type('0.15')
    cy.get('[data-cy=record]').click()
    cy.get('[data-cy=dataitem-error]').contains('Data item doesnt fit with the selected data type!')
})

it('034. Check add data with valide inputs but empty Month', () => {
    cy.get('[data-cy=location]').select('Addis Ababa')
    cy.get('[data-cy=datatype]').select('Weather Data')
    cy.get('[data-cy=dataitem]').select('Precipitation')
    cy.get('[data-cy=value]').type('0.15')
    cy.get('[data-cy=record]').click()
    cy.get('input:invalid').should('have.length', 1)
})

it('035. Check add data with valide inputs but empty value', () => {
    cy.get('[data-cy=month]').click().type('2019-01-15')
    cy.get('[data-cy=location]').select('Addis Ababa')
    cy.get('[data-cy=datatype]').select('Weather Data')
    cy.get('[data-cy=dataitem]').select('Precipitation')
    cy.get('[data-cy=record]').click()
    cy.get('input:invalid').should('have.length', 1)
})