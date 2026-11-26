total_outcomes = 52 
print("Total Outcomes (Total cards):", total_outcomes)
favorable_outcomes = int(input("Enter favorable outcomes (Face cards): "))
def calculate_probability(favorable, total):
    if favorable > total:
        #return favorable / total
        print("Favorable outcomes cannot exceed total outcomes.")
        
    return favorable / total

probability = calculate_probability(favorable_outcomes, total_outcomes)
print("Favorable Outcomes (Face cards):", favorable_outcomes)
print("Probability of drawing a face card:", f"{probability:.4f}")