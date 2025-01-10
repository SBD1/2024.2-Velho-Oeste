# Tabelas Presentes no Jogo


#### Criação da tabela PERSONAGEM

```sql
 CREATE TABLE IF NOT EXISTS PERSONAGEM (
    idPersonagem SERIAL PRIMARY KEY,
    nome VARCHAR(40) NOT NULL,
    classe VARCHAR(40) NOT NULL
);
```
#### Criação da tabela PERSONAGEM_PRINCIPAL

```sql       
CREATE TABLE IF NOT EXISTS PERSONAGEM_PRINCIPAL (
    idPersonagem INT PRIMARY KEY,
    inventario VARCHAR(255),
    reputacao INT,

    CONSTRAINT FK_PERSONAGEM_PRINCIPAL_PERSONAGEM FOREIGN KEY (idPersonagem) REFERENCES PERSONAGEM(idPersonagem)
);
```
#### Criação da tabela MISSAO

````sql
CREATE TABLE IF NOT EXISTS MISSAO (
    idMissao SERIAL PRIMARY KEY,
    tipo VARCHAR(50),
    dinheiro NUMERIC(10, 2),
    descricao TEXT,
    reputacao INT
);
````
#### Criação da tabela PERSONAGEM_PRINCIPAL_MISSAO

````sql
CREATE TABLE IF NOT EXISTS PERSONAGEM_PRINCIPAL_MISSAO (
    idPersonagem INT,
    idMissao INT,

    PRIMARY KEY (idPersonagem, idMissao),
    CONSTRAINT FK_PERSONAGEM_PRINCIPAL_MISSAO_PERSONAGEM FOREIGN KEY (idPersonagem) REFERENCES PERSONAGEM_PRINCIPAL(idPersonagem),
    CONSTRAINT FK_PERSONAGEM_PRINCIPAL_MISSAO_MISSAO FOREIGN KEY (idMissao) REFERENCES MISSAO(idMissao)
);
````
#### Criação da tabela NPC

````sql
CREATE TABLE IF NOT EXISTS NPC (
    idNpc SERIAL PRIMARY KEY,
    idPersonagem INT NOT NULL,
    funcao VARCHAR(100),

    CONSTRAINT FK_NPC_PERSONAGEM FOREIGN KEY (idPersonagem) REFERENCES PERSONAGEM(idPersonagem)
);
````
#### Criação da tabela DAMA_SALOON

````sql
CREATE TABLE IF NOT EXISTS DAMA_SALOON (
    idNpc INT PRIMARY KEY,
    dicas TEXT,
    pequenasMissoes TEXT,

    CONSTRAINT FK_DAMA_SALOON_NPC FOREIGN KEY (idNpc) REFERENCES NPC(idNpc)
);
````
#### Criação da tabela XAMA

````sql
CREATE TABLE IF NOT EXISTS XAMA (
    idNpc INT PRIMARY KEY,
    tiposCura TEXT,
    buffs TEXT,

    CONSTRAINT FK_XAMA_NPC FOREIGN KEY (idNpc) REFERENCES NPC(idNpc)
);
````
#### Criação da tabela BANDIDO

````sql
CREATE TABLE IF NOT EXISTS BANDIDO (
    idNpc INT PRIMARY KEY,
    especialidade VARCHAR(100),
    nivelPericulosidade INT,
    recompensa NUMERIC(10, 2),

    CONSTRAINT FK_BANDIDO_NPC FOREIGN KEY (idNpc) REFERENCES NPC(idNpc)
);
````
#### Criação da tabela COMERCIANTE

````sql
CREATE TABLE IF NOT EXISTS COMERCIANTE (
    idNpc INT PRIMARY KEY,
    itensVenda TEXT,
    localAtuacao VARCHAR(100),

    CONSTRAINT FK_COMERCIANTE_NPC FOREIGN KEY (idNpc) REFERENCES NPC(idNpc)
);
````
#### Criação da tabela SHERIFF

````sql
CREATE TABLE IF NOT EXISTS SHERIFF (
    idNpc INT PRIMARY KEY,
    delegacia VARCHAR(100),

    CONSTRAINT FK_SHERIFF_NPC FOREIGN KEY (idNpc) REFERENCES NPC(idNpc)
);
````
#### Criação da tabela FERREIRO

````sql
CREATE TABLE IF NOT EXISTS FERREIRO (
    idNpc INT PRIMARY KEY,
    tipoEquipamento VARCHAR(100),
    materiais TEXT,

    CONSTRAINT FK_FERREIRO_NPC FOREIGN KEY (idNpc) REFERENCES NPC(idNpc)
);
````
#### Criação da tabela LOCALIZACAO

````sql
CREATE TABLE IF NOT EXISTS LOCALIZACAO (
    idLocal SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idMundo INT NOT NULL,

    CONSTRAINT FK_LOCALIZACAO_MUNDO FOREIGN KEY (idMundo) REFERENCES MUNDO(idMundo)
);
````
#### Criação da tabela MUNDO

````sql
CREATE TABLE IF NOT EXISTS MUNDO (
    idMundo SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);
````
#### Criação da tabela CIDADE

````sql
CREATE TABLE IF NOT EXISTS CIDADE (
    idCidade SERIAL PRIMARY KEY,
    idLocal INT NOT NULL,
    nome VARCHAR(100) NOT NULL,
    localizacao VARCHAR(100) NOT NULL,

    CONSTRAINT FK_CIDADE_LOCALIZACAO FOREIGN KEY (idLocal) REFERENCES LOCALIZACAO(idLocal)
);
````
#### Criação da tabela ANIMAL

````sql
CREATE TABLE IF NOT EXISTS ANIMAL (
    idAnimal SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo VARCHAR(50),
    idGaiola INT
);
````
#### Criação da tabela CAVALO

