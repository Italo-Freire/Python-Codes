import random

def obter_diagnostico(pressao_sistolica, pressao_diastolica):
    
    if 111 <= pressao_sistolica <= 120 and 71<=  pressao_diastolica <= 80:
        return (
            "PA ótima",
            [
                "Mantenha hábitos saudáveis.",
                "Continue praticando exercícios físicos regularmente.",
                "Mantenha uma dieta equilibrada."
            ]
        )
    elif 121 <= pressao_sistolica <= 129 or 80 <=  pressao_diastolica < 85 :
        return (
            "PA normal",
            [
                "Mantenha um estilo de vida saudável.",
                "Evite o consumo excessivo de sal e gorduras.",
                "Pratique exercícios regularmente."
            ]
        )
    elif 130 <= pressao_sistolica <= 139 and 85 <= pressao_diastolica <= 89:
        return (
            "Pré-hipertensão",
            [
                "Reduza o consumo de sal e alimentos industrializados.",
                "Controle o peso corporal.",
                "Pratique atividades físicas regularmente."
            ]
        )
    elif 140 <= pressao_sistolica <= 159 or 90 <= pressao_diastolica <= 99:
        return (
            "HA Estágio 1",
            [
                "Procure acompanhamento médico para avaliação detalhada.",
                "Adote uma dieta com baixo teor de sódio.",
                "Pratique exercícios físicos moderados."
            ]
        )
    elif 160 <= pressao_sistolica <= 179 or 100 <= pressao_diastolica <= 109:
        return (
            "HA Estágio 2",
            [
                "Consulte um médico imediatamente.",
                "Pode ser necessário iniciar medicamentos para controlar a pressão arterial.",
                "Adote mudanças drásticas no estilo de vida, como redução de sal e controle do estresse."
            ]
        )
    elif pressao_sistolica >= 180 or pressao_diastolica >= 110:
        return (
            "HA Estágio 3",
            [
                "Procure atendimento médico de urgência.",
                "Siga rigorosamente as orientações médicas.",
                "Adote uma dieta restrita e evite consumo de álcool e tabaco."
            ]
        )
    else:
        return (
            "Valores irreais",
            ["Verifique se os valores dados estão corretos"]
        )

def gerar_pressao_aleatoria():
    
    while True:
        pressao_sistolica = random.randint(80, 200)  
        pressao_diastolica = random.randint(50, 120)  

       
        if pressao_sistolica > pressao_diastolica:
            return pressao_sistolica, pressao_diastolica

def gerar_paciente_aleatorio():
    
    nomes = ["João", "Maria", "Carlos", "Ana", "Paulo", "Fernanda", "Lucas", "Sofia", "Pedro", "Julia"]
    sobrenomes = ["Silva", "Souza", "Costa", "Oliveira", "Pereira", "Almeida", "Nascimento", "Gomes", "Ribeiro", "Martins"]
    
    nome_completo = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
    idade = random.randint(18, 90)  
    return nome_completo, idade

def simular_medicoes_aleatorias(num_simulacoes=5):
    
    print("\n=== Simulação de Medições de Pressão Arterial para Pacientes Aleatórios ===\n")

    for i in range(1, num_simulacoes + 1):
        
        nome_paciente, idade_paciente = gerar_paciente_aleatorio()

        pressao_sistolica, pressao_diastolica = gerar_pressao_aleatoria()

        print(f"Simulação {i}:")
        print(f"Paciente: {nome_paciente} (Idade: {idade_paciente} anos)")
        print(f"Pressão Sistólica: {pressao_sistolica}, Pressão Diastólica: {pressao_diastolica}")

        
        diagnostico, solucoes = obter_diagnostico(pressao_sistolica, pressao_diastolica)

        # Exibir resultados
        print(f"Diagnóstico: {diagnostico}")
        print("Possíveis soluções:")
        for solucao in solucoes:
            print(f"- {solucao}")
        print("-" * 40)

# Executar a simulação com pacientes e valores aleatórios
simular_medicoes_aleatorias(num_simulacoes=6)
