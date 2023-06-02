import math

def replace_domain(email,newdomain,olddomain = 'kaaj.com'):
    firstname = ''
    count = -1
    domain_name = ''
    final = ''
    for item in email:
        if item == '@':
            firstname += item
            count += 1
            break
        else:
            firstname += item
            count += 1
    total_length = len(email)
    start = count+1
    while start <= total_length -1:
        domain_name += email[start]
        start += 1
    if domain_name==newdomain :
        return f'Unchanged : {firstname}{domain_name}'
    else:
        return f'Changed : {firstname}{newdomain}'

address=input("Enter your mail address: ")
domain='sheba.xyz'
a=replace_domain(address,domain)
print(a)
