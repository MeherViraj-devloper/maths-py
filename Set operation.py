A={1,2,3,4}
B={3,4,5,6}

union_set=A|B
intersection_set=A&B
difference_set=A-B
cartesian_product={(x,y) for x in A for y in B}

print("Set A:",A)
print("Set B:",B)
print("Union (A U B):",union_set)
print("Intersection (A n B):",intersection_set)
print("Difference (A - B):",difference_set)
print("Cartesian Product (A X B):",cartesian_product)