calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    a = (len(string), string.upper(), string.lower())
    count_calls()
    return a

list_to_search = []
def is_contains(string, list_to_search):
    b = []
    for i in range(len(list_to_search)):
        if string.lower() in list_to_search[i].lower():
            a = True
            b.append(a)
        else:
            a = False
            b.append(a)
    count_calls()
    if True in b:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
