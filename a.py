nomes = ''

import re
import requests
import csv

# nomes = nomes.split()  # Coloca toda string como uma lista
# novosNome = []  # Cria a lista para os nomes da bases de dados
# codigos = []  # Lista de códigos das cidades
# dados_combinados = []
#
#
# def puxaVerificaDadosCidade(codCidade):
#     for i in range(10):
#         link = f"https://servicodados.ibge.gov.br/api/v3/agregados/4709/periodos/2022/variaveis/93?localidades=N6[{codCidade}{i}]"
#         response = requests.get(link)
#
#         if response.status_code == 200:
#             informacoes = response.json()
#             dadosCidade = informacoes[0]['resultados'][0]['series'][0]
#             codCidade = dadosCidade['localidade']['id']
#             nomeCidade = dadosCidade['localidade']['nome']
#             return [codCidade, nomeCidade]
#
# def puxaIdaBase(nome):
#     match = re.search(r'familia_(\d+)', nome)  # Faz regex para buscar os codigos das cidades
#     if match:
#         codigo = match.group(1)  # Pega 'o código da cidade
#         return puxaVerificaDadosCidade(codigo)
#
#
# with open('dados_combinados.csv', 'w', newline='') as csvfileNovo:
#     csv_writer = csv.writer(csvfileNovo)
#     for nomeBase in nomes:  # Itera em toda base de dados
#             with open(f'Peso Baixo/{nomeBase}', newline='') as csvfile:
#                 csv_reader = csv.reader(csvfile)
#                 dadosCorreto = puxaIdaBase(nomeBase)
#                 print(nomeBase, dadosCorreto[0])
#                 for row in csv_reader:
#                     if (len(row) > 0):
#                         if (row[0] != 'base') and row[1] == 's':
#                             row.append(dadosCorreto[0])
#                             row.append(dadosCorreto[1])
#                             csv_writer.writerow(row)
#
# print("========Finalizado!=============")


# import csv
# import psycopg2
# inserts = []
#
# # Open the CSV file
# with open('dadsoCOMB.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     for row in csv_reader:
#         insertUnico = f"INSERT INTO dadosCidades (base, alvo, A, D, Dp, Dn, I, id, SUPP, itemDom, descr, TP, FP, quali, lift, conf, cov, chi, pvalue, sup_p, sup_n, cod_cidade, nome_cidade) VALUES ({row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]},{row[6]}, {row[7]}, {row[8]}, {row[9]}, {row[10]}, {row[11]}, {row[12]}, {row[13]}, {row[14]}, {row[15]}, {row[16]}, {row[17]}, {row[18]}, {row[19]}, {row[20]}, {row[21]}, {row[22]});"
#         inserts.append(insertUnico.replace('"', ""))
#
#
#
# # with open('inserts.csv', 'w', newline='') as csvfileNovo:
# #     csv_writer = csv.writer(csvfileNovo)
# #     for insert in inserts:  # Itera em toda base de dados
# #         csv_writer.writerow([insert])
# #
simples = "'"
duplas = '"'

with open('dadsoCOMB.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Pula o cabeçalho

    # Abrindo o arquivo SQL para escrita
    with open('inserts.sql', 'w') as sql_file:
        # Iterando sobre as linhas do CSV
        for row in csv_reader:
            insert_sql = f"INSERT INTO dadosCidades (base, alvo, A, D, Dp, Dn, I, id, SUPP, itemDom, descr, TP, FP, quali, lift, conf, cov, chi, pvalue, sup_p, sup_n, cod_cidade, nome_cidade) VALUES ('{row[0]}', '{row[1]}', {row[2]}, {row[3]}, {row[4]}, {row[5]},{row[6]}, {row[7]}, {row[8]}, {row[9]}, '{row[10]}', {row[11]}, {row[12]}, {row[13]}, {row[14]}, {row[15]}, {row[16]}, {row[17]}, {row[18]}, {row[19]}, {row[20]}, {row[21]}, '{row[22].replace(simples, duplas)}');"
            # insert into dadosCidades(base, alvo, A, D, Dp, Dn, I, id, SUPP, itemDom, descr, TP, FP, quali, lift, conf, cov, chi,pvalue, sup_p, sup_n, cod_cidade, nome_cidade) values ('DM_peso_familia_110005', 's', 42, 323, 19, 304, 100, 5, 94.73684210526315, 0.5,  'cod_calcamento_domic_fam=nExiste@val_desp_alimentacao_fam_eq=(100;300)@val_desp_aluguel_fam_eq=0@estcivmae=solteira', 7, 41, 0.012930249499180478, 2.479166666666667, 0.14583333333333334, 0.14860681114551083,7.70948390151515, 0.005493145438373315, 0.3684210526315789, 0.13486842105263158, 1100056,'Cerejeiras (RO)');

            # Escrevendo o comando SQL no arquivo SQL
            # sql_file.write(insert_sql % tuple(row) + '\n')
            sql_file.write(insert_sql + '\n')


print("========Finalizado!=============")
