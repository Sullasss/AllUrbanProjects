calls = 0   # 1
def count_calls():  #2
    global calls
    calls += 1

def string_info(string):    #3
    stroka = str(string)
    result = (len(stroka), stroka.upper(), stroka.lower())
    count_calls()
    return result

def is_contains(string, list_to_search):    # 4
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result

# проверяем
print(string_info('Kalinka'))
print(string_info('Cavaleria'))
print(is_contains('cube', ['recycling', 'cyclic', 'sphere'])) # No matches
print(is_contains('GaZEL', ['List', 'Snow', 'Gazelist', 'gAzeL'])) # Urban ~ urBAN

print(calls)

# Другой вариант решения более сокращенный и понятный для меня

calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    length = len(string)
    str_up_registr = string.upper()
    str_low_registr = string.lower()
    return (length, str_up_registr, str_low_registr)

def is_contains(string, list_to_search):
    string_lower = string.lower()
    return string_lower in list_to_search
# проверяем
print(string_info('Kalinka'))
print(string_info('Cavaleria'))
print(is_contains('cube', ['recycling', 'cyclic', 'sphere'])) # No matches
print(is_contains('GaZEL', ['List', 'Snow', 'Gazelist', 'gAzeL'])) # Urban ~ urBAN

print(calls)

