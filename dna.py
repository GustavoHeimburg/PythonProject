import random

def gerar_dna(tamanho):
    bases = ['A', 'T', 'C', 'G']
    return ''.join(random.choices(bases, k=tamanho))

def complementar(fita):
    complemento = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([complemento[base] for base in fita])

def analisar_genes(fita):
    genes = {
        "AA": "Super Visão",
        "TT": "Alta Resistência",
        "CC": "Memória Avançada",
        "GG": "Velocidade Elevada",
        "AT": "Carisma Elevado",
        "CG": "Pensamento Rápido",
    }
    achados = []
    for gene in genes:
        if gene in fita:
            achados.append(genes[gene])
    return achados

def risco_doenca():
    return random.choice(["Baixo", "Moderado", "Alto", "Nulo"])

tamanho = int(input("🧬 Tamanho da sequência de DNA: "))

fita_original = gerar_dna(tamanho)
fita_complementar = complementar(fita_original)
genes_encontrados = analisar_genes(fita_original)
risco = risco_doenca()

print("\n🔍 Análise Genética Fake")
print("-" * 30)
print(f"🧾 Fita Original:      {fita_original}")
print(f"🧾 Fita Complementar:  {fita_complementar}")
print("\n🧠 Genes dominantes detectados:")
if genes_encontrados:
    for gene in genes_encontrados:
        print(f"✔️ {gene}")
else:
    print("❌ Nenhum gene dominante detectado.")

print(f"\n⚠️ Risco de doença genética: {risco}")
print("-" * 30)
print("🔬 Análise concluída")
