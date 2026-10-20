# #1 Morse Code Substitution Cipher

In class we used a program called letter_swapper.py to decode a message. Now, lets code one ourselves!

## How It Works

- Each letter A to E can be encoded or decoded to Morse Code
- Case doesn't matter (lowercase and uppercase letters encode to the same symbols).
- Spaces, numbers, and punctuation (`!`, `?`, `,`) stay the same.

### Substitution Rules

| Vowel | Replacement |
|---|---:|
| `A` | `.-` |
| `B` | `-...` |
| `C` | `-.-.` |
| `D` | `-..` |
| `E` | `.` |

## Starter Code

```python
letters = ["A", "B", "C", "D", "E"]
morse_codes = [".-", "-...", "-.-.", "-..", "."]
```

## Functions to Write

### 1. `encrypt_morse_substitution(plaintext)`
Takes a string of readable text and returns a string where letters are replaced by the corresponding morse code symbols.

### 2. `decrypt_morse_substitution(ciphertext)`
Takes a morese code substituted string and returns another string where the morse code symbols are replaced by letters.

### Useful Functions
The `.lower()` string method can be used to create a new string with all letters converted to lower case
```python
# Calling .tolower returns a new string "abcdefghijklmnopqrstuvwxyz"
"AbCDeFgHiJkLmNoPqRsTuVwXyZ".lower()
```

## Requirements
Your program must:

1. Replace every letter in the `letters` list during encryption.
2. Convert the morse code symbols back to letters during decryption.
3. Leave consonants, spaces, and punctuation unchanged.
4. Display the original, encrypted, and decrypted messages.
5. It is not required to preserve capitalization.
6. It is not required to handle digits in the original message.

## Example

```python
# Encrypting
secret = encrypt_morse_substitution("Meowdy Purrtners!")
print(secret)  # Output: M.ow-..y Purrtn.rs!

# Decrypting
original = decrypt_morse_substitution(secret)
print(original)  # Output: Meowdy Purrtners!
```

# #2 A pHishy *Admin* 🎣 Log Detector

You suspect an admin was involved in the pHishy Log detector scam! See if you can help the forensics team find which admins sent emails from in the email log.

## How It Works

- Read in a log file and check for emails from an admin. Specifically, search for the name `admin` at the first part of an email address. Messages from somone are always preceeded by "From: " and admins names are always followed by an **`@`** symbol
- Example: `From: admin@travelerhelper.com` is an email from an admin because it has `From: ` at the beginning and `@` after the name `admin`
- In our program, we want a *list of all the domains* from messages sent by admins. So in the example above, the domain would be `travelerhelper.com`
-For simplicity, we are going to refer to `<name>.com` as the domain in our program. For example, the domain for `https://google.com` is `google.com`

## Starter Code

```python
# phishy_admin_log_detector.py
def scan_log(file_name):
  log_file = open(file_name, "r")
  for line in log_file:
    print(line)

scan_log("email_record.log")
```
## Functions to Write

### 1. `scan_log(file_name)`
Takes a file name, opens the file, then reads through every line looking for domains that start with `From: ` followed by the name `admin` and then an `@`. Upon finding an admin's email domain, the function prints the line number followed followed by the sus admin domain. The function returns a list of all the sus admin domains with line numbers or an empty list if none occurences are found.

### Useful Functions
The `.find()` string method returns the *lowest index* where the specified substring is found within the string or -1 if not found at all
```python
# Prints 7 because "purr" is at index 7 starting from the left of the string
print("meowdy purrtners".find("purr"))

# Prints -1 because "partners" is not found in the string
print("meowdy purrtners".find("partners"))
```

## Requirements
Your program must:

1. Within `email_record.log`, find all occurrences of domains from email messages sent by admins.
2. If an admin's domain is found, print the line number followed by their domain.
3. Return a list of all the sus admin domains with line numbers or an empty list if no occurences were found.

## Example

```python
phishy_links = scan_log("email_record.log")
print(phishy_links)  # ["42. meowdy.net", "24. purrtners.org"]
