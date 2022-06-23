from API import API

api = API()
computer_science = "C41008148"
sub_concepts = api.run(computer_science, concepts=True)["related_concepts"]

with open("cs_sub_concepts.txt", "w") as f:
    for concept in sub_concepts:
        f.write(concept['id'] + ", " + concept['display_name'] + "\n")