# 8. Decode the message:
# A message containing the letters from A-Z can be encoded into the numbers using the mapping
# A-> 1, B-> 2, C-> 3, ..., Z-> 26. To decode an encoded message, you need to group the digits
# and do the reverse mapping. You are required to display all the possible decoded messages.
# For example: "11106" can be decoded into:
# a. "AAJF" with the grouping (1 1 10 6)
# b. "KJF" with the grouping (11 10 6)
def decode_message(encoded_message):
    if not encoded_message:
        return ['']
    
    results = []
    
    # Check the first single digit
    if '1' <= encoded_message[:1] <= '9':
        char = chr(ord('A') + int(encoded_message[:1]) - 1)
        for sub_message in decode_message(encoded_message[1:]):
            results.append(char + sub_message)
    
    # Check the first two digits
    if len(encoded_message) >= 2 and '10' <= encoded_message[:2] <= '26':
        char = chr(ord('A') + int(encoded_message[:2]) - 1)
        for sub_message in decode_message(encoded_message[2:]):
            results.append(char + sub_message)
    
    return results


encoded_message =  input("Enter the encoded number:")
decoded_messages = decode_message(encoded_message)

if decoded_messages:
    print("\nHere are all the possible decoded messages:")
    for message in decoded_messages:
        print(message)
else:
    print("Oops! No valid way to decode this message.")
