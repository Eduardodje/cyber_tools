# Função para verificar se o corpo do e-mail contém palavras suspeitas de phishing
def verificar_phishing(mensagem):
    # Lista de palavras que indicam possíveis e-mails de phishing
    palavras_suspeitas = ["ganhe", "prêmio", "urgente", "desconto", "click", "promoção"]
    
    # Converte a mensagem para minúsculas para tornar a busca insensível ao caso
    mensagem = mensagem.lower()
    
    # Verifica se alguma das palavras suspeitas está presente no corpo do e-mail
    for palavra in palavras_suspeitas:
        if palavra in mensagem:
            return "Phishing"  # Se encontrar qualquer palavra suspeita, classifica como "Phishing"
    
    return "Seguro"  # Caso não encontre nenhuma palavra suspeita, classifica como "Seguro"

# Entrada do usuário
email_usuario = input()

# Limpa a entrada, removendo espaços em branco no começo e no final
email_usuario = email_usuario.strip()

# Chama a função de verificação de phishing e armazena o resultado
resultado = verificar_phishing(email_usuario)

# Exibe a classificação
print(f"Classificação: {resultado}")