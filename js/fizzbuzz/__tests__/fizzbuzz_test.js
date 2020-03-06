// import the code to be tested
const { fizz, buzz, fibu, play } = require('../fizzbuzz') // the "old" safe way to import stuff

describe('A FizzBuzz program', () => {
  it('has a smoke test', () => {
    expect(true).toBe(true)
    expect(true).not.toBe(false)
  })

  describe('A fizz() function', () => {
    it('throws an error if there is no input', () => {
      expect(() => { fizz() }).toThrow('there is no input')
      expect(() => { fizz(3) }).not.toThrow()
    })

    it('returns "Fizz" if x is numeric and a multiple of 3', () => {
      expect(fizz(3)).toBe('Fizz')
      expect(fizz(4)).toBe(4)
      expect(fizz(0)).toBe('Fizz')
      expect(fizz(15)).toBe('Fizz')
      expect(fizz(-3)).toBe('Fizz')
      expect(fizz(-2)).toBe(-2)
      expect(fizz(3.5)).toBe(3.5)
      expect(fizz('Buzz')).toBe('Buzz')
    })
  })

  describe('A buzz() function', () => {
    it('throws an error if there is no input', () => {
      expect(() => { buzz() }).toThrow('there is no input')
      expect(() => { buzz(5) }).not.toThrow()
    })

    it('returns "Buzz" if x is numeric and a multiple of 5', () => {
      expect(buzz(5)).toBe('Buzz')
      expect(buzz(4)).toBe(4)
      expect(buzz(0)).toBe('Buzz')
      expect(buzz(15)).toBe('Buzz')
      expect(buzz(-5)).toBe('Buzz')
      expect(buzz(-2)).toBe(-2)
      expect(buzz(5.5)).toBe(5.5)
      expect(buzz('Fizz')).toBe('Fizz')
    })
  })

  describe('A fibu() function', () => {
    it('throws an error if there is no input', () => {
      expect(() => { fibu() }).toThrow('there is no input')
      expect(() => { fibu(15) }).not.toThrow()
    })

    it('returns "FizzBuzz" if x is numeric and a multiple of 15', () => {
      expect(fibu(15)).toBe('FizzBuzz')
      expect(fibu(4)).toBe(4)
      expect(fibu(0)).toBe('FizzBuzz')
      expect(fibu(-15)).toBe('FizzBuzz')
      expect(fibu(-2)).toBe(-2)
      expect(fibu(15.5)).toBe(15.5)
      expect(fibu('Fizz')).toBe('Fizz')
    })
  })

  it('can play FizzBuzz', () => {
    expect(play(1, 15)).toStrictEqual([
      1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz'
    ])
  })
})