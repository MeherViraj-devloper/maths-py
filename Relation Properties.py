A={1,2,3}
R={(1,1),(2,2),(3,3),(1,2),(2,1)}
def is_reflexive(A, R):  # Check Reflexive
    for a in A:
        if (a, a) not in R:
            return False
    return True
def is_symmetric(R):   # Check Symmetric
    for (a, b) in R:
        if (b, a) not in R:
            return False
    return True
def is_transitive(R):   # Check Transitive
    for (a, b) in R:
        for (c, d) in R:
            if b == c and (a, d) not in R:
                return False
    return True
reflexive = is_reflexive(A, R)        
symmetric = is_symmetric(R)
transitive = is_transitive(R)
print("Set A:",A)
print("Relation R:",R)
print("Reflexive:",reflexive)
print("Symmetric:",symmetric)
print("Transitive:",transitive)
if reflexive and symmetric and transitive:
    print("Equivalence Relation: Yes")
else:
    print("Equivalence Relation: No")



