# #1 Vowel Substitution Cipher

In class we used a program called letter_swapper.py to decode a message. Now, lets code one ourselves!

## How It Works

- Each vowel is translated in a specific digit
- Case doesn't matter (lowercase and uppercase letters use digit).
- Spaces, numbers, and punctuation (`!`, `?`, `,`) stay the same.

### Substitution Rules

| Vowel | Replacement |
|---|---:|
| `a` | `5` |
| `e` | `4` |
| `i` | `3` |
| `o` | `2` |
| `u` | `1` |

## Starter Code

```python
vowels = ["a", "e", "i", "o", "u"]
codes = ["5", "4", "3", "2", "1"]
```

## Functions to Write

### 1. `encrypt_vowel_substitution(plaintext)`
Takes a string of regular text and returns a string where vowels are replaced by the corresponding digit.

### 2. `decrypt_vowel_substitution(ciphertext)`
Takes a vowel substituted string and returns another string where the digits are replaced by letters.

### Useful Functions
The `.lower()` string method can be used to create a new string with all letters converted to lower case
```python
# Calling .tolower returns a new string "abcdefghijklmnopqrstuvwxyz"
"AbCDeFgHiJkLmNoPqRsTuVwXyZ".lower()
```

## Requirements
Your program must:

1. Replace every vowel during encryption.
2. Convert the numbers back to vowels during decryption.
3. Leave consonants, spaces, and punctuation unchanged.
4. Display the original, encrypted, and decrypted messages.
5. It is not required to preserve capitalization.
6. It is not required to handle digits in the original message.

## Example

```python
# Encrypting
secret = encrypt_vowel_substitution("Meowdy Purrtners!")
print(secret)  # Output: M42wdy P1rrtn4rs!

# Decrypting
original = decrypt_substitution(secret)
print(original)  # Output: M42wdy P1rrtn4rs!
```

# #2 A pHishy 🎣 Log Detector

In our last project, you relied on visual inspection to spot the phishing email.
Let's see if we can create a program to spot more of those security vulnerabilities in the future!

## How It Works

- Read in a log file and check for sus parts of an email, specifically protocols that begin with `http://` and not `https://` **AND** if the domain is not in the trusted domains list
- Specifically we're looking for malicious links indicated by an untrusted domain. For simplicity, we are going to refer to `<name>.com` as the domain in our program. For example, the domain for `https://google.com` is `google.com`
- In our program, we will assume the domain of a link always follows `http://` or `https://`.
- We can verify if there are any pHishy links in our email log by reading each line of the log and verifying if any of the links route to a domain not in our trusted list!

## Starter Code

```python
TRUSTED_DOMAINS = [
    "great_company.com",
    "great_company_mail_srvr.com",
    "great_company_partner.com",
    "mailserver.com",
    "travelerhelper.com",
    "fishtankmonitors.com",
    "payroll.com",
    "great_food.com",
    "restaurant_reservations.com",
    "bestofficesupplies.com",
    "campingsupplies.com",
    "campingreservations.com"
]

def scan_log(file_name):
  log_file = open(file_name, "r")
  for line in log_file:
    print(line)

scan_log("email_record.log")
```
## Functions to Write

### 1. `scan_log(file_name)`
Takes a file name, opens the file, then reads through every line looking for links that start with `http://` followed by a domain not in the TRUSTED_DOMAINS list. The function prints the line number followed by the sus domain link. The function returns a list of all the sus domains with line numbers or an empty list if none occurences are found.

> If you want to try raising an exception instead of just printing the domain and line number I would be ok with that too! 💪

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

1. Within `email_record.log`, find all occurrences of links starting with `http://` AND domains NOT in TRUSTED_DOMAINS.
2. If an untrusted domain is found, print the line number followed by the sus domain.
3. Return a list of all the sus domains with line numbers or an empty list if no occurences were found.

## Example

```python
phishy_links = scan_log("email_record.log")
print(phishy_links)  # ["42. meowdy.net", "24. purrtners.org"]
