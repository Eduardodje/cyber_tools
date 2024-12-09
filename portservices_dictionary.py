# Dicionário que mapeia números de portas aos serviços correspondentes
port_services = {
    21: "FTP",      # Serviço de transferência de arquivos
    22: "SSH",      # Secure Shell (acesso remoto seguro)
    23: "Telnet",   # Protocolo de acesso remoto inseguro
    25: "SMTP",     # Serviço de envio de emails
    53: "DNS",      # Serviço de tradução de nomes de domínio
    80: "HTTP",     # Protocolo de transferência de hipertexto (web)
    110: "POP3",    # Serviço de recebimento de emails
    143: "IMAP",    # Serviço de recebimento de emails com suporte a pastas
    443: "HTTPS",   # Protocolo seguro de transferência de hipertexto
    3306: "MySQL",  # Banco de dados MySQL
    3389: "RDP",    # Remote Desktop Protocol (Acesso remoto ao Windows)
    5432: "PostgreSQL", # Banco de dados PostgreSQL
    6379: "Redis"   # Banco de dados Redis
}

# Função para verificar os serviços de uma lista de portas
def enumerate_services(ports):
    services = []
    
    # Itera sobre cada porta fornecida
    for port in ports:
        # Verifica se a porta existe no dicionário
        if port in port_services:
            services.append(port_services[port])  # Adiciona o serviço correspondente
        else:
            services.append("Desconhecido")  # Adiciona "Desconhecido" se a porta não existir
    
    return services

# Função principal
def main():
    # Entrada: portas separadas por vírgula
    ports_input = input()
    
    # Converte a string de entrada para uma lista de inteiros (números de portas)
    ports = [int(port) for port in ports_input.split(",")]
    
    # Chama a função de enumeração para obter a lista de serviços
    services = enumerate_services(ports)
    
    # Exibe a lista de serviços
    print(services)

if __name__ == "__main__":
    main()
