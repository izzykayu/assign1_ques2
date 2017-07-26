mass_dict = {'A': 71.03711360, 'a': 71.03711360, 'C': 103.0091854, 'c': 103.0091854, 'D': 115.0269428, 'd': 115.0269428,
             'E': 129.0425928, 'e': 129.0425928, 'F': 147.0684136, 'f': 147.0684136, 'G': 57.02146360, 'g': 57.02146360,
             'H': 137.0589116, 'h': 137.0589116, 'I': 113.0840636, 'i': 113.0840636, 'K': 128.0949626, 'k': 128.0949626,
             'L': 113.0840636, 'l': 113.0840636, 'M': 131.0404854, 'm': 131.0404854, 'N': 114.0429272, 'n': 114.0429272,
             'P': 97.05276360, 'p': 97.05276360, 'Q': 128.0585772, 'q': 128.0585772, 'R': 156.1011106, 'r': 156.1011106,
             'S': 87.03202820, 's': 87.03202820, 'T': 101.0476782, 't': 101.0476782, 'V': 99.06841360, 'v': 99.06841360,
             'W': 186.0793126, 'w': 186.0793126, 'Y': 163.0633282, 'y': 163.0633282}
list_aa = list(mass_dict.keys())
print(list_aa)
p_z_dict = {'ACACIMED': 2, 'acacimed': 2, 'ELEMYRATNE': 1, 'elemyratne': 1, 'wapwop': 3, 'WAPWOP': 3, 'zeittsieg': 2,
            'ZEITTSIEG': 2, 'desfbirc': 1, 'DESFBIRC': 1, 'ALTAATSIV': 3, 'altaatsiv': 3, 'MEINWOHC': 2, 'meinwohc': 2}
# p_z_dict for protein: charge
list_p_seq = list(p_z_dict.keys())  # list of protein seq for this assignment
temp_mass_list = []  # open data list for amino acid masses in input seq


def protein_m_z(seq):  # defining protein mass to charge function; variable as seq
    sum_p = 0
    for aa in list(seq):
        if aa in list_aa:
            m = mass_dict[aa]  # m is for mass of aa in pm
            temp_mass_list.append(m)  # creating temporary list of masses of aa entered
            ch = p_z_dict[seq]  # charge = p_z_dict[pro for protein seq for assignment]
            for num in temp_mass_list:  # creating function
                sum_p = sum_p + num
                mow = 18.010564684  # mass of water (mow)
                fin_mass = mow + sum_p  # fin_mass as final mass of input AA seq
                m_z = fin_mass / ch
                print('Mass (m):\t', '{:.2f}'.format(sum_p))  # formatted to two decimal places
                print('m/z:\t', '{:.2f}'.format(m_z), '\n')


def check(seq):
    c = 0
    for letter in list(seq):
        if letter in list_aa and seq in list_p_seq:
            c = c + 1
    return c

list_of_protein_dicts = [{'seq': 'ACACIMED', 'ch': 2},
                         {'seq': 'ELEMYRATNE', 'ch': 1},
                         {'seq': 'wapwop', 'ch': 3},
                         {'seq': 'zeittsieg', 'ch': 2},
                         {'seq': 'DESFBIRC', 'ch': 1},
                         {'seq': 'altaatsiv', 'ch': 3},
                         {'seq': 'MEINWOHC', 'ch': 2}]

for aa_seq in list_p_seq:
    x = check(aa_seq)
    if x == len(aa_seq):
        protein_m_z(aa_seq)
    elif x < len(aa_seq):
            print(aa_seq, 'is an invalid protein sequence.\n')

