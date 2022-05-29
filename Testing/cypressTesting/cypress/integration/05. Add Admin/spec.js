beforeEach(() => {
    cy.visit('/login')
    cy.get('[data-cy=phone-number]').type('0911111111')
    cy.get('[data-cy=password]').type('12341234')
    cy.get('[data-cy=login]').click()
    cy.location().should((loc) => {
        expect(loc.pathname).to.eq('/')
    })
    cy.visit('/addAdmin')
})

it('020. Check add admin with valide inputs with full privileges as an authorized admin', () => {
    cy.get('[data-cy=phone-number]').type('0911111113')
    cy.get('[data-cy=username]').type('admin123')
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=confirm-password]').type('12345678')
    cy.get('[data-cy=admin-privilege]').check()
    cy.get('[data-cy=add-admin]').click()
    cy.get('[data-cy=messages]').contains('Admin registered successfully!')
})

it('021. Check add admin with valide inputs with limited privileges as an authorized admin', () => {
    cy.get('[data-cy=phone-number]').type('0911111114')
    cy.get('[data-cy=username]').type('admin123')
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=confirm-password]').type('12345678')
    cy.get('[data-cy=add-admin]').click()
    cy.get('[data-cy=messages]').contains('Admin registered successfully!')
})