# Calculadora de Consumo Elétrico Inteligente

print("--- Calculadora de Consumo Elétrico ---")
print()

# Entrada de dados
nome_aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em Watts: "))
horas_dia = float(input("Digite o tempo médio de uso diário, em horas: "))

# Cálculo do consumo mensal em kWh
consumo_mensal_kwh = (potencia * horas_dia * 30) / 1000

# Cálculo do custo estimado (R$ 0,75 por kWh)
custo_mensal = consumo_mensal_kwh * 0.75

# Exibição dos resultados formatados
print()
print("--- RESULTADO ----")
print(f"Aparelho: {nome_aparelho}")
print(f"Consumo estimado: {consumo_mensal_kwh:.1f} kWh/mês")
print(f"Custo estimado: R$ {custo_mensal:.2f}/mês")
print()
