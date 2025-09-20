def to_jaden_case(string):
    s = string.split()
    return ' '.join(ward.capitalize() for ward in s)
print(to_jaden_case("How can mirror be real if our eyes aren't real"))