from itertools import permutations
import re
from sub_decrypt import read_dictionary, substitution
import threading
import multiprocessing

'''
Permute the given cipher string according to the given key.
'''
def rearrange(cipher, perm_key):
    special_removed = re.sub('[^a-z]','',cipher)
    permuted = ""
    for i in range(0,len(special_removed),5):
        sub_text = special_removed[i:i+5]
        for i in range(5):
            permuted = permuted + sub_text[perm_key[i]]
    final_str = ""
    track=0
    for ch in cipher:
        if ch.isalpha():
            final_str = final_str + permuted[track]
            track = track + 1
        else:
            final_str = final_str + ch
    return final_str

'''
Try all the permutations in the input list.
For each permutation. try to decrypt it assuming it to be substitution cipher.
'''
def solve(perms):
    dictionary = read_dictionary('american-english')
    cipher = "Lg ccud qh urg tgay ejbwdkt, wmgtf su bgud nkudnk lrd vjfbg. Yrhfm qvd vng sfuuxytj \"vkj_ecwo_ogp_ej_rnfkukf\" wt iq urtuwjm. Ocz iqa jdag vio uzthsivi pqx vkj pgyd encpggt. Uy hopg yjg fhkz arz hkscv ckoq pgfn vu wwygt nkioe zttft djkth.".lower()
    for perm in perms:
        print("############### TRYING WITH PERMUTATION:", perm," ###############")
        substitution(rearrange(cipher, perm), dictionary)

'''
Paralleize code.
Split all possible permutations into 4 parts.
For each part run solve() parallely.
'''
if __name__ == '__main__':
    main_list = [0, 1, 2, 3, 4]
    all_perms = list(permutations(main_list))
    t1 = multiprocessing.Process(target=solve, args=(all_perms[:30],))
    t2 = multiprocessing.Process(target=solve, args=(all_perms[30:60],))
    t3 = multiprocessing.Process(target=solve, args=(all_perms[60:90],))
    t4 = multiprocessing.Process(target=solve, args=(all_perms[90:],))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
