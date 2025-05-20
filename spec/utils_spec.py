from expects import expect, equal
from tipoinstalacion import nearest


with description('Searching the nearest element.'):
    with context('If only one element is passed'):
        with it('must return this element'):
            x = nearest(1, 10)
            expect(x).to(equal(10))
    with context('If more elements are passed.'):
        with context('If it is the lowest between to values'):
            with it('must return the lowest'):
                x = nearest(14, 1, 2, 3, 20, 40)
                expect(x).to(equal(20))
        with context('If the element is just in the middle between to values'):
            with it('must return the lowest'):
                x = nearest(35, 0, 30, 40)
                expect(x).to(equal(30))
        with context('If it is the greatest between to values'):
            with it('must return the greatest'):
                x = nearest(36, 0, 30, 40)
                expect(x).to(equal(40))
