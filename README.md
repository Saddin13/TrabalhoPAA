# Trabalho de Projeto de Análise de Algoritmos

<<<<<<< Updated upstream
Implementação do algoritmo de ordenação merge sort em uma lista encadeada, simulando o uso no dia a dia em uma planilha do Excel.

## Autores

- Jéssica Cavalcante Costa
- João Pedro Gomes Breta
- João Pedro F. A. L. de Miranda
- Vitor Saddi Ribeiro

## Recomendações e ponto importante

O sistema opera a partir de um arquivo XLS ou XLSX e retorna um arquivo no mesmo formato.
Acompanha um arquivo de testes (todos os dados daquele arquivo foram retirados do Gemini, fizemos a tabela usando a IA da Google Sheets para testes do código)

## Instalação

Bibliotecas usadas: 
- Tkinter (padrão do Python); 
- Pandas (necessário instalar).

```bash
pip install pandas 
```

## Complexidade
- Pior caso: O(n log n);
- Melhor caso: O(n log n).

## Explicação do código

### Bloco 1
O usuário irá escolher qual arquivo será usado para realizar a compilação.

### Bloco 2
O usuário escolherá a coluna que deseja usar para a ordenação.

### Bloco 3
O usuário deverá informar ao código o tipo de dado presente na coluna escolhida para ordenar — seja inteiro (int) ou string. No caso do tipo inteiro, todos os caracteres não numéricos serão ignorados.

### Bloco 4
Seleciona qual algoritmo do merge será utilizado conforme o bloco 3.

### Bloco 5
O programa lê a tabela e constrói uma lista encadeada com base na escolha feita no bloco 3. Em seguida, gera uma lista de índices correspondente ao tamanho da lista de valores.

### Bloco 6
**6.1.** Divide ambas as listas passadas ao meio;  
**6.2.** Junta sublistas já organizadas, comparando os elementos que as compõem;  
**6.3.**Disponibiliza um arquivo organizado pela metade
**6.4.**Trabalha com os elementos restantes à esquerda;
**6.5.**Trabalha com os elementos restantes à direita.

### Bloco 7
O sistema realiza a entrega do arquivo já ordenado ao usuário.

## Referência

- [Link GitHub](https://github.com/Saddin13/TrabalhoPAA)
=======
Bibliotecas nessesarias:
    pandas: ler a tabela de execel
    

precisa ser usado a partir de um arquivo XLS ou XLSX, e devolve um arquivo em mesmo formato, JÁ FORMATADO

ACOMPANHA UM ARQUIVO DE TESTES (TODOS OS DADOS DAQUELE ARQUIVO SAO RETIRADOS DO GEMINI, FIZ A TABELA USANDO A IA DO GOOGLE SHEETS PARA TESTES DO CODIGO)

Complexidade

Explicacao do codigo
    Bloco 1
        O objetivo é fazer com que o usuario escolha o arquivo que será usado na compilacao
    Bloco 2
        O objetivo é fazer com que o usuario escolha qual a coluna da tabela será ordenada
    Bloco 3
        O objetivo é fazer com que o usuario escolha qual o tipo do dado será ultilizado para a organizacao, Int ou String(o de int ignora todos os caracteres nao numerais)
    Bloco 4
        seleciona o merge a ser ultilizado corforme o bloco 3
    Bloco 5
        le a tabela e monta uma lista encadeada(de acordo com a escolha feita no bloco 3)  e monta uma lista de indice q é o tamanho da lista de valores.
    Bloco 6: Merge Sort
        Bloco 6.1
            Divide ambas as listas passada ao meio 
        Bloco 6.2
            junta sublistas já organizadas, comparando os elementos que ha compoem 
        Bloco 6.3
            Disponibiliza um arquivo organizado pela metade    
        Bloco 6.4
            Trabalha com os elementos restantes a esquerda
        Bloco 6.5
            Trabalha com os elementos restantes a direita
    Bloco 7
        realiza a devolucao do arquivo ordenado
>>>>>>> Stashed changes
