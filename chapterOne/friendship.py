#list of users represented as dicts with id and name

users = [{"id": 0, "name": "Hero"},
         {"id": 1, "name": "Dunn"},
         {"id": 2, "name": "Sue"},
         {"id": 3, "name": "Chi"},
         {"id": 4, "name": "Thor"},
         {"id": 5, "name": "Clive"},
         {"id": 6, "name": "João"},
         {"id": 7, "name": "Nicolas"},
         {"id": 8, "name": "Maria"},
         {"id": 9, "name": "Gabriel"},]

#list of pairs of ids representing friendships between users
friendship_pairs = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9),]

# empty dict to catch friendships, where keys are user ids and values are lists of friends' ids
friendships = {user["id"]: [] for user in users}

# populate the friendships dict with the friendship pairs
for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

print(friendships) 

# function to count the number of friends a user has, given the user dict and the friendships dict
def number_of_friends(user):
    user_id = user["id"]
    friends_ids = friendships[user_id]
    return len(friends_ids)

# total connections
total_connections = sum(number_of_friends(user)for user in users)
print(total_connections)
num_users = len(users)

#average connections by users
avg_conn = total_connections / num_users
print(avg_conn)

# number of friends by id
num_friends_by_id = [(user["id"], number_of_friends(user))for user in users]

num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True)
print(num_friends_by_id) # each pair is: user_id and number of friends

# In that network, we implemented a metric called degree cetrality, which is the number of friends a user has. 


# creating a suggest_friend function

def adua_ids_bad(user):
    
    #adua means ("friends of a friends") in portuguese
    return [adua_id for friend_id in friendships[user["id"]]
            for adua_id in friendships[friend_id]]
    
print(adua_ids_bad(users[0])) # this will return the ids of the friends of the friends of user 0, but it will include the user itself and its direct friends, which is not what we want. We want to exclude those.

# now, we gonna generate a set of user ids that we want to exclude from the suggestions, which are the user itself and its direct friends.

from collections import Counter

def adua_ids_good(user):
    user_id = user["id"]
    return Counter(adua_id for friend_id in friendships[user_id]
            for adua_id in friendships[friend_id]
            if adua_id != user_id and adua_id not in friendships[user_id])

print(adua_ids_good(users[3])) # this will return a Counter object with the ids of the friends of the friends of user 3, excluding user 3 itself and its direct friends. The keys of the Counter object are the ids of the suggested friends, and the values are the number of mutual friends they have with user 3.


#interest of users

interests = [(0, "Hadoop"),( 0,"Big Data"), (0, "HBase"), (0, "Java"), (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
             (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"),(1, "HBase"),(1, "Postgres"),(2, "Python"),(2, "scikit-learn"),
             (2, "scipy"),(2, "numpy"),(2, "statsmodels"),
             (3, "R"),(3, "Python"),(3, "statistics"),(3, "regression"),(3, "probability"),
             (4, "machine learning"),(4, "regression"),(4, "decision trees"),(4, "libsvm"),
             (5, "Python"),(5, "R"),(5, "Java"),(5, "C++"),(5, "Haskell"),
             (6,"statistics"),(6,"probability"),(6,"mathematics"),(6,"theory"),
             (7,"machine learning"),(7,"scikit-learn"),(7,"Mahout"),(7,"neural networks"),
             (8,"neural networks"),(8,"deep learning"),(8,"Big Data"),(8,"artificial intelligence"),
             (9,"Hadoop"),(9,"Java"),(9,"MapReduce"),(9,"Big Data")]

print(interests)
    
    
# basic function to find users with a common interest

def data_scientists_who_like(target_interest):
    return [user_id for user_id, user_interest in interests
            if user_interest == target_interest]

print(data_scientists_who_like("Python")) # this will return the ids of the users who have "Python" as an interest. In this case, it will return [2, 3, 5].

# Buildind indexes to make the search faster and more efficient

from collections import defaultdict

user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)  
    
print(user_ids_by_interest) # this will return a defaultdict where the keys are the interests and the values are lists of user ids that have that interest. For example, "Python" will have the value [2, 3, 5].

interest_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interest_by_user_id[user_id].append(interest)

print(interest_by_user_id[0]) # this will return the list of interests for user 0, which is ["Hadoop", "Big Data", "HBase", "Java", "Spark", "Storm", "Cassandra"].

# now we can use these indexes to find users with a common interest more efficiently.

def most_common_interests_with(user):
    return Counter(interested_user_id 
                for interest in interest_by_user_id[user["id"]]
                for interested_user_id in user_ids_by_interest[interest]
                if interested_user_id != user["id"])

print(most_common_interests_with(users[0])) # this will return a Counter object with the ids of the users who have at least one interest in common with user 0, and the number of interests they have in common. For example, user 9 has 3 interests in common with user 0, so it will have the value 3 in the Counter object.
    
    