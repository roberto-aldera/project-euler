# frozen_string_literal: true

# Problem 001
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

if __FILE__ == $PROGRAM_NAME
  sum = 0
  (1..999).each do |i|
    sum += i if (i % 3).zero? || (i % 5).zero?
  end
  puts sum
end
