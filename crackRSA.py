#Fermat's Little Theorem: a^p == a mod p, a^(p-1) == 1 mod p
n = 4654252230393111226989449826741007006486078009450861095070222439898324342353927553909251532232407850265642079868425916328810273416481567992145162141358151
#n ends with 1, which means that 2 is coprime with n
# then by Fermat's little theorem, a^(p-i) must be equal to 1 mod p if it is prime
askcomposite = Mod(2,n)^(n-1)
TorF = (1==askcomposite)
print (TorF) #false therefore, n is not a prime number, therefore it is composite number
#hint: n = p*q.  p and q are little close then we assume that n = q^2 = p^2
integer_n = int(n^(1/2))
possible_p = previous_prime(integer_n)
possible_q = next_prime(integer_n)
# let possible_n be calculation of possible_p*possible_q which derived from n = p*q
possible_n = possible_p * possible_q
askequal = (n==possible_n)
print "p and q = " + str(possible_p) + " and " + str(possible_q)
print (askequal) #True,
#p and q = 68222080226222296181917368518534332259513625527062166102114730123514248558349 and 68222080226222296181917368518534332259513625527062166102114730123514248558499
