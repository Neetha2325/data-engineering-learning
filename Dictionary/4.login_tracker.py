users = ['john', 'bob', 'alex', 'alice', 'charlie', 'john',
         'alex', 'alice', 'john', 'alex']
login_tracker={}

for x in users:
    if x in login_tracker:
        login_tracker[x]+=1
    else:
        login_tracker[x]=1


for x,y in login_tracker.items():
    print(x,y)