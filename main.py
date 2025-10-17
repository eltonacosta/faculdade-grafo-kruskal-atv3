def kruskal(grafo_vertices, grafo_arestas):
    parent = {vertice: vertice for vertice in grafo_vertices} # Cada cidade é sua própria capital
    agm_arestas = []
    custo_total = 0

    def find(vertice):
        if parent[vertice] == vertice:
            return vertice
        parent[vertice] = find(parent[vertice])
        return parent[vertice]

    def union(v1, v2):
        root1 = find(v1)
        root2 = find(v2)
        if root1 != root2:
            parent[root2] = root1
    
    grafo_arestas.sort()

    for peso, v1, v2 in grafo_arestas:
        if find(v1) != find(v2):
            union(v1, v2)
            agm_arestas.append((v1, v2, peso))
            custo_total += peso

    return agm_arestas, custo_total


vertices_kruskal = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'}
arestas_kruskal = [
    (4, 'a', 'b'), (8, 'a', 'h'), (8, 'b', 'c'), (11, 'b', 'h'),
    (7, 'c', 'd'), (4, 'c', 'f'), (2, 'c', 'i'), (9, 'd', 'e'),
    (14, 'd', 'f'), (10, 'e', 'f'), (2, 'g', 'f'), (6, 'i', 'g'),
    (1, 'g', 'h'), (7, 'i', 'h')
]

arestas_resultado, custo_resultado = kruskal(vertices_kruskal, arestas_kruskal)

print("Arestas da Árvore Geradora Mínima (Kruskal):")
for v1, v2, peso in arestas_resultado:
    print(f"  {v1} --({peso})--> {v2}")

print(f"\nCusto Total da AGM: {custo_resultado}")