beforeEach(() => {
    cy.visit('/login')
    cy.get('[data-cy=phone-number]').type('0911111111')
    cy.get('[data-cy=password]').type('12341234')
    cy.get('[data-cy=login]').click()
    cy.location().should((loc) => {
        expect(loc.pathname).to.eq('/')
    })
    cy.visit('/users')
})

it('029. Check authorized admin can remove other users', () => {
    let lengthBefore;
    cy.get('[data-cy=usersTable]').find("tr").its('length').then((len) => {
        lengthBefore = len;
        cy.log('Initial table Length is: ' + lengthBefore);
      });
    cy.get('[data-cy=delete-4]').click()
    cy.get('[data-cy=usersTable]').find("tr").its('length').then((lenAfter) => {
        cy.log('After table Length is: ' + lenAfter);
        expect(lengthBefore).to.equal(lenAfter + 1);
      });
})