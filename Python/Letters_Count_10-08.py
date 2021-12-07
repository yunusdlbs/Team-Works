sentence = input("Enter your sentence: ")
sen_dict={}
for i in sentence:
    if i not in sen_dict:
        sen_dict[i]=1
    else:
        sen_dict[i]+=1
print(sen_dict)
