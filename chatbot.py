def chatbot_especialista():
    print("===================================")
    print(" Chatbot Especialista em Tecnologia")
    print("===================================")
    print("Olá! Eu sou um chatbot especialista em tecnologia.")
    print("Posso responder sobre Python, lógica de programação, GitHub e carreira tech.")
    print("Digite 'sair' para encerrar.\n")

    while True:
        pergunta = input("Você: ").lower()

        if pergunta == "sair":
            print("Chatbot: Obrigado por conversar comigo. Até mais!")
            break

        elif "python" in pergunta:
            print("Chatbot: Python é uma linguagem de programação simples e muito usada em automação, inteligência artificial, análise de dados e desenvolvimento web.")

        elif "lógica" in pergunta or "logica" in pergunta:
            print("Chatbot: Lógica de programação é a base para aprender a programar. Ela ajuda a organizar ideias e criar soluções passo a passo.")

        elif "github" in pergunta:
            print("Chatbot: GitHub é uma plataforma usada para armazenar projetos, controlar versões do código e montar um portfólio profissional.")

        elif "html" in pergunta:
            print("Chatbot: HTML é uma linguagem de marcação usada para estruturar páginas da web.")

        elif "css" in pergunta:
            print("Chatbot: CSS é usado para estilizar páginas web, definindo cores, fontes, tamanhos e layouts.")

        elif "javascript" in pergunta:
            print("Chatbot: JavaScript é uma linguagem usada para deixar sites interativos e dinâmicos.")

        elif "carreira" in pergunta or "tecnologia" in pergunta:
            print("Chatbot: Para começar na área de tecnologia, é importante estudar lógica, praticar programação, criar projetos e publicar no GitHub.")

        elif "inteligência artificial" in pergunta or "ia" in pergunta:
            print("Chatbot: Inteligência Artificial é uma área da tecnologia que busca criar sistemas capazes de aprender, analisar dados e tomar decisões.")

        else:
            print("Chatbot: Ainda não tenho uma resposta específica para isso, mas continue estudando e pesquisando. Esse é o caminho para evoluir na tecnologia.")


chatbot_especialista()
