# traverse multiple list simultaneusly using zip function

names = ["ram","shyam","ravi","karan"]
city = ["lucknow","kanpur","delhi","mumbai"]


for n,c in zip(names,city):
    print(f'{n} lives in {c}')