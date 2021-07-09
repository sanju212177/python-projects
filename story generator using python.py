import random
when = ['Two years ago', 'Yesterday', 'Last night', 'A long time ago','On 15th Dec']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
live_in = ['America','India', 'Germany', 'Australia', 'England']
went = ['cinema', 'university','seminar', 'school', 'laundry']
happened = ['made a lot of friends','eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
