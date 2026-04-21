import pandas as pd
nota = {'alunos':['bruno', 'joao', 'ana', 'jose'],
        'Notas':['10', '7', '10', '4'],
        'situação':['aprovado', 'aprovado', 'aprovado', 'reprovado']}
tabela = pd.DataFrame(nota)
print(tabela)