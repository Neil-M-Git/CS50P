# extended dictionary demo

stud_dict2 = [
    {"Name" : "Harry", "House" : "Gryffindor", "Patronus" : "Stag"},
    {"Name" : "Ron", "House" : "Gryffindor", "Patronus" : "Jack Russell Terrier"},
    {"Name" : "Hermione", "House" : "Gryffindor", "Patronus" : "Otter"},
    {"Name" : "Draco", "House" : "Slytherin", "Patronus" : None}
]

for s in stud_dict2:
    print(s["Name"], s["House"], s["Patronus"], sep= ", ")