````sql
CREATE TABLE IF NOT EXISTS CAVALO (
    idAnimal INT PRIMARY KEY,
    idPersonagem INT,
    tipoCavalo VARCHAR(50),
    velocidade INT,

    CONSTRAINT FK_CAVALO_ANIMAL FOREIGN KEY (idAnimal) REFERENCES ANIMAL(idAnimal),
    CONSTRAINT FK_CAVALO_PERSONAGEM FOREIGN KEY (idPersonagem) REFERENCES PERSONAGEM(idPersonagem)
);
````
#### Criação da tabela CACHORRO

````sql
CREATE TABLE IF NOT EXISTS CACHORRO (
    idAnimal INT PRIMARY KEY,
    especie VARCHAR(50),
    habilidade VARCHAR(50),

    CONSTRAINT FK_CACHORRO_ANIMAL FOREIGN KEY (idAnimal) REFERENCES ANIMAL(idAnimal)
);
````
#### Criação da tabela GADO

````sql
CREATE TABLE IF NOT EXISTS GADO (
    idAnimal INT PRIMARY KEY,
    tipoGado VARCHAR(50),

    CONSTRAINT FK_GADO_ANIMAL FOREIGN KEY (idAnimal) REFERENCES ANIMAL(idAnimal)
);
````
#### Criação da tabela ITEM

````sql
CREATE TABLE IF NOT EXISTS ITEM (
    idItem SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    descricao TEXT
);
````
#### Criação da tabela ITEM_ESPECIAL

````sql
CREATE TABLE IF NOT EXISTS ITEM_ESPECIAL (
    idItemEspecial SERIAL PRIMARY KEY,
    idItem INT NOT NULL,
    atributoEspecial VARCHAR(255),

    CONSTRAINT FK_ITEM_ESPECIAL_ITEM FOREIGN KEY (idItem) REFERENCES ITEM(idItem)
);
````
#### Criação da tabela ARMA

````sql
CREATE TABLE IF NOT EXISTS ARMA (
    idArma SERIAL PRIMARY KEY,
    idItem INT,
    tipo VARCHAR(50),
    alcance INT,

    CONSTRAINT FK_ARMA_ITEM FOREIGN KEY (idItem) REFERENCES ITEM(idItem)
);
````

#### Criação da tabela ARMA_BRANCA

````sql
CREATE TABLE IF NOT EXISTS ARMA_BRANCA (
    idArma INT PRIMARY KEY,
    danoCorte INT,
    durabilidade INT,
    danoPerfurante INT,

    CONSTRAINT FK_ARMA_BRANCA_ARMA FOREIGN KEY (idArma) REFERENCES ARMA(idArma)
);
````
#### Criação da tabela ARMA_DE_FOGO

````sql
CREATE TABLE IF NOT EXISTS ARMA_DE_FOGO (
    idArma INT PRIMARY KEY,
    precisao INT,
    inicioVeloz INT,
    tempoRecarga INT,
    capacidade INT,

    CONSTRAINT FK_ARMA_DE_FOGO_ARMA FOREIGN KEY (idArma) REFERENCES ARMA(idArma)
);
````
#### Criação da tabela EXPLOSIVO

````sql
CREATE TABLE IF NOT EXISTS EXPLOSIVO (
    idArma INT PRIMARY KEY,
    danoArea INT,

    CONSTRAINT FK_EXPLOSIVO_ARMA FOREIGN KEY (idArma) REFERENCES ARMA(idArma)
);
````
#### Criação da tabela ESPINGARDA_SERRADA

````sql
CREATE TABLE IF NOT EXISTS ESPINGARDA_SERRADA (
    idArma INT PRIMARY KEY,
    danoExtraCurto INT,

    CONSTRAINT FK_ESPINGARDA_SERRADA_ARMA FOREIGN KEY (idArma) REFERENCES ARMA_DE_FOGO(idArma)
);
````
#### Criação da tabela RIFLE

````sql
CREATE TABLE IF NOT EXISTS RIFLE (
    idArma INT PRIMARY KEY,
    penetracao INT,

    CONSTRAINT FK_RIFLE_ARMA FOREIGN KEY (idArma) REFERENCES ARMA_DE_FOGO(idArma)
);
````
#### Criação da tabela COLT_45

````sql
CREATE TABLE IF NOT EXISTS COLT_45 (
    idArma INT PRIMARY KEY,

    CONSTRAINT FK_COLT_45_ARMA FOREIGN KEY (idArma) REFERENCES ARMA_DE_FOGO(idArma)
);
````
#### Criação da tabela REVOLVER

````sql
CREATE TABLE IF NOT EXISTS REVOLVER (
    idArma INT PRIMARY KEY,

    CONSTRAINT FK_REVOLVER_ARMA FOREIGN KEY (idArma) REFERENCES ARMA_DE_FOGO(idArma)
);
````
#### Criação da tabela PISTOLA_DERRINGER

````sql
CREATE TABLE IF NOT EXISTS PISTOLA_DERRINGER (
    idArma INT PRIMARY KEY,

    CONSTRAINT FK_PISTOLA_DERRINGER_ARMA FOREIGN KEY (idArma) REFERENCES ARMA_DE_FOGO(idArma)
);
````
#### Criação da tabela INVENTARIO

````sql
CREATE TABLE IF NOT EXISTS INVENTARIO (
    idInventario SERIAL PRIMARY KEY,
    idPersonagem INT,
    item VARCHAR(255),

    CONSTRAINT FK_INVENTARIO_PERSONAGEM FOREIGN KEY (idPersonagem) REFERENCES PERSONAGEM(idPersonagem)
);
````