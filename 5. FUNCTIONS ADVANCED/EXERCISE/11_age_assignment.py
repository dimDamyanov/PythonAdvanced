def age_assignment(*args, **kwargs):
    age_dict = {}
    for key, value in kwargs.items():
        for name in args:
            if name[0] == key:
                age_dict[name] = value
                break
    return age_dict


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
