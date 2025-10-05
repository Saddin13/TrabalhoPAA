import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd

#Bloco 7 INT
def mergeexit(input,indices,df, file_path):
        df_ordenado = df.iloc[indices].reset_index(drop=True)
        output_path = os.path.splitext(file_path)[0] +'_'+ input + '.xlsx'
        df_ordenado.to_excel(output_path, index=False)
        print(f"Arquivo organizado salvo em: {output_path}")

def MergeShortINT(coluna, file_path):
    #Bloco 5 INT
    print("Organizando arquivo por valor numerico...")
    df = pd.read_excel(file_path)
    df.iloc[:, coluna] = df.iloc[:, coluna].astype(str).str.replace(r'\D', '', regex=True)
    valores = list(df.iloc[:, coluna].astype(int))
    indices = list(range(len(valores)))
    tamanho_original = len(valores)
    metade_salva = [0]
    #Bloco 6 INT
    def merge_sort(arr, idx):
        #Bloco 6.1 INT
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            L_idx = idx[:mid]
            R_idx = idx[mid:]

            merge_sort(L, L_idx)
            merge_sort(R, R_idx)

            i = j = k = 0
            #Bloco 6.2 INT
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    idx[k] = L_idx[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    idx[k] = R_idx[j]
                    j += 1
                k += 1
            #Bloco 6.3 INT
            if metade_salva[0] == 0 and len(arr) == tamanho_original:
                metade_salva[0] = 1
                mergeexit("metade_organizado", idx, df, file_path)
            #Bloco 6.4 INT
            while i < len(L):
                arr[k] = L[i]
                idx[k] = L_idx[i]
                i += 1
                k += 1
            #Bloco 6.5 INT
            while j < len(R):
                arr[k] = R[j]
                idx[k] = R_idx[j]
                j += 1
                k += 1
    merge_sort(valores, indices)
    mergeexit("inteiramente_organizado", indices, df, file_path)

def MergeShortChr(coluna, file_path):
    print("Organizando arquivo por valor string...")
    df = pd.read_excel(file_path)
    valores = list(df.iloc[:, coluna])
    indices = list(range(len(valores)))
    tamanho_original = len(valores)
    metadesalva = [0]
    def merge_sort(arr, idx):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            L_idx = idx[:mid]
            R_idx = idx[mid:]

            merge_sort(L, L_idx)
            merge_sort(R, R_idx)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if str(L[i]) <= str(R[j]):
                    arr[k] = L[i]
                    idx[k] = L_idx[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    idx[k] = R_idx[j]
                    j += 1
                k += 1
            # Salva apenas quando estiver mesclando as duas grandes metades
            if metadesalva[0] == 0 and len(arr) == tamanho_original:
                metadesalva[0] = 1
                mergeexit("metade_organizado", idx, df, file_path)
            while i < len(L):
                arr[k] = L[i]
                idx[k] = L_idx[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                idx[k] = R_idx[j]
                j += 1
                k += 1
    merge_sort(valores, indices)
    mergeexit("inteiramente_organizado", indices, df, file_path)

#Bloco 1
while True:
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Selecione o arquivo para processar")
    if (file_path.endswith('.xls') or file_path.endswith('.xlsx')):
        break
    else:
        print("Erro: O arquivo selecionado não é um arquivo Excel (.xls ou .xlsx).")
print(f"Arquivo selecionado: {file_path}")
#Bloco 2
while True:
    print("qual coluna da tabela voce quer organizar?")
    coluna = input("Digite o numero da coluna: ")
    if coluna.isdigit():
        coluna = int(coluna) - 1  # Ajusta para índice baseado em zero
        break
    else:
        print("Erro: Por favor, insira um número válido para a coluna.")
#Bloco 3
while True:
    print(f"Pelo oque voce quer organizar este arquivo? (1 = valor(NUMERICO) ou 2 = character(STRING))")
    tipo = input("Digite 1 ou 2: ")
    if tipo in ['1', '2']:
        tipo = int(tipo)
        break
    else:
        print("Erro: Por favor, insira 1 ou 2.")
#Bloco 4
if tipo == 1:
    MergeShortINT(coluna, file_path)
else:
    MergeShortChr(coluna, file_path)
