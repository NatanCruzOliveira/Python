n = input('Digite algo: ')

print('O que foi digitado é tipo número? ', n.isnumeric())
print('O que foi digitado é tipo letras? ', n.isalpha())
print('O que foi digitado tem só espaços? ', n.isspace())
print('O que foi digitado é alfanúmerico? ', n.isalnum())
print('O que foi digitado está em maiúscula? ', n.isupper())
print('O que foi digitado está em minúscula? ', n.islower())
print('O que foi digitado está capitalizado? ', n.istitle())
