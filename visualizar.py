
from pyvis.network import Network


def gerar_html(kg, arquivo="naruto.html"):

    # Cria a representação visual do grafo
    rede = Network(
        height="850px",
        width="100%",
        directed=True,
        bgcolor="#F8FAFC",
        font_color="#1E293B",
        cdn_resources="in_line"
    )

    # Define uma cor para cada tipo de entidade
    cores = {
        "Personagem": "#FDBA74",
        "Cla": "#C4B5FD",
        "Vila": "#93C5FD",
        "Time": "#86EFAC",
        "Organizacao": "#CBD5E1",
        "Kekkei Genkai": "#F9A8D4",
        "Bijuu": "#FCA5A5",
        "Jutsu": "#FDE68A",
        "Natureza": "#67E8F9"
    }

    # Adiciona os vértices
    for nome, dados in kg.nos.items():

        tipo = dados["tipo"]
        propriedades = dados["propriedades"]

        # Informações exibidas ao passar o mouse
        informacoes = f"{nome}\nTipo: {tipo}"

        for chave, valor in propriedades.items():
            informacoes += f"\n{chave}: {valor}"

        rede.add_node(
            nome,
            label=nome,
            shape="box",
            color=cores.get(tipo, "#CBD5E1"),
            title=informacoes,
            font={"size": 18},
            margin=15,
            borderWidth=2
        )

    # Adiciona as arestas
    for origem in kg.adj:

        for relacao, destino in kg.adj[origem]:

            rede.add_edge(
                origem,
                destino,
                label=relacao,
                title=relacao,
                color="#64748B",
                width=2,
                font={
                    "size": 12,
                    "align": "middle",
                    "background": "#F8FAFC",
                    "strokeWidth": 0
                }
            )

    # Ajusta o espaçamento entre os vértices
    rede.barnes_hut(
        gravity=-8000,
        central_gravity=0.1,
        spring_length=300,
        spring_strength=0.02,
        damping=0.5,
        overlap=1
    )

    # Gera e salva o HTML em UTF-8
    html = rede.generate_html()

    with open(arquivo, "w", encoding="utf-8") as arquivo_html:
        arquivo_html.write(html)

    print(f"Grafo salvo em {arquivo}")

# Teste inicial da visualizacao
if __name__ == "__main__":
    from carregar import carregar_grafo
    grafo = carregar_grafo()
    
    gerar_html(grafo)