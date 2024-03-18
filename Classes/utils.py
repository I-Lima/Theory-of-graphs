class Utils:
  def readGraphs(self):
    choice = input("Deseja inserir os caminhos manualmente ou ler os arquivos já salvos? (1/2): ")
    if choice == '1':
        file1 = input("Digite o caminho do primeiro arquivo: ")
        file2 = input("Digite o caminho do segundo arquivo: ")
        return file1, file2
    
    elif choice == '2':
        return 'File/graph1.txt', 'File/graph2.txt'
    
    else:
        print("Opção inválida. Por favor, escolha '1' para ler de arquivos salvos ou '2' para inserir os caminhos pelo terminal.")
        return self.readGraphs()