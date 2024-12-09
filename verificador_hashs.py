def verificar_hashes(lista_hashes):
  
    for hash_comparacao in lista_hashes:
        
        hash_calculado, hash_esperado = hash_comparacao.split(",")
        
        # Remover espaços extras antes de comparar
        hash_calculado = hash_calculado.strip()
        hash_esperado = hash_esperado.strip()
        
        # TODO: Verifique se o hash calculado é igual ao hash esperado:
        if hash_esperado == hash_calculado:
          
            print("Correto")
            
        else:
          
            print("Inválido")
            
        
hashes_usuario = input()

lista_hashes = hashes_usuario.split(";")

verificar_hashes(lista_hashes)