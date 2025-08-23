
# this is an implementation of the apriori  algorithm with the naive approach. 

# pseudocode

# 1. Input: transaction database T, min_support threshold.
# 2. Generate all possible itemsets from items in T (power set).
# 3. For each candidate itemset:
#      - Count how many transactions contain it.
#      - Compute support = count / total_transactions.
# 4. Keep only itemsets with support >= min_support.
# 5. Output frequent itemsets

# 👉 Data Structures Used:

# list of sets → store transactions (easy membership check).

# itertools.combinations → generate candidate itemsets.

# dict → store support counts.


from itertools import combinations

def naive_apriori(transactions, min_support):
    """
    Naive Apriori implementation (inefficient).
    
    Parameters:
        transactions (list of sets): Transaction database.
        min_support (float): Minimum support threshold (0-1).
    
    Returns:
        dict: Frequent itemsets with their support values.
    """
    # Number of transactions
    num_transactions = len(transactions)
    
    # Get all unique items
    items = set()
    for t in transactions:
        items.update(t)
    
    # Generate all possible itemsets (powerset, excluding empty set)
    all_candidates = []
    for size in range(1, len(items) + 1):
        all_candidates.extend(combinations(items, size))
    
    # Count support for each candidate
    frequent_itemsets = {}
    for candidate in all_candidates:
        candidate_set = set(candidate)
        count = sum(1 for t in transactions if candidate_set.issubset(t))
        support = count / num_transactions
        
        if support >= min_support:
            frequent_itemsets[tuple(sorted(candidate))] = support
    
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
frequent_itemsets = naive_apriori(transactions, min_support)

print("Frequent Itemsets (Naive):")
for itemset, support in frequent_itemsets.items():
    print(itemset, "->", round(support, 2))



# Complexity (Naive Version):

# Time Complexity:

# Generates all possible itemsets → 
# 2
# 𝑛
# 2
# n
#  where n = \text{#unique items}.

# For each itemset, scans all transactions → 
# 𝑂
# (
# 𝑚
# )
# O(m), where m = \text{#transactions}.

# Total: O(m × 2^n) → exponential!

# Space Complexity:

# Stores all candidate itemsets → O(2^n).

# Support counts in dictionary → O(2^n).

# ⚠️ This is very inefficient but helps us understand the brute force approach.
