import numpy as np
from scipy.stats import norm, pareto
import pandas as pd
import matplotlib.pyplot as plt

def menu():
    while True:
        print("Escolha uma opção:")
        print("1. Importar dados de um arquivo")
        print("2. Gerar dados simulados")
        print("3. Gerar duas populações e comparar")
        print("4. Sair")
        
        choice = input("Opção: ")
        
        if choice == '1':
            importar_dados()
        elif choice == '2':
            gerar_dados_simulados()
        elif choice == '3':
            gerar_e_comparar_populacoes()
        elif choice == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def importar_dados():
    arquivo = input("Digite o nome do arquivo (incluindo a extensão): ")
    
    has_headers = input("Os dados possuem cabeçalho? (S/N): ").strip().lower() == 's'
    
    try:
        dados = pd.read_csv(arquivo, header=None if not has_headers else 'infer')
        print("Dados importados com sucesso:")
        print(dados)
        plot_histogram(dados)
    except FileNotFoundError:
        print(f"Arquivo '{arquivo}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao importar o arquivo: {str(e)}")

def gerar_dados_simulados():
    tamanho_amostra = int(input("Digite o tamanho da amostra: "))
    
    while True:
        print("Escolha uma distribuição:")
        print("1. Distribuição Gaussiana (Normal)")
        print("2. Distribuição Pareto")
        print("3. Voltar ao menu principal")
        
        escolha_distribuicao = input("Escolha a distribuição: ")
        
        if escolha_distribuicao == '1':
            gerar_dados_gaussianos(tamanho_amostra)
        elif escolha_distribuicao == '2':
            gerar_dados_pareto(tamanho_amostra)
        elif escolha_distribuicao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

def gerar_dados_gaussianos(tamanho_amostra):
    media = float(input("Digite a média da distribuição Gaussiana: "))
    desvio_padrao = float(input("Digite o desvio padrão da distribuição Gaussiana: "))
    
    dados_gaussianos = np.random.normal(media, desvio_padrao, tamanho_amostra)
    print("Dados gerados com sucesso:")
    print(dados_gaussianos)
    plot_histogram(dados_gaussianos)

def gerar_dados_pareto(tamanho_amostra):
    forma = float(input("Digite o parâmetro de forma da distribuição Pareto: "))
    
    dados_pareto = pareto.rvs(forma, size=tamanho_amostra)
    print("Dados gerados com sucesso:")
    print(dados_pareto)
    plot_histogram(dados_pareto)

def gerar_e_comparar_populacoes():
    tamanho_amostra = int(input("Digite o tamanho da amostra para cada população: "))
    
    while True:
        print("Escolha uma distribuição:")
        print("1. Distribuição Gaussiana (Normal)")
        print("2. Distribuição Pareto")
        print("3. Voltar ao menu principal")
        
        escolha_distribuicao = input("Escolha a distribuição para a primeira população: ")
        
        if escolha_distribuicao == '1':
            pop1 = np.random.normal(float(input("Média para a primeira população: ")), float(input("Desvio padrão para a primeira população: ")), tamanho_amostra)
        elif escolha_distribuicao == '2':
            pop1 = pareto.rvs(float(input("Parâmetro de forma para a primeira população: ")), size=tamanho_amostra)
        elif escolha_distribuicao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue
        
        escolha_distribuicao = input("Escolha a distribuição para a segunda população: ")
        
        if escolha_distribuicao == '1':
            pop2 = np.random.normal(float(input("Média para a segunda população: ")), float(input("Desvio padrão para a segunda população: ")), tamanho_amostra)
        elif escolha_distribuicao == '2':
            pop2 = pareto.rvs(float(input("Parâmetro de forma para a segunda população: ")), size=tamanho_amostra)
        elif escolha_distribuicao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue
        
        comparar_populacoes(pop1, pop2)

def comparar_populacoes(pop1, pop2):
    medians_diff = []
    
    for _ in range(10**4):
        sample1 = np.random.choice(pop1, len(pop1))
        sample2 = np.random.choice(pop2, len(pop2))
        
        median_diff = np.median(sample1) - np.median(sample2)
        medians_diff.append(median_diff)
    
    print("Medianas das diferenças geradas com sucesso.")
    plot_histogram(medians_diff)
    
    while True:
        print("Escolha uma opção:")
        print("1. Calcular o intervalo de maior probabilidade (95%)")
        print("2. Calcular a probabilidade de resultado negativo")
        print("3. Calcular ambos")
        print("4. Voltar ao menu principal")
        
        choice = input("Opção: ")
        
        if choice == '1':
            calculate_highest_probability_range(medians_diff)
        elif choice == '2':
            calculate_negative_probability(medians_diff)
        elif choice == '3':
            calculate_highest_probability_range(medians_diff)
            calculate_negative_probability(medians_diff)
        elif choice == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

def calculate_highest_probability_range(data):
    sorted_data = sorted(data)
    num_samples = len(sorted_data)
    lower_index = int(num_samples * 0.025)
    upper_index = int(num_samples * 0.975)
    
    range_start = sorted_data[lower_index]
    range_end = sorted_data[upper_index]
    
    print(f"Intervalo de maior probabilidade (95%): [{range_start}, {range_end}]")

def calculate_negative_probability(data):
    negative_prob = np.mean(np.array(data) < 0)
    
    print(f"Probabilidade de resultado negativo: {negative_prob * 100}%")

def plot_histogram(data):
    density = input("Plotar histograma com densidade? (S/N): ").strip().lower() == 's'
    
    plt.hist(data, bins=20, density=density)
    
    if density:
        plt.ylabel('Densidade')
    else:
        plt.ylabel('Frequência')
    
    plt.xlabel('Valores')
    plt.title('Histograma')
    plt.show()

if __name__ == "__main__":
    menu()
