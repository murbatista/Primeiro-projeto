

# ============================================================
# MEMBRO DO CORPO
# ============================================================

def divisor_de_treino():
    while True:
        print("\n=== Encontre o seu treino ===")
        print("1 - INFERIORES")
        print("2 - SUPERIORES")
        print("0 - Voltar")

        opcao = input("Digite uma opção: ").strip()
        
        if opcao == "1":
            buscar_inferiores()
        elif opcao == "2":
            buscar_superiores()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


# ============================================================
# MÚSCULOS INFERIORES
# ============================================================

def buscar_inferiores():
    while True:
        print("\n=== Treinos ===")
        print("1 - Panturrilha")
        print("2 - Posterior")
        print("3 - Quadríceps")
        print("0 - Voltar")
        
        opcao = input("Digite uma opção: ").strip()
        
        if opcao == "1":
            buscar_panturrilha()
        elif opcao == "2":
            buscar_posterior()
        elif opcao == "3":
            buscar_quadriceps()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


# ============================================================
# MÚSCULOS SUPERIOES
# ============================================================

def buscar_superiores():
    while True:
        print("\n=== Treinos ===")
        print("1 - Trapézio")
        print("2 - Ombro")
        print("3 - Tríceps")
        print("4 - Bíceps")
        print("5 - Peito")
        print("6 - Costas")
        print("0 - Voltar")

        opcao = input("Digite uma opção: ")
        
        if opcao == "1":
            buscar_trapezio()
        elif opcao == "2":
            buscar_ombro()
        elif opcao == "3":
            buscar_triceps()
        elif opcao == "4":
            buscar_biceps()
        elif opcao == "5":
            buscar_peito()
        elif opcao == "6":
            buscar_costas()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


# ============================================================
# EXERCíCIOS INFERIOES
# ============================================================

def buscar_panturrilha():
    while True:
        print("\n=== Exercícios ===")
        print("1 - Elevação de panturrilha em pé")
        print("2 - Elevação de panturrilha sentado")
        print("0 - Voltar")

        opcao = input("Digite uma opção: ").strip()
        
        if opcao == "1":
            exercicio_elevação_de_panturrilha_em_pe()
        elif opcao == "2":
            exercicio_elevação_de_panturrilha_sentado()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def buscar_posterior():
    while True:
        print("\n=== Exercícios ===")
        print("1 - Mesa flexora")
        print("2 - Stiff")
        print("3 - Flexora sentada")
        print("0 - Voltar")

        opcao = input("Digite uma opção: ").strip()
        
        if opcao == "1":
            exercicio_mesa_flexora()
        elif opcao == "2":
            exercicio_stiff()
        elif opcao == "3":
            exercicio_flexora_sentada()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def buscar_quadriceps():
    while True:
        print("\n=== Exercícios ===")
        print("1 - Agachamento livre")
        print("2 - Leg press 45°")
        print("3 - Cadeira extensora")
        print("0 - Voltar")

        opcao = input("Digite uma opção: ")
        
        if opcao == "1":
            exercicio_agachamento_livre()
        elif opcao == "2":
            exercicio_leg_press_45()
        elif opcao == "3":
            exercicio_cadeira_extensora()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


# ============================================================
# EXERÍCIOS SUPERIOES
# ============================================================

