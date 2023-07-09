'''
    AUTHOR          : OrderOfThePhoenix
    ACKNOWLEDGEMENT : quadgram frequency file taken from http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/english-letter-frequencies/#quadgram-frequencies
'''
import sys
import random
import math
import re
import time

''' shift alphabet by the amount 'shift' '''
def shift_word(alphabet, shift):
    if alphabet.islower():
        return chr(97 + ((ord(alphabet)-97 +shift) % 26))
    elif alphabet.isupper():
        return chr(65 + ((ord(alphabet)-65 +shift) % 26))
    else:
        return alphabet

''' caesar cipher decryption with 'shift' as the key '''
def caesar(text, shift):
    decrypted_text = ""
    for ch in text:
        decrypted_text = decrypted_text + shift_word(ch, shift)
    return decrypted_text

''' Read the dictionary file and return the list of words '''
def read_dictionary(file_name):
    words = []
    with open(file_name, 'r') as handle:
        for line in handle:
            words.append(line.strip().lower())
    return words

'''Calculate 'accuracy' of text, where accuracy is defined as the fraction of words present in dictionary '''
def calculate_accuracy(text, dictionary):
    total = 0
    matched = 0
    for word in text.lower().strip().split():
        if word[-1] == '.': #strip full-stop
            word = word[:-1]
        if word in dictionary:
            matched = matched + 1
        total = total + 1
    return (matched/total)

''' return frequency of each alphabet in message. '''
def frequency_list(message):
    total = 0
    frequency = dict()
    for ch in message:
        total = total + 1
        if ch.isalpha():
            if ch in frequency:
                frequency[ch] = frequency[ch] + 1
            else:
                frequency[ch] = 1
    for key in frequency:
        frequency[key] = frequency[key]/total
    return frequency

''' return a list of all the single-letter words in the message '''
def single_letters(message):
    letters = []
    for word in message.strip().split():
        if len(word.strip()) == 1 and word not in letters and word.isalpha():
            letters.append(word)
    return letters

''' return a list of all the two-letterd words in the message '''
def double_letters(message):
    letters = []
    for word in message.strip().split():
        if len(word.strip()) == 2 and word not in letters:
            letters.append(word)
    return letters

''' return a list of all the three-lettered words in the message '''
def three_letters(message):
    letters = dict()
    total = 0
    for word in message.strip().split():
        if len(word.strip()) == 3:
            total = total + 1
            if word not in letters:
                letters[word] = 1
            else:
                letters[word] = letters[word] + 1
    for key in letters:
        letters[key] = letters[key]/total
    return letters

''' Takes a dictionary of key -> frequency and return top n most frequent keys '''
def n_most_frequent(mapping, n):
    answer = list()
    for i in range(n):
        maximum = 0
        result = ""
        for key in mapping:
            if key not in answer and mapping[key] > maximum:
                maximum = mapping[key]
                result = key
        answer.append(result)
    return answer

'''
Takes the encrypted text and the mapping (a list whose 1st element specifies what 'a' in ciphertext is mapped to
and so on. Ex: mapping = [3,1,5,....] means 'a' in cipher is 'c' in plain, 'b' in cipher is 'a' in plain, 'c' in
cipher is 'e' in plain and so on). Returns the decrypted message according to mapping.
'''
def decrypt_substitution(encrypted_message, mapping):
    message = ""
    for ch in encrypted_message:
        if ch.isalpha():
            message = message + chr(97+mapping[ord(ch)-97])
        else:
            message = message + ch
    return message

'''
Read the file of quadgrams and save score of each quadgram.
score = log(probability of quadgram) , where
probability of quadgram = frequency of quadgram/sum of frequency of all quadgrams
log is taken to prevent numerical underflow later when calculating quadgram score.
'''
def read_quadgram(file):
    result = dict()
    total = 0
    with open(file, 'r') as handle:
        for line in handle:
            word, times = line.split()[0], int(line.split()[1])
            result[word.strip().lower()] = times + 1
            total = total + times + 1
    for key in result:
        result[key] = math.log(result[key]/total)
    return result

'''
Calculate quadgram score. To Calculate quadgram score:
1) Remove all non-alphabets from text. Ex: Dumbeldore's Army ==> DumbeldoresArmy
2) Then consider all quadgrams like ['Dumb', 'umbe', 'mbel', 'beld' ...] and sum
   the score of each quadgram as given by the dictionary parameter 'quadgram'
'''
def quadgram_score(text, quadgram):
    message = re.sub('[^a-z]','',text.lower())
    score = 0
    for i in range(len(message)-3):
        if message[i:i+4] in quadgram:
            score = score + quadgram[message[i:i+4]]
    return score

