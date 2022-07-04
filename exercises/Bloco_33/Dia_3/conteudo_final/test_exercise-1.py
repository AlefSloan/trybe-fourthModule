from exercise_1 import fizz_buzz

response_lists = [
  [1, 2, 'Fizz', 4, 'Buzz'],
  [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz'],
  [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8,
      'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz'],
  [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz',
      11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz']
]


def test_fizz_buzz_function():
    assert fizz_buzz(5) == response_lists[0]
    assert fizz_buzz(10) == response_lists[1]
    assert fizz_buzz(15) == response_lists[2]
    assert fizz_buzz(20) == response_lists[3]
