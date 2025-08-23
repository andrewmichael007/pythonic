# this is the optimized implementation of the apriori algorithm 

# pseudocode

# 1. Input: transaction database T, min_support threshold.
# 2. Generate frequent 1-itemsets (support ≥ min_support).
# 3. For k = 2 to max:
#       - Generate candidate itemsets of size k from frequent (k-1)-itemsets.
#       - Prune candidates whose subsets are not frequent.
#       - Count support by scanning transactions.
#       - Keep only itemsets with support ≥ min_support.
# 4. Stop when no frequent itemsets are found.
# 5. Output frequent itemsets.

# 👉 Data Structures Used:

# set → for transactions and itemsets (fast subset checks).

# dict → mapping itemsets → support values.

# Efficient candidate generation via joining frequent itemsets.


from itertools import combinations

def apriori(transactions, min_support):
    """
    Efficient Apriori implementation (with pruning).
    
    Parameters:
        transactions (list of sets): Transaction database.
        min_support (float): Minimum support threshold (0-1).
    
    Returns:
        dict: Frequent itemsets with their support values.
    """
    num_transactions = len(transactions)
    frequent_itemsets = {}
    
    # Step 1: Generate frequent 1-itemsets
    item_counts = {}
    for t in transactions:
        for item in t:
            item_counts[frozenset([item])] = item_counts.get(frozenset([item]), 0) + 1
    
    current_frequents = {
        item: count / num_transactions
        for item, count in item_counts.items()
        if count / num_transactions >= min_support
    }
    
    frequent_itemsets.update(current_frequents)
    
    k = 2
    while current_frequents:
        # Step 2: Generate candidate k-itemsets
        items = list(current_frequents.keys())
        candidates = set()
        
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                union_set = items[i].union(items[j])
                if len(union_set) == k:
                    candidates.add(union_set)
        
        # Step 3: Prune candidates
        pruned_candidates = set()
        for candidate in candidates:
            subsets = combinations(candidate, k - 1)
            if all(frozenset(subset) in current_frequents for subset in subsets):
                pruned_candidates.add(candidate)
        
        # Step 4: Count support
        candidate_counts = {c: 0 for c in pruned_candidates}
        for t in transactions:
            for candidate in pruned_candidates:
                if candidate.issubset(t):
                    candidate_counts[candidate] += 1
        
        # Step 5: Keep frequent itemsets
        current_frequents = {
            c: count / num_transactions
            for c, count in candidate_counts.items()
            if count / num_transactions >= min_support
        }
        
        frequent_itemsets.update(current_frequents)
        k += 1
    
    return frequent_itemsets


# Example usage
transactions = [
    {"milk", "bread", "eggs"},
    {"milk", "bread"},
    {"milk", "eggs"},
    {"bread", "eggs"},
    {"milk", "bread", "butter"},
]

min_support = 0.4
frequent_itemsets = apriori(transactions, min_support)

print("\nFrequent Itemsets (Efficient):")
for itemset, support in frequent_itemsets.items():
    print(set(itemset), "->", round(support, 2))



# Complexity (Optimized Version):

# Time Complexity:

# Instead of all 
# 2
# 𝑛
# 2
# n
#  subsets, only generates candidates from frequent itemsets.

# Still worst-case exponential, but much faster in practice.

# Approx: 
# 𝑂
# (
# 𝑚
# ×
# 𝑘
# ×
# 𝐶
# )
# O(m×k×C), where 
# 𝐶
# C is number of candidates after pruning.

# Space Complexity:

# Stores only frequent itemsets per level, not all → O(C) (much less than 
# 2
# 𝑛
# 2
# n
# ).
