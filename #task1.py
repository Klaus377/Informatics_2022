#task1
if number % 2 == 0: 
        return "Even" 
    else: 
        return "Odd" 
even_or_odd(10) 
 
 
#task2 
def count_sheeps(sheep): 
    return sheep.count(True) 
 
 
#task3 
def monkey_count(n): 
    result = [] 
    for num in range(1, n + 1): 
        result.append(num) 
    return result 
monkey_count(10) 
 
 
#task4 
def paperwork(n, m): 
    return n * m if n > 0 and m > 0 else 0  
paperwork(10,16) 
 
 
#task5 
def hero(b, d): 
  bulletsneeded = d * 2 
  if b >= bulletsneeded: 
    return True 
  else: 
    return False 
hero(30,10)
#task1 
def polish_letters(s): 
    polish = {"ą": "a", "ć": "c", "ę": "e", "ł": "l", "ń": "n", "ó": "o", "ś": "s", "ź": "z", "ż": "z"} 
    return "".join([polish[c] if c in polish else c for c in s]) 
 
#task2 
def sum_of_minimums(numbers): 
    result = 0 
    for i in numbers: 
        result += min(i) 
    return result 
 
 
 
#task3 
list = [] 
 
 
def find_all(list, x): 
    l = len(list) 
    result = [] 
    for i in range(0,l): 
        if x == list[i]: 
            result.append(i) 
    return result 
 
 