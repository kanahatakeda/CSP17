#Roman Numeral calculator


def value(numeral):

  numeral = string
  
#  Returns base 10 value of roman numeral
#  if found else returns None
 
  values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
  }
  
  return values.get(numeral.upper())
numerals = list(input_numerals)

except TypeError:
    return False
  
  if all(value(i) for i in numerals):
    return numerals
  
  return False
  
  
def calculate(numerals):

  numerals = list of roman numerals (string)
  returns int total value of roman numerals

  total = 0
  
  nums = validate(numerals)
  
  if nums:
    substraction = substract(nums)
  else:
    return "Please enter a valid roman numeral"

  if substraction:
    # take last value in list
    # to substract from
    total = value(nums.pop())
    
    for n in nums:
      total -= value(n)
    return total
  
  for n in nums:
    total += value(n)
  
  return total
  

print(calculate("miiv"))
print(calculate("iiv"))
print(calculate("miiv3"))
print(calculate("i"))
  

