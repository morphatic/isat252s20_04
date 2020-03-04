// import the code to be tested
const { fizz } = require('../fizzbuzz') // the "old" safe way to import stuff

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
  })
})