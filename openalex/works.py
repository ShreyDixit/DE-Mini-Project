from API import API

api = API()

sub_concept_ids = ["C41008148"]

with open("cs_sub_concepts.txt", "r") as f:
    for line in f:
        sub_concept_ids.append(line.split(", ")[0].split("/")[-1])

# uhh https://openalex.org/I159176309
# tuhh https://openalex.org/I884043246
# haw https://openalex.org/I70451448
# hcu https://openalex.org/I2801160284
# hsu https://openalex.org/I190134885

query = "works?filter=institutions.id:https://openalex.org/I190134885,concepts.id:" + "|".join(sub_concept_ids)

api.run(query)