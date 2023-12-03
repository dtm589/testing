'''
Our data scientists at Socialytics have found that the growth of the average influencer's follow count is roughly the same growth rate as the Fibonacci sequence! In other words, after 6 weeks of good Instagram posts, the average influencer will have 8 followers. After 7 weeks, 13 followers, and so on.

Trouble is, our current implementation of the fib function takes so long to complete that when our influencers navigate to their analytics page it often never completes loading!

Alter the fib function according to the given algorithm to give it a polynomial runtime.
'''

def fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    
    grandparent = 0
    parent = 1
    current = 0
    for i in range(n-1):
        current = grandparent + parent
        grandparent = parent
        parent = current
    return current