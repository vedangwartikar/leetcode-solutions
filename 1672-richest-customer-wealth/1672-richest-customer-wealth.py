class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = -1
        for customer in accounts:
            total = sum(customer)
            if total > wealth:
                wealth = total
        return wealth