'''
Start with the given mapping. At each iteration random switch two elements in the map
and calculate the new quadgram score. Keep the new map if its quadgram score is higher
otherwise revert back to previous map. Keep doing this iteratively until the decrypted
text is readable where readability is determined by checking the fraction of words in
decrypted text present in dictionary. If 'readability' is above a threshold, currently
set to 0.9, stop and output the decrypted text.
If the algorithm is stuck, it restarts.
'''
def improve_mapping(encrypted_message, mapping, dictionary):
    quadgram = read_quadgram('quadgrams.txt')
    prev_score = quadgram_score(decrypt_substitution(encrypted_message, mapping), quadgram)
    iter = 0
    start_time = time.time()
    while calculate_accuracy(decrypt_substitution(encrypted_message, mapping), dictionary) < 0.9:
        i = 0
        if (time.time() - start_time) >= 15: #Restart every 10s
            print("Stuck after",iter,"iterations, Restarting!")
            return
        while i < 100:
            iter = iter + 1
            i = i + 1
            index1, index2 = random.randint(0,25), random.randint(0,25)
            mapping[index1], mapping[index2] = mapping[index2], mapping[index1]
            new_score = quadgram_score(decrypt_substitution(encrypted_message, mapping), quadgram)
            if new_score < prev_score:
                mapping[index1], mapping[index2] = mapping[index2], mapping[index1] #revert back
            else:
                prev_score = new_score #update max_score

    key = ""
    for i in range(26):
        key = key + chr(97+mapping[i])
    print()
    print("############################## DECRYPTION ##############################")
    print(decrypt_substitution(encrypted_message, mapping))
    print()
    print("# of iterations: ",iter)
    print("############################## KEY FOUND ##############################")
    print("CIPHERTEXT: abcdefghijklmnopqrstuvwxyz")
    print("PLAINTEXT :",key)
    sys.exit(0)


'''
Determine initial substitution key using frequency analysis:
1) Most frequent alphabet is set to 'e'
2) Most frequent three lettered word is set to 'the'
3) Single lettered words are set to 'i' and 'a', where higher frequency word is
   set to 'a'
4) Remaining words are mapped randomly
This initial map is passed to improve_mapping function above for incremental
improvement.
'''
def substitution(encrypted_message, dictionary):
    mapping = [0]*26
    mapped_indices = []
    unmapped_chars = [i for i in range(26)]

    frequency = frequency_list(encrypted_message)
    mapping[ord(n_most_frequent(frequency, 1)[0])-97] = ord('e')-97
    mapped_indices.append(ord(n_most_frequent(frequency, 1)[0])-97)
    unmapped_chars.remove(ord('e')-97)

    triples = three_letters(encrypted_message)
    most_frequent = n_most_frequent(triples, 1)[0]
    mapping[ord(most_frequent[0])-97] = ord('t')-97
    mapping[ord(most_frequent[1])-97] = ord('h')-97
    mapped_indices.append(ord(most_frequent[0])-97)
    mapped_indices.append(ord(most_frequent[1])-97)
    unmapped_chars.remove(ord('t')-97)
    unmapped_chars.remove(ord('h')-97)

    singles = single_letters(encrypted_message)
    if len(singles) == 1:
        mapping[ord(singles[0])-97] = ord('a')-97
        mapped_indices.append(ord(singles[0])-97)
        unmapped_chars.remove(ord('a')-97)
    elif len(singles) == 2:
        if frequency[singles[0]] > frequency[singles[1]]:
            mapping[ord(singles[0])-97] = ord('a')-97
            mapping[ord(singles[1])-97] = ord('i')-97
            mapped_indices.append(ord(singles[0])-97)
            mapped_indices.append(ord(singles[1])-97)
            unmapped_chars.remove(ord('a')-97)
            unmapped_chars.remove(ord('i')-97)
        else:
            mapping[ord(singles[0])-97] = ord('i')-97
            mapping[ord(singles[1])-97] = ord('a')-97
            mapped_indices.append(ord(singles[0])-97)
            mapped_indices.append(ord(singles[1])-97)
            unmapped_chars.remove(ord('a')-97)
            unmapped_chars.remove(ord('i')-97)

    for i in range(12):
        random.shuffle(unmapped_chars)
        used = 0
        flag = 1
        for i in range(26):
            if i not in mapped_indices:
                try:
                    mapping[i] = unmapped_chars[used]
                    used = used + 1
                except IndexError as error:
                    flag = 0
                    print("##### DEBUG: i =",i,"used =",used,"Mapping =",len(mapping),"Unmapped =",len(unmapped_chars),"Mapped =",len(mapped_indices),"#####")
                    break
        if flag == 1:
            improve_mapping(encrypted_message, mapping, dictionary)
    print("############### INCORRECT PERMUTATION ###############")

'''
Entry Point.
1) First check if the cipher is caesar cipher.
2) If not then call substitution function above to break the cipher, assumed to be substitution cipher.
'''
if __name__ == '__main__':
    encrypted_message = input()
    dictionary = read_dictionary('american-english')
    for shift in range(1,26):
        decryption = caesar(encrypted_message, shift)
        if calculate_accuracy(decryption, dictionary) > 0.9:
            print("##############################  POSSIBLE CANDIDATE ##############################")
            print('Possible Decryption Key (Caesar): ',shift)
            print('Decrypted Text: ')
            print(decryption)
            sys.exit(1)

    substitution(encrypted_message.lower(), dictionary)
