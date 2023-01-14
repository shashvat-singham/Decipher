from itertools import permutations
import re
from sub_perm_decrypt import read_dictionary, substitution
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
    cipher = "wklsalq rf acrd nxoe hxle el wwlodld wl qcu dsvlgkx dbualq axdjoxxi cj qxl lrec. il scrso, sjo fsjo xhfu rs wklsaxci qjl eblde xj crp qsdn wl qcu lyxe msafsf. qbl dcxrxq af ncl qssl pmj ed sxhhud sxrc uqv. oxjf qsl pcisn hxjs qcoq exeh erq ulv rvq rf ncl qsxld. mq ervho lskp upv s rsxxnise, jr jlcd qdsf ysjfra! qs ia qcrrdic, vbqsk lcd bsldorah: etj_hzvrm_sr".lower()
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
    all_perms = list(permutations([2,3,4]))
    all_perms = [[0]+list(i)+[1] for i in all_perms]
    solve(all_perms)
