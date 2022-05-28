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

it('022. Check add admin with valide inputs except phone number as an authorized admin', () => {
    cy.get('[data-cy=phone-number]').type('091111')
    cy.get('[data-cy=username]').type('admin123')
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=confirm-password]').type('12345678')
    cy.get('[data-cy=add-admin]').click()
    cy.get('[data-cy=phone-number-error]').contains('Please provide a valid phone number!')
})

it('023. Check add admin with valide inputs but empty phone number as an authorized admin', () => {
    cy.get('[data-cy=username]').type('admin123')
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=confirm-password]').type('12345678')
    cy.get('[data-cy=add-admin]').click()
    cy.get('input:invalid').should('have.length', 1)
})

it('024. Check add admin with valide inputs but existing phone number as an authorized admin', () => {
    cy.get('[data-cy=phone-number]').type('0911111113')
    cy.get('[data-cy=username]').type('admin123')
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=confirm-password]').type('12345678')
    cy.get('[data-cy=add-admin]').click()
    cy.get('[data-cy=phone-number-error]').contains('This phone number is already registered!')
})

it('025. Check add admin with valide inputs but empty user name as an authorized admin', () => {
    cy.get('[data-cy=phone-number]').type('0911111119')
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=confirm-password]').type('12345678')
    cy.get('[data-cy=add-admin]').click()
    cy.get('input:invalid').should('have.length', 1)
})

it('026. Check add admin with valide inputs except password as an authorized admin', () => {
    cy.get('[data-cy=phone-number]').type('0911111119')
    cy.get('[data-cy=username]').type('admin123')
    cy.get('[data-cy=password]').type('1234')
    cy.get('[data-cy=confirm-password]').type('1234')
    cy.get('[data-cy=add-admin]').click()
    cy.get('[data-cy=password-error]').contains('Password length must be at least 8 characters long!')
})

it('027. Check add admin with valide inputs but empty password as an authorized admin', () => {
    cy.get('[data-cy=phone-number]').type('0911111119')
    cy.get('[data-cy=username]').type('admin123')
    cy.get('[data-cy=add-admin]').click()
    cy.get('input:invalid').should('have.length', 2)
})