class Utils:
  def readGraphs(self):
    choice = input("Do you want to enter the paths manually(1) or read already saved files(2)? (1/2): ")
    if choice == '1':
        file1 = input("Enter the path of the first file: ")
        file2 = input("Enter the path of the second file: ")

        return file1, file2
    
    elif choice == '2':
        return 'Files/graph1.txt', 'Files/graph2.txt'
    
    else:
        print("Invalid option. Choose '1' to read saved files or '2' to enter paths via terminal.")
        return self.readGraphs()
    
  def readSimilarityMethod(self):
     choice = input("Choose the method for calculating similarity (1 - cosine, 2 - simRank, 3 - jaccard):")
     if choice == '1':
         return 'cosine'
     elif choice == '2':
         return 'simRank'
     elif choice == '3':
         return 'jaccard'
     else:
         print("Invalid option. Choose '1', '2' or '3'.")
         return self.readSimilarityMethod()