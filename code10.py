def min_coins(coins, amount):
    
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0 

    
    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
if __name__ == "__main__":
    coins = [2, 4, 10] 
    amount = 26     
    result = min_coins(coins, amount)
    print("Minimum number of coins required:", result)