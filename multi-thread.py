import sys
import threading

# Variável para contar a qtdade de linhas
total = 0

class minhaThread (threading.Thread):
    threadID = 0
    arquivo = None
    linha = 0
    subtotal = 0

    def __init__(self, threadID, arquivo):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.arquivo = arquivo

    def run(self):
        print(f"Iniciando thread {self.threadID}")
        self.linha = 0
        self.processo() # Inicia o processo
        print(f"Finalizando {self.arquivo}")

    def processo(self):
        # Abre o arquivo
        with open(self.arquivo, newline='') as arquivo_txt:
            # Varre linha a linha
            for row in arquivo_txt:
                self.linha += 1
                print(f"[Thread {self.threadID}] Arquivo '{self.arquivo}' - Linha {self.linha}: {row}")

            # Incrementa o contador, depois que as linhas são lidas
            self.subtotal += self.linha

        print(f"FIM DA THREAD {self.threadID}")

    # Retorna os subtotais lidos
    def get_subtotal(self):
        return self.subtotal

if __name__ == "__main__":
    thread_nro = 0
    threads = []
    for arquivo in sys.argv[1:]: # [1:] para pegar apenas os parâmetros
        thread_nro += 1
        thread = minhaThread(thread_nro, arquivo) # Criamos o objeto da classe
        thread.start() # Inicia a thread
        threads.append(thread) # Adicionamos a thread no array

    # Depois que as threads foram iniciadas, acionamos o .join() para que aguarde o encerramento das demais
    for t in threads:
       t.join() # Aguarda a thread main terminar
       total += t.get_subtotal() # Incrementa o contador, depois que as linhas são lidas

    print("Total lidos: " + str(total))
