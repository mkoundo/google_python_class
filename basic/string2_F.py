# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  a_front = evenodd(a)
  a_back = a.replace(a_front,'')
  b_front = evenodd(b)
  b_back = b.replace(b_front,'')
  return a_front + b_front + a_back + b_back

def evenodd(a):
  if float(len(a))/2 > float(len(a))//2:
    a_front = a[0:len(a)/2 + 1]  #odd
  else:
    a_front = a[0:len(a)/2]  #even
  return a_front


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print
  print 'front_back'
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
