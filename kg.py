class KnowledgeGraph:
    def __init__(self):
        self.nos = {}
        self.adj = {}
        self.adj_rev = {}

    def adicionar_no(self, nome, tipo, propriedades=None):
        if propriedades is None:
            propriedades = {}
        if nome in self.nos:
            raise ValueError(f"O nó {nome} ja existe")
        
        self.nos[nome] = {"tipo": tipo, "propriedades": propriedades}
        self.adj[nome] = []
        self.adj_rev[nome] = []
            
    def adicionar_relacao(self, origem, relacao, destino):
        if origem not in self.nos or destino not in self.nos:
            raise KeyError(f"{origem} ou {destino} nao existem")
        if (relacao, destino) in self.adj[origem]:
            return
        
        self.adj[origem].append((relacao, destino))
        self.adj_rev[destino].append((relacao, origem))

    def remover_relacao(self, origem, relacao, destino):
        if (relacao, destino) not in self.adj[origem]:
            raise KeyError(f"A relação ({origem}, {relacao}, {destino}) não existe")
        
        self.adj[origem].remove((relacao, destino))
        self.adj_rev[destino].remove((relacao, origem))

    def remover_no(self, nome):
        if nome not in self.nos:
            raise KeyError(f"O nó {nome} nao existe")
        
        for relacao, destino in self.adj[nome]:
            self.adj_rev[destino].remove((relacao, nome))
        for relacao, origem in self.adj_rev[nome]:
            self.adj[origem].remove((relacao, nome))
            
        del self.nos[nome]
        del self.adj[nome]
        del self.adj_rev[nome]
            
