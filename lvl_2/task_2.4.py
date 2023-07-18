# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s : str):
    return s.replace('!','')

#print(remove_exclamation_marks("Hi! Hello!"))
#print(remove_exclamation_marks(""))
#print(remove_exclamation_marks("Oh, no!!!"))

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s : str):
    if s[-1]=='!':
        return s[0:-1]
    else:
        return s

#print(remove_last_em("Hi!"))
#print(remove_last_em("Hi!!!"))
#print(remove_last_em("!Hi"))
# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    result = ""
    lst = s.split(' ')
    for i in lst:
        if i.count('!') != 1:
            result += i+" "

    return result[0:-1]     


#print(remove_word_with_one_em("Hi!")) 
#print(remove_word_with_one_em("Hi! Hi!"))# === ""
#print(remove_word_with_one_em("Hi! Hi! Hi!"))# === ""
#print(remove_word_with_one_em("Hi Hi! Hi!"))# === "Hi"
#print(remove_word_with_one_em("Hi! !Hi Hi!"))# === ""
#print(remove_word_with_one_em("Hi! Hi!! Hi!"))# === "Hi!!"
#print(remove_word_with_one_em("Hi! !Hi! Hi!"))# === "!Hi!"   


