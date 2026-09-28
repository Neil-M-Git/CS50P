# dictionary demo

stud_dict1 = {
    "Harry" : "Gryffindor", 
    "Ron" : "Gryffindor", 
    "Hermione" : "Gryffindor", 
    "Draco" : "Slytherin"
}

for s in stud_dict1:  # noqa: PLC0206
    print(s, stud_dict1[s], sep= ", ")