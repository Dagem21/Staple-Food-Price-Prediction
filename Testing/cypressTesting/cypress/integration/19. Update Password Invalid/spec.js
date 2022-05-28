beforeEach(() => {
    cy.visit('/login')
    cy.get('[data-cy=phone-number]').type('0912121212')
    cy.get('[data-cy=password]').type('12341234')
    cy.get('[data-cy=login]').click()
    cy.location().should((loc) => {
        expect(loc.pathname).to.eq('/')
    })
    cy.visit('/setting')
})

it('044. Check update password with valid old password but invalid new password', () => {
    cy.get('[data-cy=old-password]').type('12341234')
    cy.get('[data-cy=new-password]').type('1234')
    cy.get('[data-cy=confirm-password]').type('1234')
    cy.get('[data-cy=update]').click()
    cy.get('[data-cy=new-password-error]').contains('Password length must be at least 8 characters long!')
})

it('045. Check update password with valid new password but wrong old password', () => {
    cy.get('[data-cy=old-password]').type('1234567q')
    cy.get('[data-cy=new-password]').type('12345678')
    cy.get('[data-cy=confirm-password]').type('12345678')
    cy.get('[data-cy=update]').click()
    cy.get('[data-cy=password-error]').contains('The password provided is incorrect!')
})

it('046. Check update password with valid new password same as old password', () => {
    cy.get('[data-cy=old-password]').type('12341234')
    cy.get('[data-cy=new-password]').type('12341234')
    cy.get('[data-cy=confirm-password]').type('12341234')
    cy.get('[data-cy=update]').click()
    cy.get('[data-cy=new-password-error]').contains('Your new password should be different from the old one!')
})

it('047. Check update password with valid new password but empty old password', () => {
    cy.get('[data-cy=new-password]').type('12341234')
    cy.get('[data-cy=confirm-password]').type('12341234')
    cy.get('[data-cy=update]').click()
    cy.get('input:invalid').should('have.length', 1)
})

it('048. Check update password with valid new password but empty old password', () => {
    cy.get('[data-cy=old-password]').type('12341234')
    cy.get('[data-cy=update]').click()
    cy.get('[data-cy=new-password-error]').contains('Please enter a new password!')
})