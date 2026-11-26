import csv
from kg import KnowledgeGraph

#converte os textos das propriedades para um dicionario
def converter_propriedades(string):
    propriedades = {}
    
    if string == "":
        return propriedades
    
    for parte in string.split(";"):
        chave, valor = parte.split("=")
        propriedades[chave] = valor
        
    return propriedades

#carrega o grafo, primeiro os nos e dps as relacoes
def carregar_grafo(pasta="dados"):
    kg = KnowledgeGraph()
    
    with open(f"{pasta}/nos.csv", encoding="utf-8") as f:
        for linha in csv.DictReader(f):
            kg.adicionar_no(linha["nome"], linha["tipo"], converter_propriedades(linha["propriedades"]))
            
    with open(f"{pasta}/relacoes.csv", encoding="utf-8") as f:
        for linha in csv.DictReader(f):
            kg.adicionar_relacao(linha["origem"], linha["relacao"], linha["destino"])
    
    return kg

if __name__ == "__main__":
    kg = carregar_grafo()
    print(len(kg.nos))
    #print(kg.adj["Naruto"])
    #print(kg.consultar_no("Naruto"))
    print(kg.consultar_relacao("MEMBRO_DE", "Akatsuki"))
    print(kg.consultar_relacao("PAI_DE"))