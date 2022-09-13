

import uuid
import random
import hashlib


# staking = {uuid.uuid4().hex: (random.randint(1, 10), random.randint(10000000, 100000000000000)) for i in range(5, 500000)}
staking = {uuid.uuid4().hex: (random.randint(1, 3), random.randint(10000000, 1000000000)) for i in range(10**7)}
for i in range(100):
    staking[uuid.uuid4().hex] = (10, random.randint(10000000, 100000000000000))
# {
#     'abc123': (30, 123456),
#     '09876f': (90, 234567890),
# }


total = sum([i[0] for i in staking.values()])
print('total', total)
# print(staking_secret)

blockhash = uuid.uuid4().hex
print('blockhash', blockhash)

# pointer = (int(blockhash, 16)) % total
# print('pointer', pointer)
# for user, (token, secret) in staking.items():
#     user_pointer = (int(blockhash, 16) + secret) % total
#     rate = abs(user_pointer - pointer)/token
#     if rate < 3:
#         print(user, rate, token)

# pointer = (int(blockhash, 16)) % total
# print('pointer', pointer)
print('user rate pointer token')
for user, (token, secret) in staking.items():
    user_pointer = (int(blockhash, 16) + secret) % total
    rate = user_pointer/token
    if rate < 5:
        print(user, '%f' % rate, user_pointer, token)

# a user id in the staking table is chose to generate next block
# blockhash = hash(prev_hash + user_pk + height + data)

# we cannot use blockhash to decide the next miner
# as data is decided by the current miner

# pointer = hash(prev_hash + user_pk)
# current miner cannot decide pointer

# previous block 
# current block 
# next block 


# block 1 user1                                 hash1
# block 2 user2                                 hash2
# block 3 user3 <- hash1 + user2 + data2        hash3 <- hash2 + user3 + height + data3
# block 4 user4 <- hash2 + user3 + data3        hash4 <- hash3 + user4 + height + data4
# block 5 user5 <- hash3 + user4 + data4        hash5 <- hash4 + user5 + height + data5

# user5 is decided by hash3 user4 data4
# hash3 is decided by data3 as hash2 and user3 is fixed
# when hash3 is generated, user4 is decided, but data4 is unknown.
# so user5 is decided by data4

# import uuid
# import random

# staking = {uuid.uuid4().hex: (random.randint(1, 100), random.randint(10000000, 100000000000000)) for i in range(5, 500000)}
# total = sum([i[0] for i in staking.values()])
# blockhash = uuid.uuid4().hex

# pointer = (int(blockhash, 16)) % total
# print('pointer', pointer)
# for user, (token, secret) in staking.items():
#     user_pointer = (int(blockhash, 16) + secret) % total
#     rate = abs(user_pointer - pointer)/token
#     if rate < 3:
#         print(user, rate, token)

