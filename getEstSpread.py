'''
As it turns out, social media posts spread at an exponential rate! We've found that the estimated spread of a social post can be calculated using the following formula:

estimated_spread = average_audience_followers * ( num_followers^1.2 )
Copy icon
In the formula above, average_audience_followers refers to an average calculated from each number within the audiences_followers argument - which is a list containing the user's follower's individual follower count.

For example, if audiences_followers = [2, 4, 2, 19], then the influencer has 4 followers, and each of them has their own follower counts of 2, 4, 2, and 19 respectively.
'''

def get_estimated_spread(audiences_followers):
    average_audience_followers = (sum(audiences_followers) / len(audiences_followers))
    return average_audience_followers * (len(audiences_followers) ** 1.2)