def buscar_trapezio():
    while True:
        print("\n=== Exercícios ===")
        print("1 - Encolhimento com barra ou halteres")
        print("2 - Remada alta no cabo")
        print("0 - Voltar")

        opcao = input("Digite uma opção: ").strip()
        
        if opcao == "1":
            exercicio_encolhimento_com_barra_ou_halteres()
        elif opcao == "2":
            exercicio_remada_alta_no_cabo()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def buscar_ombro():
    while True:
        print("\n=== Exercícios ===")
        print("1 - Desenvolvimento com halteres")
        print("2 - Elevação lateral")
        print("3 - Crucifixo inverso")
        print("0 - Voltar")

        opcao = input("Digite uma opção: ").strip()
        
        if opcao == "1":
            exercicio_desenvolvimento_com_halteres()
        elif opcao == "2":
            exercicio_elevação_lateral()
        elif opcao == "3":
            exercicio_crucifixo_inverso()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def buscar_triceps():
    while True:
        print("\n=== Exercícios ===")
        print("1 - Tríceps testa")
        print("2 - Tríceps na polia com corda")
        print("3 - Tríceps na polia com barra")
        print("0 - Voltar")

        opcao = input("Digite uma opção: ").strip()
        
        if opcao == "1":
            exercicio_triceps_testa()
        elif opcao == "2":
            exercicio_triceps_na_polia_com_corda()
        elif opcao == "3":
            exercicio_triceps_na_polia_com_barra()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def buscar_biceps():
    while True:
        print("\n=== Exercícios ===")
        print("1 - Rosca direta com barra")
        print("2 - Rosca inclinada com halteres")
        print("3 - Rosca martelo")
        print("0 - Voltar")

        opcao = input("Digite uma opção: ").strip()
        
        if opcao == "1":
            exercicio_rosca_direta_com_barra()
        elif opcao == "2":
            exercicio_rosca_inclinada_com_halteres()
        elif opcao == "3":
            exercicio_rosca_martelo()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def buscar_peito():
    while True:
        print("\n=== Exercícios ===")
        print("1 - Supino reto com barra")
        print("2 - Supino inclinado com halteres")
        print("3 - Crucifixo na máquina")
        print("0 - Voltar")

        opcao = input("Digite uma opção: ").strip()
        
        if opcao == "1":
            exercicio_supino_reto_com_barra()
        elif opcao == "2":
            exercicio_supino_inclinado_com_halteres()
        elif opcao == "3":
            exercicio_crucifixo_na_maquina()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def buscar_costas():
    while True:
        print("\n=== Exercícios ===")
        print("1 - Puxada alta")
        print("2 - Remada curvada com barra")
        print("3 - Remada baixa na polia")
        print("0 - Voltar")

        opcao = input("Digite uma opção: ").strip()
        
        if opcao == "1":
            exercicio_puxada_alta()
        elif opcao == "2":
            exercicio_remada_curvada_com_barra()
        elif opcao == "3":
            exercicio_remada_baixa_na_polia()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


# ============================================================
# EXERCÍCIO DETALHADO
# ============================================================

