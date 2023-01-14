import re
import sys

''' Read the dictionary file and return the list of words '''
def read_dictionary(file_name):
    words = []
    with open(file_name, 'r') as handle:
        for line in handle:
            words.append(line.strip().lower())
    return words

'''Calculate 'accuracy' of text, where accuracy is defined as the fraction of words present in dictionary '''
def calculate_accuracy(text):
    total = 0
    matched = 0
    dictionary = read_dictionary("american-english")
    for word in text.lower().strip().split():
        if word[-1] == '.': #strip full-stop
            word = word[:-1]
        if word in dictionary:
            matched = matched + 1
        total = total + 1
    return (matched/total)

'''
Decode vigenere cipher-text according to the given key.
'''
def vigen_decode(cipher, length, key):
    index = 0
    decrypted = ""
    for ch in cipher:
        if ch.isalpha():
            decrypted = decrypted + chr((((ord(ch)-97)-key[index % length]) % 26) + 97)
            index = index + 1
        else:
            decrypted = decrypted + ch
    return decrypted

'''
Given a partially found key and key length, generate all possible keys s.t. the
partial_key is part of the generated key.
Use these generated keys to decrypt and see if the resultant plaintext is valid.
'''
def try_key(cipher, key_sub, length, part_key):
    if len(key_sub)+len(part_key) == length:
        key = key_sub + part_key
        for i in range(length):
            key = key[1:] + [key[0]]
            if calculate_accuracy(vigen_decode(cipher, length, key)) > 0.9:
                print("############################## DECRYPTION ##############################")
                print(vigen_decode(cipher, length, key))
                print()
                print("############################## KEY FOUND ##############################")
                print("KEY :",key)
                sys.exit(0)
    else:
        for i in range(26):
            try_key(cipher, key_sub, length, part_key + [i])

'''
We guess that the string password must be present in the plaintext.
The 8 lettered words in ciphertext are: sfuuxytj and uzthsivi
Since 'sfuuxytj' occurs before quoted text, it must be encryption of password.
Using this guess we find, the partial vigenere key. We get partial key of length 8.
Now we try all possible keys of length 8 and above such that the above found partial_key
occurs in the key (not contiguously but when considered in a circular fashion).
'''
if __name__ == '__main__':
    cipher = "Lg ccud qh urg tgay ejbwdkt, wmgtf su bgud nkudnk lrd vjfbg. Yrhfm qvd vng sfuuxytj \"vkj_ecwo_ogp_ej_rnfkukf\" wt iq urtuwjm. Ocz iqa jdag vio uzthsivi pqx vkj pgyd encpggt. Uy hopg yjg fhkz arz hkscv ckoq pgfn vu wwygt nkioe zttft djkth.".lower()
    special_chars_removed = re.sub('[^a-z]','',cipher)
    dictionary = read_dictionary("american-english")
    encrypted_password = "sfuuxytj"
    plain_password = "password"
    key_sub = []
    for i in range(8):
        key_sub.append((ord(encrypted_password[i]) - ord(plain_password[i])) % 26)

    print("Part Key guessed: ", key_sub)
    print()

    for i in range(8,100):
        print("#################### TRYING KEYS OF LENGTH ", i, "####################")
        try_key(cipher, key_sub, i, [])
