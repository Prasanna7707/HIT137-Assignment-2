def decrypt_caesar_cipher(ciphertext, shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decrypted = ''
    
    # Loop over the characters in the ciphertext
    for char in ciphertext:
        if char in alphabet:
            # Find the index of the character in the alphabet
            index = alphabet.find(char)
            # Shift the index and wrap around the alphabet if needed
            shifted_index = (index - shift) % len(alphabet)
            # Append the decrypted character to the decrypted message
            decrypted += alphabet[shifted_index]
        else:
            # If the character is not in the alphabet (e.g., a space or punctuation), leave it as is
            decrypted += char     
    return decrypted

encrypted_message = '''
    VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY 
    NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF
    URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR 
    '''

decryption_attempts = [(shift, decrypt_caesar_cipher(encrypted_message, shift)) for shift in range(1, 26)]

for attempt in decryption_attempts:
    print(f"{attempt[0]}. {attempt[1]}\n")
