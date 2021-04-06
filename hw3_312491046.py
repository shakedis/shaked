from functools import reduce

print('###------ Homework 3: Shaked Israel 312491046 ------###')

######### Part A

print('@----- A.1')
def display_camel_temp(camel):
    """returns Catalog name and Temperature of a camel"""
    print ('Catalog name: ',camel[0])
    print('Temperature: ', camel[1])

camel1= ['cml_1', '35.5 C']
display_camel_temp(camel1)

print('@----- A.2')
def get_camel_temp_fahr(camel):
    """convert temperature C to F"""
    F = ((9/5) * float(camel[1])) + 32
    print('Camel number', camel[0][4:5], '-', camel[1], 'Celsius', F, 'Fahrenheit')
    return F

#camel1 = ['cml_1', 35.5]
#print(get_camel_temp_fahr(camel1))

print('@----- A.3')
def add(x, y):
    """returns x+y"""
    return x + y

def camels_temp_fahr(camel_list):
        """returns sum of temp' of a camel's list"""
        x = list(map(get_camel_temp_fahr, camel_list))
        z=reduce(add, x)
        print('Temperatures in Fahrenheit summed: ', z)
        return z

#L = [['cml_1', 38.5], ['cml_2', 36.9], ['cml_3', 39.3], ['cml_4', 35.8]]
#print(camels_temp_fahr(L))


###### Part B
print('@----- B.1')
inserts=['GGCTATATAGCGCGATGCTGATCGCGCGCGATGCTAGCTGCTCCGCGCGCGAAT',
'TGAATAGAATTATATAGAATGACGCGCGATGAATCCGCTACGCGATAAGTCCGTAA',
'ACCGCGCTATATAGCGTAAGCTGAATCGCCGCGCGTAAGCTGAATCGCTAGGGGCCGCC',
'TGGTATATACGCGCGCGCCCGCGAATGCTGATCGCCTCGCGCGTAAGATGC',
'CCGTGAATGCCTCGTATATACGCGCTGAATGCCTGCCGCGCGCGCGCGCGCG']

print('@----- B.2')

def list_G_index(list):
    """returns a list of integers representing the index of the first ’G’ character in each string"""
    x= list.index('G')
    return x

def seq_list_G_index(seq_list):
    """returns a list of integers representing the index of the first ’G’ character in each string"""
    A=map(list_G_index, (seq_list))
    return A

#inserts_G_indices= seq_list_G_index(inserts)
#print(list((inserts_G_indices)))

print('@----- B.3')
def integer(str):
    """convert a string's (TATATA) index into an int"""
    return int(str.index('TATATA')+5)

#T='CDVTATATANCJD'
#print(integer(T))

def remove_adaptor(s):
    """remove all letters till TATATA included"""
    New = s[integer(s):-1]
    return New

trimmed_inserts= list(map(remove_adaptor, (inserts)))
print(list(trimmed_inserts))

#I='GGCTATATAGCGCGATGCTGATCGCGCGCGATGCTAGCTGCTCCGCGCGCGAAT'
#print(remove_adaptor(I))

print('@----- B.4')
def insert_to_vector(vector, insert):
    """returns a list of 2 elements sequence and its length"""
    vector= vector.lower()
    answer= (vector[:10] + insert + vector[11:])
    return answer, len(answer)

print('@----- B.5')

cloning_vec = ['CGTACAGCGATCGTACATGCGATCCACTCGGCTATCG'] * len(trimmed_inserts)
full_vectors= list(map(insert_to_vector, cloning_vec, trimmed_inserts))
print(full_vectors)

######### Part C

print('@----- 3.1')
def seq_Tm(seq):
    """returns the calculation of melting temp"""
    if len(seq) < 13:
        Tm= (2 * ((seq.count('A') + seq.count('T'))) + (4 * (seq.count('G')+ seq.count('C'))))
        return Tm
    else:
        Tm= 64.9 + ((41 * (seq.count('G') + seq.count('C') -16.4)) / (seq.count('A') + seq.count('T') + seq.count('G') + seq.count('C')))
        return Tm

print('@----- 3.2')
from functools import reduce

def concat_strings_w_TACTAC(seq_list):
    """returns a sequence of DNA seq with TACTAC between """
    x= list(map(add, seq_list, (['TACTAC'] * len(seq_list))))
    return ''.join(x)

seq_list=['ATCGGG', 'GACGATCGC', 'CGATCGTGTA']

#print(concat_strings_w_TACTAC(seq_list))

print('@----- 3.3')
list_of_lists= [['TTTTTCCCC', 'AAAAA'],
['ATCGGG', 'GACGATCGC', 'CGATCGTGTA', 'CACGTC'],
['CATACCGTCT', 'CGTCTCTAC', 'AACCGCAT'],
['GCATCGATCG', 'AGCTC', 'CCGCTAA', 'GAGC', 'GTAGGAG']]

dna_special_list=list(map(concat_strings_w_TACTAC, list_of_lists))
print(dna_special_list)

print('@----- 3.4')
def melt_temp_for_list(dna_list, sum_or_mean):
    """returns the sum or the mean of DNA seq"""
    if sum_or_mean == 'sum':
        return sum(map(seq_Tm,dna_list))
    else:
        return sum(map(seq_Tm, dna_list)) / len(dna_list)

print('@----- 3.5')

dna_special_Tm_sum = melt_temp_for_list(dna_special_list, 'sum')
dna_special_Tm_mean= melt_temp_for_list(dna_special_list, 'mean')

print(dna_special_Tm_sum)
print(dna_special_Tm_mean)

######### Bonus

print('@----- *Bonus')
def mult(x,y):
    """returns x*y"""
    return x * y

def calc_digits(number, n, operation):
    """returns sum or multiply of the digits in a number"""
    if operation == 'sum':
        x= list(str(number))
        y=list(map(int, x))
        z= reduce(add, y)
        return z
    elif operation == 'multiply':
        a = list(str(number))
        b = list(map(int, a))
        c = reduce(mult, b)
        return c
    else:
        return 'calc_digits got an unknown operation'

#calc_digits(234, 3, 'sum')



