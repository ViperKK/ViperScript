import random
import math

def viper_print(prstring):
    print(prstring)
pass

def viper_ask(qsstring):
        return input(qsstring)
        pass
pass

def viper_test(bool__, y, n):
  return y if bool__ else n
pass

def viper_checkval(x, y, type__):
  if type__ == '===':
    return x == y
  if type__ == '!=!':
    return x != y
  if type__ == '<<<':
    return x < y
  if type__ == '>>>':
    return x > y
  if type__ == '<=<':
    return x <= y
  if type__ == '>=>':
    return x >= y
pass

def viper_math(x, y, z, type__):
  if type__ == 'add':
    return x + y
  if type__ == 'sub':
    return x - y
  if type__ == 'mtp':
    return x * y
  if type__ == 'div':
    return x / y
  if type__ == 'pwr':
    return x ** y
  if type__ == 'sqt':
    return math.sqrt(x)
  if type__ == 'abs':
    return math.fabs(x)
  if type__ == 'neg':
    return -x
  if type__ == 'nlg':
    return math.log(x)
  if type__ == 'l10':
    return math.log10(x)
  if type__ == 'epw':
    return math.exp(x)
  if type__ == 'tpw':
    return math.pow(10,x)
  if type__ == 'sin':
    return math.sin(x / 180.0 * math.pi)
  if type__ == 'cos':
    return math.cos(x / 180.0 * math.pi)
  if type__ == 'tan':
    return math.tan(x / 180.0 * math.pi)
  if type__ == 'asn':
    return math.asin(x) / math.pi * 180
  if type__ == 'acs':
    return math.acos(x) / math.pi * 180
  if type__ == 'atn':
    return math.atan(x) / math.pi * 180
  if type__ == 'rnd':
    return round(x)
  if type__ == 'rdu':
    return math.ceil(x)
  if type__ == 'rdd':
    return math.floor(x)
  if type__ == 'rmd':
    return x % y
  if type__ == 'cst':
    return min(max(x, y), z)
  if type__ == 'rng':
    return random.randint(x, y)
pass