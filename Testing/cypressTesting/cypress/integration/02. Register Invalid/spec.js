beforeEach(() => {
    cy.visit('/register')
})

it('003. Check registration with all valid inputs except phone number and as a farmer', () => {
    cy.get('[data-cy=phone-number]').type('091111')
    cy.get('[data-cy=username]').type('user123')
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=confirm-password]').type('12345678')
    cy.get('[data-cy=usertype]').select('Farmer')
    cy.get('[data-cy=register]').click()
    cy.get('[data-cy=phone-number-error]').contains('Please provide a valid phone number!')
})

it('004. Check registration with all valid inputs except phone number and as an economist', () => {
    cy.get('[data-cy=phone-number]').type('091111')
    cy.get('[data-cy=username]').type('user123')
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=confirm-password]').type('12345678')
    cy.get('[data-cy=usertype]').select('Economist')
    cy.get('[data-cy=register]').click()
    cy.get('[data-cy=phone-number-error]').contains('Please provide a valid phone number!')
})

it('005. Check registration with all valid inputs but empty phone number and as a farmer', () => {
    cy.get('[data-cy=username]').type('user123')
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=confirm-password]').type('12345678')
    cy.get('[data-cy=usertype]').select('Farmer')
    cy.get('[data-cy=register]').click()
    cy.get('input:invalid').should('have.length', 1)
})

it('006. Check registration with all valid inputs but empty phone number and as an economist', () => {
    cy.get('[data-cy=username]').type('user123')
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=confirm-password]').type('12345678')
    cy.get('[data-cy=usertype]').select('Economist')
    cy.get('[data-cy=register]').click()
    cy.get('input:invalid').should('have.length', 1)
})

it('007. Check registration with all valid inputs but phone number that already exists', () => {
    cy.get('[data-cy=phone-number]').type('0911111111')
    cy.get('[data-cy=username]').type('user123')
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=confirm-password]').type('12345678')
    cy.get('[data-cy=usertype]').select('Farmer')
    cy.get('[data-cy=register]').click()
    cy.get('[data-cy=phone-number-error]').contains('This phone number is already registered!')
})

it('008. Check registration with all valid inputs except username', () => {
    cy.get('[data-cy=phone-number]').type('0911111133')
    cy.get('[data-cy=username]').type('user123/<>')
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=confirm-password]').type('12345678')
    cy.get('[data-cy=usertype]').select('Farmer')
    cy.get('[data-cy=register]').click()
    cy.get('[data-cy=username-error]').contains('Special characters are not allowed in Username!')
})

it('009. Check registration with all valid inputs but empty username', () => {
    cy.get('[data-cy=phone-number]').type('0911111133')
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=confirm-password]').type('12345678')
    cy.get('[data-cy=usertype]').select('Farmer')
    cy.get('[data-cy=register]').click()
    cy.get('input:invalid').should('have.length', 1)
})

it('010. Check registration with all valid inputs except password', () => {
    cy.get('[data-cy=phone-number]').type('0911111133')
    cy.get('[data-cy=username]').type('user123')
    cy.get('[data-cy=password]').type('1234')
    cy.get('[data-cy=confirm-password]').type('1234')
    cy.get('[data-cy=usertype]').select('Farmer')
    cy.get('[data-cy=register]').click()
    cy.get('[data-cy=password-error]').contains('Password length must be at least 8 characters long!')
})

it('011. Check registration with all valid inputs but empty password', () => {
    cy.get('[data-cy=phone-number]').type('0911111133')
    cy.get('[data-cy=username]').type('user123')
    cy.get('[data-cy=usertype]').select('Farmer')
    cy.get('[data-cy=register]').click()
    cy.get('input:invalid').should('have.length', 2)
})

it('012.Check registration with all valid inputs but wrong confirmation password', () => {
    cy.get('[data-cy=phone-number]').type('0911111133')
    cy.get('[data-cy=username]').type('user123')
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=confirm-password]').type('1234')
    cy.get('[data-cy=usertype]').select('Farmer')
    cy.get('[data-cy=register]').click()
    cy.get('[data-cy=confirm-password-error]').contains('Passwords do not match!')
})

it('013. Check registration with all valid inputs but empty confirmation password', () => {
    cy.get('[data-cy=phone-number]').type('0911111133')
    cy.get('[data-cy=username]').type('user123')
    cy.get('[data-cy=password]').type('12345678')
    cy.get('[data-cy=usertype]').select('Farmer')
    cy.get('[data-cy=register]').click()
    cy.get('input:invalid').should('have.length', 1)
})

