A={1,2,3}
B={2,4,6}
f={1:2, 2:4, 3:6}

def is_injective(f):
    images = list(f.values())
    return len(images) == len(set(images))
def is_surjective(f, B):
    return set(f.values()) == B
def is_bijective(f, B):
    return is_injective(f) and is_surjective(f, B)
injective = is_injective(f)
surjective = is_surjective(f, B)
bijective = is_bijective(f, B)

print("Domain A:",A)
print("Codomain B:",B)
print("Function f:",f)
print("Injective:",injective)
print("Surjective:",surjective)
print("Bijective:",bijective)