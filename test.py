# hex1 = "1c0111001f010100061a024b53535009181c"
# hex2 = "686974207468652062756c6c277320657965"
plaintext = "Hello World"
key = "A"
plaintext1 = bytes(plaintext,encoding='UTF-8')
key = bytes(key,encoding='UTF-8')
print(plaintext, key)
print(key * len(plaintext1))
print(key * len(plaintext))