def exercicio_elevação_de_panturrilha_em_pe():
    print("\n")
    
    treino = {
"nome": "Elevação de Panturrilha em Pé",
"tipo": "força",
"músculo": "panturrilha",
"dificuldade": "iniciante",
"instruções": "Fique em pé com os pés afastados aproximadamente na largura dos ombros. Mantenha o tronco ereto e segure os halteres ao lado do corpo, se estiver utilizando carga. Esta será sua posição inicial. Inicie o movimento elevando os calcanhares o máximo possível, ficando apoiado sobre as pontas dos pés. Faça uma breve pausa no topo do movimento e, em seguida, abaixe os calcanhares lentamente até a posição inicial.",
"equipamentos": "nenhum ou halteres",
"Informações de segurança": "Mantenha o tronco estável durante todo o movimento e evite balançar o corpo. Execute a subida e a descida de forma controlada, utilizando uma amplitude confortável. Use uma carga adequada ao seu nível e mantenha os pés firmemente apoiados."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_elevação_de_panturrilha_sentado():
    print("\n")
    
    treino = {
"nome": "Elevação de Panturrilha Sentado",
"tipo": "força",
"músculo": "panturrilha",
"dificuldade": "iniciante",
"instruções": "Sente-se em um banco ou máquina apropriada, mantendo os pés firmemente apoiados no chão ou na plataforma e os joelhos flexionados. Posicione a carga sobre as coxas, próxima aos joelhos, quando utilizar um equipamento específico. Esta será sua posição inicial. Inicie o movimento elevando os calcanhares o máximo possível, mantendo as pontas dos pés apoiadas. Faça uma breve pausa no topo e, em seguida, abaixe os calcanhares lentamente até a posição inicial.",
"equipamentos": "máquina de panturrilha sentada ou halter",
"Informações de segurança": "Mantenha as costas apoiadas e o tronco estável durante o movimento. Evite utilizar impulso ou realizar movimentos bruscos. Controle tanto a subida quanto a descida e utilize uma carga adequada ao seu nível. Não force a amplitude caso sinta desconforto nos tornozelos ou joelhos."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_mesa_flexora():
    print("\n")
    
    treino = {
"nome": "Mesa Flexora",
"tipo": "força",
"músculo": "posterior de coxa",
"dificuldade": "iniciante",
"instruções": "Deite-se de bruços na mesa flexora, mantendo o quadril e o tronco firmemente apoiados no banco. Posicione a parte posterior dos tornozelos sob o apoio acolchoado e segure as alças laterais. Esta será sua posição inicial. Inicie o movimento flexionando os joelhos e levando os calcanhares em direção aos glúteos. Contraia o posterior de coxa no topo do movimento e faça uma breve pausa. Em seguida, abaixe a carga lentamente até retornar à posição inicial.",
"equipamentos": "mesa flexora",
"Informações de segurança": "Mantenha o quadril e o tronco apoiados durante todo o exercício. Evite levantar o quadril ou utilizar impulso para movimentar a carga. Execute o movimento de forma controlada e utilize uma carga adequada ao seu nível. Evite realizar a extensão completa dos joelhos de forma brusca."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_stiff():
    print("\n")
    
    treino = {
"nome": "Stiff",
"tipo": "força",
"músculo": "posterior de coxa",
"dificuldade": "intermediário",
"instruções": "Fique em pé com os pés afastados aproximadamente na largura dos quadris, segurando uma barra ou halteres à frente das coxas. Mantenha os joelhos levemente flexionados, o peito aberto e a coluna em posição neutra. Esta será sua posição inicial. Inicie o movimento levando o quadril para trás enquanto abaixa a carga próxima às pernas. Desça até sentir um alongamento confortável no posterior de coxa, mantendo as costas estáveis. Em seguida, empurre o quadril para frente e retorne à posição inicial, contraindo os músculos posteriores.",
"equipamentos": "barra ou halteres",
"Informações de segurança": "Mantenha a coluna neutra durante todo o movimento e evite arredondar as costas. Mantenha a carga próxima ao corpo e não desça além do ponto em que consegue preservar a postura correta. Utilize uma carga adequada ao seu nível e execute o movimento de forma lenta e controlada."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_flexora_sentada():
    print("\n")
    
    treino = {
"nome": "Flexora Sentada",
"tipo": "força",
"músculo": "posterior de coxa",
"dificuldade": "iniciante",
"instruções": "Sente-se na máquina flexora com as costas firmemente apoiadas no encosto. Ajuste o banco e o apoio das pernas de modo que os joelhos fiquem alinhados com o eixo de rotação da máquina. Posicione as pernas sob o apoio acolchoado e mantenha as coxas firmemente apoiadas. Esta será sua posição inicial. Inicie o movimento flexionando os joelhos e levando os calcanhares para baixo e para trás. Contraia o posterior de coxa no final do movimento e faça uma breve pausa. Em seguida, retorne lentamente à posição inicial.",
"equipamentos": "máquina flexora sentada",
"Informações de segurança": "Mantenha as costas e as coxas firmemente apoiadas durante todo o exercício. Evite utilizar impulso ou realizar movimentos bruscos. Controle a carga durante a subida e a descida e utilize um peso adequado ao seu nível. Ajuste corretamente o equipamento antes de iniciar o exercício."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_agachamento_livre():
    print("\n")
    
    treino = {
"nome": "Agachamento Livre",
"tipo": "força",
"músculo": "quadríceps",
"dificuldade": "intermediário",
"instruções": "Fique em pé com os pés aproximadamente na largura dos ombros, mantendo a barra apoiada de forma confortável sobre a parte superior das costas. Retire a barra do suporte e posicione-se com o tronco estável e o abdômen contraído. Esta será sua posição inicial. Inicie o movimento flexionando os joelhos e levando o quadril para trás e para baixo, mantendo os pés firmemente apoiados no chão. Desça até uma amplitude confortável, mantendo a coluna em posição neutra. Em seguida, empurre o chão com os pés e estenda os joelhos e o quadril para retornar à posição inicial.",
"equipamentos": "barra e suporte para agachamento",
"Informações de segurança": "Mantenha a coluna neutra e o abdômen contraído durante todo o movimento. Mantenha os joelhos alinhados com a direção dos pés e evite deixá-los colapsarem para dentro. Utilize uma carga adequada ao seu nível e, ao usar cargas elevadas, tenha um suporte adequado e, de preferência, um observador. Não aumente a carga às custas da técnica."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_leg_press_45():
    print("\n")
    
    treino = {
"nome": "Leg Press 45°",
"tipo": "força",
"músculo": "quadríceps",
"dificuldade": "iniciante",
"instruções": "Sente-se no leg press 45° com as costas e o quadril firmemente apoiados no encosto. Posicione os pés na plataforma aproximadamente na largura dos ombros. Destrave o equipamento e mantenha as pernas estendidas sem travar completamente os joelhos. Esta será sua posição inicial. Inicie o movimento flexionando os joelhos e controlando a descida da plataforma em direção ao corpo, mantendo os pés firmemente apoiados. Desça até uma amplitude confortável e, em seguida, empurre a plataforma para retornar à posição inicial.",
"equipamentos": "leg press 45°",
"Informações de segurança": "Mantenha as costas e o quadril firmemente apoiados no encosto durante todo o movimento. Não permita que os joelhos colapsem para dentro e evite travá-los de forma brusca na subida. Utilize uma carga adequada ao seu nível e controle a descida. Não desça além do ponto em que consegue manter a postura correta."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_cadeira_extensora():
    print("\n")
    
    treino = {
"nome": "Cadeira Extensora",
"tipo": "força",
"músculo": "quadríceps",
"dificuldade": "iniciante",
"instruções": "Sente-se na cadeira extensora com as costas firmemente apoiadas no encosto. Ajuste o banco e o apoio acolchoado de forma que o eixo de rotação da máquina fique alinhado com os joelhos. Posicione a parte da frente dos tornozelos sob o apoio e segure as alças laterais. Esta será sua posição inicial. Inicie o movimento estendendo os joelhos e elevando o apoio até que as pernas estejam estendidas de forma confortável. Faça uma breve pausa no topo, contraindo o quadríceps, e depois abaixe a carga lentamente até a posição inicial.",
"equipamentos": "cadeira extensora",
"Informações de segurança": "Mantenha as costas e o quadril firmemente apoiados no encosto durante todo o exercício. Evite utilizar impulso ou realizar movimentos bruscos. Controle a subida e a descida e utilize uma carga adequada ao seu nível. Não trave os joelhos de forma brusca no final do movimento."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_encolhimento_com_barra_ou_halteres():
    print("\n")
    
    treino = {
"nome": "Encolhimento com Barra ou Halteres",
"tipo": "força",
"músculo": "trapézio",
"dificuldade": "iniciante",
"instruções": "Fique em pé com os pés aproximadamente na largura dos ombros, segurando uma barra à frente do corpo ou um halter em cada mão ao lado do corpo. Mantenha os braços estendidos e o tronco ereto. Esta será sua posição inicial. Inicie o movimento elevando os ombros em direção às orelhas, mantendo os braços imóveis. Contraia o trapézio no ponto mais alto e faça uma breve pausa. Em seguida, abaixe os ombros lentamente até retornar à posição inicial.",
"equipamentos": "barra ou halteres",
"Informações de segurança": "Mantenha a coluna neutra e o tronco estável durante todo o movimento. Evite girar os ombros ou utilizar impulso para levantar a carga. Realize o movimento de forma controlada e utilize um peso adequado ao seu nível. Não incline excessivamente a cabeça ou o tronco durante a execução."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_remada_alta_no_cabo():
    print("\n")
    
    treino = {
"nome": "Remada Alta no Cabo",
"tipo": "força",
"músculo": "trapézio",
"dificuldade": "intermediário",
"instruções": "Fique em pé de frente para a polia baixa, segurando a barra ou o acessório com as duas mãos e os braços estendidos à frente do corpo. Mantenha os pés afastados aproximadamente na largura dos ombros e o tronco ereto. Esta será sua posição inicial. Inicie o movimento puxando o acessório para cima, conduzindo os cotovelos para cima e para os lados. Eleve a carga até uma altura confortável, mantendo os cotovelos controlados. Faça uma breve pausa no topo e retorne lentamente à posição inicial.",
"equipamentos": "cabo e barra reta ou corda",
"Informações de segurança": "Mantenha o tronco estável e evite utilizar impulso para movimentar a carga. Não eleve os cotovelos além de uma amplitude confortável, especialmente se sentir desconforto nos ombros. Execute o movimento de forma controlada e utilize uma carga adequada ao seu nível."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_desenvolvimento_com_halteres():
    print("\n")
    
    treino = {
"nome": "Desenvolvimento com Halteres",
"tipo": "força",
"músculo": "ombros",
"dificuldade": "intermediário",
"instruções": "Sente-se em um banco com encosto, mantendo os pés firmemente apoiados no chão. Segure um halter em cada mão e posicione-os ao lado dos ombros, com os cotovelos flexionados. Mantenha o tronco ereto e o abdômen contraído. Esta será sua posição inicial. Inicie o movimento empurrando os halteres para cima, estendendo os cotovelos de forma controlada. Ao chegar próximo da extensão completa, faça uma breve pausa e, em seguida, abaixe os halteres lentamente até a posição inicial.",
"equipamentos": "halteres e banco com encosto",
"Informações de segurança": "Mantenha as costas apoiadas no encosto e evite arquear excessivamente a lombar. Não utilize impulso para levantar os halteres e mantenha os movimentos controlados. Utilize uma carga adequada ao seu nível e evite travar os cotovelos de forma brusca no topo do movimento."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_elevação_lateral():
    print("\n")
    
    treino = {
"nome": "Elevação Lateral",
"tipo": "força",
"músculo": "ombros",
"dificuldade": "iniciante",
"instruções": "Fique em pé com os pés aproximadamente na largura dos ombros, segurando um halter em cada mão ao lado do corpo. Mantenha os braços levemente flexionados, o tronco ereto e o abdômen contraído. Esta será sua posição inicial. Inicie o movimento elevando os braços para os lados até aproximadamente a altura dos ombros, mantendo os cotovelos levemente flexionados. Faça uma breve pausa no ponto mais alto e, em seguida, abaixe os halteres lentamente até a posição inicial.",
"equipamentos": "halteres",
"Informações de segurança": "Mantenha o tronco estável e evite balançar o corpo para levantar os pesos. Não utilize cargas excessivas que prejudiquem a execução. Realize o movimento de forma lenta e controlada e evite elevar os braços muito acima da linha dos ombros caso isso cause desconforto."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_crucifixo_inverso():
    print("\n")
    
    treino = {
"nome": "Crucifixo Inverso",
"tipo": "força",
"músculo": "ombros",
"dificuldade": "iniciante",
"instruções": "Sente-se na ponta de um banco ou fique em pé com o tronco inclinado à frente, mantendo a coluna em posição neutra. Segure um halter em cada mão com os braços estendidos em direção ao chão. Esta será sua posição inicial. Inicie o movimento elevando os braços para os lados, aproximando as escápulas e mantendo os cotovelos levemente flexionados. Eleve os halteres até aproximadamente a altura dos ombros, faça uma breve pausa e retorne lentamente à posição inicial.",
"equipamentos": "halteres e banco",
"Informações de segurança": "Mantenha a coluna neutra e evite arredondar excessivamente as costas. Não utilize impulso para elevar os halteres e mantenha o movimento controlado. Utilize uma carga adequada ao seu nível e evite elevar os braços além de uma amplitude confortável."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_triceps_testa():
    print("\n")
    
    treino = {
"nome": "Tríceps Testa",
"tipo": "força",
"músculo": "tríceps",
"dificuldade": "intermediário",
"instruções": "Deite-se em um banco reto segurando uma barra ou halteres acima do peito, com os braços estendidos e os cotovelos apontando para cima. Esta será sua posição inicial. Inicie o movimento flexionando os cotovelos e abaixando a carga de forma controlada em direção à testa ou ligeiramente atrás da cabeça. Faça uma breve pausa e, em seguida, estenda os cotovelos para retornar à posição inicial, mantendo os braços superiores relativamente imóveis.",
"equipamentos": "barra ou halteres e banco reto",
"Informações de segurança": "Mantenha os cotovelos apontados para cima e evite abri-los excessivamente para os lados. Utilize uma carga adequada ao seu nível e controle a descida para evitar que a carga caia em direção à cabeça. Evite movimentos bruscos e não trave os cotovelos de forma agressiva no final da extensão."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_triceps_na_polia_com_corda():
    print("\n")
    
    treino = {
"nome": "Tríceps na Polia com Corda",
"tipo": "força",
"músculo": "tríceps",
"dificuldade": "iniciante",
"instruções": "Fique em pé de frente para a polia alta, segurando as extremidades da corda com as duas mãos. Mantenha os cotovelos próximos ao corpo, os braços superiores imóveis e o tronco ereto. Esta será sua posição inicial. Inicie o movimento empurrando a corda para baixo, estendendo os cotovelos até que os braços estejam quase completamente estendidos. Faça uma breve pausa na parte inferior e retorne lentamente à posição inicial, controlando a subida da carga.",
"equipamentos": "polia e corda",
"Informações de segurança": "Mantenha os cotovelos próximos ao corpo e evite utilizar o peso do corpo para movimentar a carga. Execute o movimento de forma controlada, sem balançar o tronco. Utilize uma carga adequada ao seu nível e evite travar os cotovelos de forma brusca na extensão."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_triceps_na_polia_com_barra():
    print("\n")
    
    treino = {
"nome": "Tríceps na Polia com Barra",
"tipo": "força",
"músculo": "tríceps",
"dificuldade": "iniciante",
"instruções": "Fique em pé de frente para a polia alta, segurando a barra com as duas mãos e os braços flexionados. Mantenha os cotovelos próximos ao corpo, os braços superiores imóveis e o tronco ereto. Esta será sua posição inicial. Inicie o movimento empurrando a barra para baixo até estender os cotovelos de forma controlada. Faça uma breve pausa na parte inferior e, em seguida, retorne lentamente à posição inicial, mantendo a tensão no tríceps.",
"equipamentos": "polia e barra reta",
"Informações de segurança": "Mantenha os cotovelos próximos ao corpo durante todo o movimento e evite inclinar excessivamente o tronco para utilizar impulso. Controle a subida e a descida da carga e utilize um peso adequado ao seu nível. Evite travar os cotovelos de forma brusca no final do movimento."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_rosca_direta_com_barra():
    print("\n")
    
    treino = {
"nome": "Rosca Direta com Barra",
"tipo": "força",
"músculo": "bíceps",
"dificuldade": "iniciante",
"instruções": "Fique em pé com os pés aproximadamente na largura dos ombros, segurando uma barra com as palmas das mãos voltadas para cima. Mantenha os braços estendidos ao lado do corpo, os cotovelos próximos ao tronco e a coluna neutra. Esta será sua posição inicial. Inicie o movimento flexionando os cotovelos e levando a barra em direção ao peito, mantendo os braços superiores imóveis. Contraia o bíceps no topo do movimento e faça uma breve pausa. Em seguida, abaixe a barra lentamente até retornar à posição inicial.",
"equipamentos": "barra",
"Informações de segurança": "Mantenha os cotovelos próximos ao corpo e evite balançar o tronco para levantar a carga. Execute o movimento de forma controlada, principalmente na descida. Utilize um peso adequado ao seu nível e evite estender ou travar os cotovelos de forma brusca."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_rosca_inclinada_com_halteres():
    print("\n")
    
    treino = {
"nome": "Rosca Inclinada com Halteres",
"tipo": "força",
"músculo": "bíceps",
"dificuldade": "intermediário",
"instruções": "Sente-se em um banco inclinado com um halter em cada mão, mantendo as costas e a cabeça apoiadas no encosto. Deixe os braços estendidos para baixo ao lado do corpo, com as palmas das mãos voltadas para frente. Esta será sua posição inicial. Inicie o movimento flexionando os cotovelos e levando os halteres em direção aos ombros, mantendo os braços superiores imóveis. Contraia o bíceps no topo do movimento e faça uma breve pausa. Em seguida, abaixe os halteres lentamente até retornar à posição inicial.",
"equipamentos": "halteres e banco inclinado",
"Informações de segurança": "Mantenha as costas firmemente apoiadas no banco e evite utilizar impulso para levantar os halteres. Controle especialmente a descida e utilize uma carga adequada ao seu nível. Mantenha os cotovelos estáveis e evite realizar movimentos bruscos."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_rosca_martelo():
    print("\n")
    
    treino = {
"nome": "Rosca Martelo",
"tipo": "força",
"músculo": "bíceps",
"dificuldade": "iniciante",
"instruções": "Fique em pé com os pés aproximadamente na largura dos ombros, segurando um halter em cada mão com as palmas voltadas uma para a outra. Mantenha os braços estendidos ao lado do corpo, os cotovelos próximos ao tronco e a coluna neutra. Esta será sua posição inicial. Inicie o movimento flexionando os cotovelos e levando os halteres em direção aos ombros, mantendo a pegada neutra e os braços superiores imóveis. Faça uma breve pausa no topo e, em seguida, abaixe os halteres lentamente até retornar à posição inicial.",
"equipamentos": "halteres",
"Informações de segurança": "Mantenha os cotovelos próximos ao corpo e evite balançar o tronco para movimentar os pesos. Execute a subida e a descida de forma controlada e utilize uma carga adequada ao seu nível. Evite movimentos bruscos e não force a extensão dos cotovelos."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_supino_reto_com_barra():
    print("\n")
    
    treino = {
"nome": "Supino Reto com Barra",
"tipo": "força",
"músculo": "peito",
"dificuldade": "intermediário",
"instruções": "Deite-se em um banco reto com os pés firmemente apoiados no chão. Segure a barra com as mãos um pouco mais afastadas que a largura dos ombros e mantenha as escápulas retraídas contra o banco. Retire a barra do suporte e posicione-a acima do peito, com os braços estendidos. Esta será sua posição inicial. Desça a barra lentamente em direção à parte média do peito, mantendo os cotovelos em uma posição confortável. Toque ou aproxime a barra do peito de forma controlada e, em seguida, empurre a barra para cima até retornar à posição inicial.",
"equipamentos": "barra, anilhas e banco reto",
"Informações de segurança": "Mantenha os pés firmemente apoiados no chão e as escápulas estáveis contra o banco. Utilize uma carga adequada ao seu nível e evite realizar o exercício sem suporte de segurança quando estiver usando cargas elevadas. Mantenha o controle da barra durante todo o movimento e, de preferência, utilize um observador para séries próximas da falha."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_supino_inclinado_com_halteres():
    print("\n")
    
    treino = {
"nome": "Supino Inclinado com Halteres",
"tipo": "força",
"músculo": "peito",
"dificuldade": "intermediário",
"instruções": "Ajuste o banco em uma inclinação moderada e sente-se segurando um halter em cada mão. Deite-se no banco com as costas e a cabeça apoiadas e mantenha os pés firmemente apoiados no chão. Posicione os halteres ao lado do peito, com os cotovelos flexionados. Esta será sua posição inicial. Empurre os halteres para cima, estendendo os braços de forma controlada sem bater os pesos entre si. Faça uma breve pausa no topo e, em seguida, abaixe os halteres lentamente até retornar à posição inicial.",
"equipamentos": "halteres e banco inclinado",
"Informações de segurança": "Mantenha as costas e a cabeça apoiadas no banco durante todo o exercício. Evite utilizar impulso ou deixar os halteres descerem de forma descontrolada. Utilize uma carga adequada ao seu nível e mantenha os cotovelos em uma posição confortável durante o movimento. Ao utilizar cargas elevadas, tenha cuidado ao posicionar e retirar os halteres."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_crucifixo_na_maquina():
    print("\n")
    
    treino = {
"nome": "Crucifixo na Máquina",
"tipo": "força",
"músculo": "peito",
"dificuldade": "iniciante",
"instruções": "Sente-se na máquina de crucifixo com as costas firmemente apoiadas no encosto. Ajuste o banco de modo que os braços ou pegadores fiquem aproximadamente na altura do peito. Segure os pegadores e mantenha os cotovelos levemente flexionados. Esta será sua posição inicial. Inicie o movimento aproximando os braços à frente do corpo, contraindo o peito até que os pegadores se aproximem. Faça uma breve pausa na contração e, em seguida, retorne lentamente à posição inicial, permitindo que o peito seja alongado de forma controlada.",
"equipamentos": "máquina de crucifixo (peck deck)",
"Informações de segurança": "Mantenha as costas apoiadas no encosto e evite utilizar impulso durante o movimento. Não permita que os pesos batam ao retornar à posição inicial. Utilize uma carga adequada ao seu nível e mantenha os cotovelos levemente flexionados durante toda a execução. Evite uma amplitude que cause desconforto nos ombros."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_puxada_alta():
    print("\n")
    
    treino = {
"nome": "Puxada Alta",
"tipo": "força",
"músculo": "costas",
"dificuldade": "iniciante",
"instruções": "Sente-se na máquina de puxada alta e ajuste o apoio das coxas para manter o corpo firme. Segure a barra com as mãos um pouco mais afastadas que a largura dos ombros, com as palmas voltadas para frente. Mantenha o tronco ereto e os braços estendidos. Esta será sua posição inicial. Inicie o movimento puxando a barra em direção à parte superior do peito, conduzindo os cotovelos para baixo e para trás. Faça uma breve pausa na parte inferior e, em seguida, retorne lentamente a barra à posição inicial, controlando a subida.",
"equipamentos": "máquina de puxada alta e barra",
"Informações de segurança": "Mantenha o tronco estável e evite inclinar excessivamente o corpo para trás durante a puxada. Não utilize impulso para movimentar a carga e mantenha o controle durante a subida. Evite puxar a barra atrás da cabeça. Utilize uma carga adequada ao seu nível e mantenha os movimentos controlados."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_remada_curvada_com_barra():
    print("\n")
    
    treino = {
"nome": "Remada Curvada com Barra",
"tipo": "força",
"músculo": "costas",
"dificuldade": "intermediário",
"instruções": "Fique em pé com os pés aproximadamente na largura dos ombros, segurando a barra com as mãos um pouco mais afastadas que a largura dos ombros. Flexione levemente os joelhos e incline o tronco à frente, levando o quadril para trás e mantendo a coluna em posição neutra. Esta será sua posição inicial. Inicie o movimento puxando a barra em direção à parte inferior do abdômen, conduzindo os cotovelos para trás e mantendo-os próximos ao corpo. Faça uma breve pausa no topo e, em seguida, abaixe a barra lentamente até retornar à posição inicial.",
"equipamentos": "barra e anilhas",
"Informações de segurança": "Mantenha a coluna neutra e o abdômen contraído durante todo o exercício. Evite arredondar as costas ou utilizar impulso para levantar a carga. Mantenha os joelhos levemente flexionados e o movimento controlado. Utilize uma carga adequada ao seu nível e interrompa o exercício caso sinta dor, especialmente na região lombar."
}
    for index, price in treino.items():
        print(index, ":", price)


def exercicio_remada_baixa_na_polia():
    print("\n")
    
    treino = {
"nome": "Remada Baixa na Polia",
"tipo": "força",
"músculo": "costas",
"dificuldade": "iniciante",
"instruções": "Sente-se em frente à polia baixa com os pés firmemente apoiados na plataforma e os joelhos levemente flexionados. Segure o acessório com as duas mãos e mantenha o tronco ereto. Esta será sua posição inicial. Inicie o movimento puxando o acessório em direção ao abdômen, conduzindo os cotovelos para trás e aproximando as escápulas. Faça uma breve pausa quando as mãos estiverem próximas ao corpo e, em seguida, estenda os braços lentamente, permitindo que as escápulas se afastem de forma controlada até retornar à posição inicial.",
"equipamentos": "polia baixa e triângulo ou barra",
"Informações de segurança": "Mantenha a coluna neutra e evite balançar o tronco para movimentar a carga. Não arredonde excessivamente as costas durante a fase de retorno. Utilize uma carga adequada ao seu nível e mantenha o movimento controlado durante toda a execução."
}
    for index, price in treino.items():
        print(index, ":", price)


# ============================================================
# FEEDBACK E RELATÓRIO DE BUGS
# ============================================================

from datetime import datetime


def salvar_feedback():
    print("\n=== Enviar feedback ===")
    
    feedback = input("Digite seu feedback: ").strip()

    if feedback == "":
        print("O feedback não pode ficar vazio.")
        return

    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open("feedbacks.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{data}] {feedback}\n")

    print("Feedback salvo com sucesso!")


def relatar_bug():
    print("\n=== Relatar bug ===")
    
    bug = input("Descreva o bug encontrado: ").strip()

    if bug == "":
        print("O relato do bug não pode ficar vazio.")
        return

    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open("bugs.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{data}] {bug}\n")

    print("Bug salvo com sucesso!")


def visualizar_feedbacks():
    print("\n=== Feedbacks salvos ===")

    try:
        with open("feedbacks.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()

        if conteudo.strip():
            print(conteudo)
        else:
            print("Ainda não existem feedbacks.")
    except FileNotFoundError:
        print("Ainda não existem feedbacks.")


def visualizar_bugs():
    print("\n=== Bugs salvos ===")

    try:
        with open("bugs.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()

        if conteudo.strip():
            print(conteudo)
        else:
            print("Ainda não existem bugs relatados.")
    except FileNotFoundError:
        print("Ainda não existem bugs relatados.")


# ============================================================
# MENU DO ADMINISTRADOR
# ============================================================

def menu_administrador():
    senha_correta = "1234"
    
    print("\n=== ÁREA DO ADMINISTRADOR ===")
    
    senha = input("Digite a senha: ")
    
    if senha != senha_correta:
        print("Senha incorreta!")
        return
    
    while True:
        print("\n=== MENU ADMINISTRADOR ===")
        print("1 - Ver feedbacks")
        print("2 - Ver bugs relatados")
        print("3 - Limpar feedbacks")
        print("4 - Limpar bugs")
        print("0 - Voltar")
        
        opcao = input("Digite uma opção: ").strip()
        
        if opcao == "1":
            visualizar_feedbacks()
        elif opcao == "2":
            visualizar_bugs()
        elif opcao == "3":
            limpar_feedbacks()
        elif opcao == "4":
            limpar_bugs()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def limpar_feedbacks():
    confirmacao = input("Tem certeza que deseja apagar todos os feedbacks? (s/n): ").strip().lower()
    
    if confirmacao == "s":
        with open("feedbacks.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("")
        print("Feedbacks apagados com sucesso!")
    else:
        print("Operação cancelada.")


def limpar_bugs():
    confirmacao = input("Tem certeza que deseja apagar todos os bugs? (s/n): ").strip().lower()
    
    if confirmacao == "s":
        with open("bugs.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("")
        print("Bugs apagados com sucesso!")
    else:
        print("Operação cancelada.")


# ============================================================
# MENU PRINCIPAL
# ============================================================

def menu_principal():
    while True:
        print("\n================================")
        print("       PROJETO ACADEMIA")
        print("================================")
        print("1 - Encontrar treino")
        print("2 - Enviar feedback")
        print("3 - Relatar bug")
        print("4 - Área do administrador")
        print("0 - Sair")

        opcao = input("Digite uma opção: ").strip()

        if opcao == "1":
            divisor_de_treino()
        elif opcao == "2":
            salvar_feedback()
        elif opcao == "3":
            relatar_bug()
        elif opcao == "4":
            menu_administrador()
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_principal()
