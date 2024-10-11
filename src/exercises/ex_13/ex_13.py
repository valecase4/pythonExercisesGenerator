def palindromes(input_string):
    palindromes = []

    chars = len(input_string)

    for i in range(chars):
        substring = ""

        for j in range(i, chars):
            substring += input_string[j]

            if substring == substring[::-1]: 
                if not substring in palindromes:
                    palindromes.append(substring)

    return palindromes
                

input_string = 'abac'
print(palindromes(input_string))