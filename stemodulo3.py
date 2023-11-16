candidatos = [
    {"Meire": "1", "resultado": "4_3_8_7"},
    {"Hanna": "2", "resultado": "3_5_7_6"},
    {"Debora": "3", "resultado": "5_4_6_8"},
    {"Albino": "4", "resultado": "4_4_7_7"},
    {"Arthur": "5", "resultado": "4_4_8_8"},
]

def buscar_candidatos(notas_minimas):
    candidatos_atendem_critérios = []
    for candidato in candidatos:
        notas_candidato = list(map(int, candidato["resultado"].split("_")))
        if all(nota_candidato >= nota_minima for nota_candidato, nota_minima in zip(notas_candidato, notas_minimas)):
            candidatos_atendem_critérios.append(candidato["nome"])
    return candidatos_atendem_critérios

nota_entrevista = int(input("Informe a nota mínima desejada na entrevista: "))
nota_teste_teórico = int(input("Informe a nota mínima desejada no teste teórico: "))
nota_teste_prático = int(input("Informe a nota mínima desejada no teste prático: "))
nota_soft_skills = int(input("Informe a nota mínima desejada em soft skills: "))

candidatos_selecionados = buscar_candidatos([nota_entrevista, nota_teste_teórico, nota_teste_prático, nota_soft_skills])

print("Candidatos que atendem aos critérios:")
for candidato in candidatos_selecionados:
    print(candidato)
