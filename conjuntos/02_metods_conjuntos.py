conj_a = {1,2,3,4}
conj_b = {3,4,5,6}
conj_c = {5,6,7,8}

print(conj_a.union(conj_b)) #union
print(conj_a.union(conj_b, conj_c)) #union com 3 conjuntos 
print(conj_a.intersection(conj_b)) #intersection 
print(conj_a.intersection(conj_b, conj_c)) #intersection com 3 conjuntos - Retornou vazio, pois não há elemento nos 3 simultaneamente.
print(conj_a.difference(conj_b)) #difference
print(conj_a.difference(conj_b, conj_c)) #difference com 3 conjuntos
print(conj_a.symmetric_difference(conj_b)) #symmetric_difference - Só pode com 2 conjuntos.

