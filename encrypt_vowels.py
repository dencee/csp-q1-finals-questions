vowels = ["a", "e", "i", "o", "u"]
codes = ["5", "4", "3", "2", "1"]

def encrypt_vowel_substitution(plaintext):
  encrypted_message = ""

  for letter in plaintext:
    found = False
    for i in range(len(vowels)):
      if letter == vowels[i]:
        encrypted_message += codes[i]
        found = True

    if not found:
      encrypted_message += letter
  return encrypted_message


def decrypt_vowel_substitution(ciphertext):
  encrypted_message = ""

  for letter in ciphertext:
    found = False
    for i in range(len(codes)):
      if letter == codes[i]:
        encrypted_message += vowels[i]
        found = True

    if not found:
      encrypted_message += letter
  return encrypted_message

secret = encrypt_vowel_substitution("Hello")
print(secret)
print(decrypt_vowel_substitution(secret))