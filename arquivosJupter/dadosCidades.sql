CREATE TABLE dadosCidades (
    base VARCHAR(50),
    alvo VARCHAR(10),
    A int,
    D int,
    Dp int,
    Dn int,
    I int,
    id int,
    SUPP FLOAT,
    itemDom FLOAT,
    descr VARCHAR(250),
    TP INT,
    FP INT,
    quali FLOAT,
    lift FLOAT,
    conf FLOAT,
    cov FLOAT,
    chi FLOAT,
    pvalue VARCHAR(100),
    sup_p FLOAT,
    sup_n FLOAT,
    cod_cidade INT,
    nome_cidade VARCHAR(150)
      );

CREATE TABLE historico (
     id SERIAL PRIMARY KEY,
     cpf_aluno VARCHAR(14) NOT NULL,
     id_disciplina INT NOT NULL,
     status int NOT NULL,
     ano int NOT NULL,
     semestre int NOT NULL,
     nota DECIMAL(5,2) NOT NULL,
     --PROFESSOR
     FOREIGN KEY (cpf_aluno) REFERENCES aluno(cpf) ON DELETE CASCADE,
     FOREIGN KEY (id_disciplina) REFERENCES disciplina(id) ON DELETE CASCADE
);