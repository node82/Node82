import re
# Take any string data
string = """can we find the valid credit card in this string,
mistakenly entered into the user input. 4444 3232 1010 8989
and perhaps another? 9191 0232 9999 1111"""

# Define the searching pattern
pattern = '(([0-9](\s+)?){4}){4}'

# match the pattern with input value
found = re.search(pattern, string)
print(found)
# Print message based on the return value
if found:
  print("Found a credit card number!")
else:
  print("No credit card numbers present in input")
