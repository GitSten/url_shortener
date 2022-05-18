import  random
from string import  ascii_lowercase,ascii_uppercase

numbers =[str(i) for i in range(10)]

pool = numbers + list(ascii_uppercase) + list(ascii_lowercase)



def generate_aliases():
    return  "".join(random.sample(pool,8))


print(generate_aliases())

