
from itertools import combinations

#this function fetches all possible subsequences (i.e. non-contiguous substrings) in a word
def get_all_subs(word):
    word_length = len(word) + 1
    combs = []
    all_subs=[]
    for l in range(1, word_length):
        combs.append(list(combinations(word, l)))
    for c in combs:
        for t in c:
            all_subs.append(''.join(t))
    return all_subs

#this function fetches all contiguous substrings in a particular word - this is helpful for the later method
def get_contiguous_substring(word):
    res = [word[x:y] for x, y in combinations(
            range(len(word) + 1), r = 2)]
    return res

#main logic of finding pronounciable substrings
def filter_pronounciable(subs):
    vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
    pronounciable_subs = []

    """  the idea here is to look at all the substrings individually, for 3 cases:
     - if its just ONE letter, a vowel is assumed to be 'pronounciable' while a consonant is not
     - if its TWO letters, its deemed 'pronounciable' when (at-least) one vowel is after (at-most) one consonant 
     - if its THREE or MORE letters, it searches for a contiguous block of 3 consonants in that substring,
     because only then is the condition not met (>=1 vowel after <=2 consonants)
    
    """
    for sub in subs:
        if len(sub)==1:
            if sub in vowels:
                pronounciable_subs.append(sub)
        elif len(sub)==2:
            # ideally in a real-life parser the order shouldnt matter: 
            # a vowel before a consonant should also work but isn't put because of the scope of this assignment
            if sub[0] not in vowels and sub[1] in vowels:
                pronounciable_subs.append(sub)
        else:
            # the contiguous substrings and NOT all the subsequences, since we'll be checking the indices of the characters
            all_combs = get_contiguous_substring(sub)
            flag=0
            for comb in all_combs:
                if len(comb)==3:
                    if comb[0] not in vowels and comb[1] not in vowels and comb[2] not in vowels:
                        # debug statement is added for references which shows which combinations aren't pronounciable
                        # print(comb+" is not pronounciable, hence "+sub+" is not added.")
                        flag=1
                        break
            if flag==0:
                pronounciable_subs.append(sub)

    return pronounciable_subs



# main program for execution
if __name__=="__main__":
    str = input("Enter your word=> ")
    all_subs = get_all_subs(str)
    #print("\nALL SUBSEQUENCES ARE: {}".format(all_subs))
    
    result = filter_pronounciable(all_subs)

    print("\n{}: ".format(str))
    print(*result, sep=", ")