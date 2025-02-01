def find_mutual_friends(network, friend):
    if friend not in network:
        return "This friend is not in the network."
    
    mutual_friends = set()
    for other_friend in network:
        if other_friend != friend:
            mutuals = network[friend] & network[other_friend]
            if mutuals:
                mutual_friends.update(mutuals)
    
    return mutual_friends if mutual_friends else "No mutual friends found."


social_network = {
    "Alice": {"Bob", "Charlie", "David"},
    "Bob": {"Alice", "Charlie", "Eve"},
    "Charlie": {"Alice", "Bob", "Frank"},
    "David": {"Alice"},
    "Eve": {"Bob"},
    "Frank": {"Charlie"}
}


friend = input("Enter the friend's name: ")
print(f"Mutual friends for {friend}: {find_mutual_friends(social_network, friend)}")