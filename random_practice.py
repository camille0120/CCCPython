import random
noun1=["莊仲薇","葉文萃","林璟衡"]
verb=["吃","喜歡","打"]
noun2=["大便","石頭","蟑螂"]

def random_sample(list1):
    word=random.sample(list1,1)[0]
    return word

def random_sentence(list1,list2,list3):
    sentence=random_sample(list1)+random_sample(list2)+random_sample(list3)+"。"
    return sentence

for i in range(10):
    print(random_sentence(noun1, verb, noun2))