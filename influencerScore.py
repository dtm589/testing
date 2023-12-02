'''
We want to be able to give our influencers a simple "influencer score". It will be a small number, like less than 100. This will make it easier to "rank" them against each other in terms of how many people they are "influencing".

Complete the get_influencer_score function. The formula for an influencer score is:

average_engagement_percentage * log2(num_followers)
'''

import math

def get_influencer_score(num_followers, average_engagement_percentage):
    return average_engagement_percentage * math.log(num_followers,2)