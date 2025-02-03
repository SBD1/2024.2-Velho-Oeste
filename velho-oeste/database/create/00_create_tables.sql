CREATE TABLE IF NOT EXISTS INSTANCIAITEM (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS MISSAO (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    dinheiro NUMERIC(10, 2) CHECK (dinheiro >= 0),
    reputacao INT CHECK (reputacao >= 0)
);

CREATE TABLE IF NOT EXISTS ITEMMISSAO (
    missaoid INT,
    itemid INT,
    PRIMARY KEY (missaoid, itemid),
    FOREIGN KEY (missaoid) REFERENCES MISSAO(id),
    FOREIGN KEY (itemid) REFERENCES INSTANCIAITEM(id)
);


INSERT INTO INSTANCIAITEM (nome) VALUES
('Pistola Derringer'),
('Espingarda Serrada'),
('Chapéu Resistente a Balas'),
('Novo Cavalo'),
('Suprimentos Médicos'),
('Arma Rara');


INSERT INTO MISSAO (nome, descricao, dinheiro, reputacao) VALUES
('Início da Jornada', 'Após ouvir histórias sobre bandidos que aterrorizam cidades vizinhas, o caçador de recompensas chega ao Saloon e encontra o xerife, que apresenta seu primeiro contrato: capturar um ladrão de cavalos conhecido por saquear vilas próximas.', 50.00, 10),
('O Cemitério Assombrado', 'Os moradores relatam eventos estranhos no cemitério, onde dizem ver fantasmas e ouvir vozes. O coveiro pede ajuda ao jogador para investigar.', 20.00, 5),
('Perigo no Trem', 'O jogador recebe informações da dama do Saloon sobre um assalto a um trem que carrega ouro e mercadorias valiosas.', 100.00, 20),
('O Ouro da Montanha', 'Com o mapa da mina obtido no cemitério, o jogador é atraído para explorar a montanha e encontrar uma mina que dizem guardar riquezas, mas que é protegida por bandidos locais.', 200.00, 30),
('A Diligência', 'O mercador de cavalos pede ajuda ao jogador para proteger uma diligência carregada de suprimentos e remédios que será enviada para uma cidade próxima.', 150.00, 15),
('A Última Fronteira', 'O xerife pede ajuda para capturar um dos criminosos mais procurados, o líder de uma gangue de bandidos chamada de “Os Renegados do Deserto”.', 500.00, 50);


INSERT INTO MISSAO (nome, descricao, dinheiro, reputacao) VALUES
('Aposta no Saloon', 'O jogador pode participar de um torneio de cartas no Saloon. Se vencer, recebe dicas valiosas sobre locais secretos ou sobre criminosos escondidos.', 10.00, 5),
('Desafio de Duelo', 'Rivais do jogador o desafiam para um duelo. Ele precisa enfrentá-los para manter sua honra como caçador de recompensas.', 20.00, 15),
('Herança Perdida', 'Uma viúva da cidade pede ajuda para recuperar itens de valor de seu marido, que foram roubados por uma gangue.', 30.00, 10),
('Tesouro do Guerreiro', 'Um guia indígena oferece uma missão para encontrar o “Tesouro do Guerreiro”, escondido em cavernas sagradas nas montanhas.', 50.00, 20);


INSERT INTO ITEMMISSAO (missaoid, itemid) VALUES
(2, 1),
(3, 2),
(4, 3),
(5, 4),
(5, 5),
(7, 6);

-- CREATE TABLE IF NOT EXISTS PERSONAGEM (
--     idPersonagem SERIAL PRIMARY KEY,
--     nome VARCHAR(40) NOT NULL,
--     classe VARCHAR(40) NOT NULL
-- );

-- CREATE TABLE IF NOT EXISTS PERSONAGEM_PRINCIPAL (
--     idPersonagem INT PRIMARY KEY,
--     inventario VARCHAR(255),
--     reputacao INT,
--     CONSTRAINT FK_PERSONAGEM_PRINCIPAL_PERSONAGEM FOREIGN KEY (idPersonagem) REFERENCES PERSONAGEM(idPersonagem)
-- );

-- CREATE TABLE IF NOT EXISTS MISSAO (
--     idMissao SERIAL PRIMARY KEY,
--     tipo VARCHAR(50),
--     nome VARCHAR(255),
--     dinheiro NUMERIC(10, 2),
--     descricao VARCHAR(5000),
--     reputacao INT
-- );

-- CREATE TABLE IF NOT EXISTS PERSONAGEM_PRINCIPAL_MISSAO (
--     idPersonagem INT,
--     idMissao INT,
--     PRIMARY KEY (idPersonagem, idMissao),
--     CONSTRAINT FK_PERSONAGEM_PRINCIPAL_MISSAO_PERSONAGEM FOREIGN KEY (idPersonagem) REFERENCES PERSONAGEM_PRINCIPAL(idPersonagem),
--     CONSTRAINT FK_PERSONAGEM_PRINCIPAL_MISSAO_MISSAO FOREIGN KEY (idMissao) REFERENCES MISSAO(idMissao)
-- );

-- CREATE TABLE IF NOT EXISTS NPC (
--     idNpc SERIAL PRIMARY KEY,
--     idPersonagem INT NOT NULL,
--     funcao VARCHAR(100),
--     CONSTRAINT FK_NPC_PERSONAGEM FOREIGN KEY (idPersonagem) REFERENCES PERSONAGEM(idPersonagem)
-- );

-- CREATE TABLE IF NOT EXISTS DAMA_SALOON (
--     idNpc INT PRIMARY KEY,
--     dicas TEXT,
--     pequenasMissoes TEXT,
--     CONSTRAINT FK_DAMA_SALOON_NPC FOREIGN KEY (idNpc) REFERENCES NPC(idNpc)
-- );

-- CREATE TABLE IF NOT EXISTS XAMA (
--     idNpc INT PRIMARY KEY,
--     tiposCura TEXT,
--     buffs TEXT,
--     CONSTRAINT FK_XAMA_NPC FOREIGN KEY (idNpc) REFERENCES NPC(idNpc)
-- );

-- CREATE TABLE IF NOT EXISTS BANDIDO (
--     idNpc INT PRIMARY KEY,
--     especialidade VARCHAR(100),
--     nivelPericulosidade INT,
--     recompensa NUMERIC(10, 2),
--     CONSTRAINT FK_BANDIDO_NPC FOREIGN KEY (idNpc) REFERENCES NPC(idNpc)
-- );

-- CREATE TABLE IF NOT EXISTS COMERCIANTE (
--     idNpc INT PRIMARY KEY,
--     itensVenda TEXT,
--     localAtuacao VARCHAR(100),
--     CONSTRAINT FK_COMERCIANTE_NPC FOREIGN KEY (idNpc) REFERENCES NPC(idNpc)
-- );

-- CREATE TABLE IF NOT EXISTS SHERIFF (
--     idNpc INT PRIMARY KEY,
--     delegacia VARCHAR(100),
--     CONSTRAINT FK_SHERIFF_NPC FOREIGN KEY (idNpc) REFERENCES NPC(idNpc)
-- );

-- CREATE TABLE IF NOT EXISTS FERREIRO (
--     idNpc INT PRIMARY KEY,
--     tipoEquipamento VARCHAR(100),
--     materiais TEXT,
--     CONSTRAINT FK_FERREIRO_NPC FOREIGN KEY (idNpc) REFERENCES NPC(idNpc)
-- );

-- CREATE TABLE IF NOT EXISTS MUNDO (
--     idMundo SERIAL PRIMARY KEY,
--     nome VARCHAR(100) NOT NULL
-- );

-- CREATE TABLE IF NOT EXISTS LOCALIZACAO (
--     idLocal SERIAL PRIMARY KEY,
--     nome VARCHAR(100) NOT NULL,
--     idMundo INT NOT NULL,
--     CONSTRAINT FK_LOCALIZACAO_MUNDO FOREIGN KEY (idMundo) REFERENCES MUNDO(idMundo)
-- );

-- CREATE TABLE IF NOT EXISTS CIDADE (
--     idCidade SERIAL PRIMARY KEY,
--     idLocal INT NOT NULL,
--     nome VARCHAR(100) NOT NULL,
--     localizacao VARCHAR(100) NOT NULL,
--     CONSTRAINT FK_CIDADE_LOCALIZACAO FOREIGN KEY (idLocal) REFERENCES LOCALIZACAO(idLocal)
-- );

-- CREATE TABLE IF NOT EXISTS ANIMAL (
--     idAnimal SERIAL PRIMARY KEY,
--     nome VARCHAR(100) NOT NULL,
--     tipo VARCHAR(50),
--     idGaiola INT
-- );

-- CREATE TABLE IF NOT EXISTS CAVALO (
--     idAnimal INT PRIMARY KEY,
--     idPersonagem INT,
--     tipoCavalo VARCHAR(50),
--     velocidade INT,
--     CONSTRAINT FK_CAVALO_ANIMAL FOREIGN KEY (idAnimal) REFERENCES ANIMAL(idAnimal),
--     CONSTRAINT FK_CAVALO_PERSONAGEM FOREIGN KEY (idPersonagem) REFERENCES PERSONAGEM(idPersonagem)
-- );

-- CREATE TABLE IF NOT EXISTS CACHORRO (
--     idAnimal INT PRIMARY KEY,
--     especie VARCHAR(50),
--     habilidade VARCHAR(50),
--     CONSTRAINT FK_CACHORRO_ANIMAL FOREIGN KEY (idAnimal) REFERENCES ANIMAL(idAnimal)
-- );

-- CREATE TABLE IF NOT EXISTS GADO (
--     idAnimal INT PRIMARY KEY,
--     tipoGado VARCHAR(50),
--     CONSTRAINT FK_GADO_ANIMAL FOREIGN KEY (idAnimal) REFERENCES ANIMAL(idAnimal)
-- );

-- CREATE TABLE IF NOT EXISTS ITEM (
--     idItem SERIAL PRIMARY KEY,
--     nome VARCHAR(100) NOT NULL,
--     categoria VARCHAR(50),
--     descricao TEXT
-- );

-- CREATE TABLE IF NOT EXISTS ITEM_ESPECIAL (
--     idItemEspecial SERIAL PRIMARY KEY,
--     idItem INT NOT NULL,
--     atributoEspecial VARCHAR(255),
--     CONSTRAINT FK_ITEM_ESPECIAL_ITEM FOREIGN KEY (idItem) REFERENCES ITEM(idItem)
-- );

-- CREATE TABLE IF NOT EXISTS ARMA (
--     idArma SERIAL PRIMARY KEY,
--     idItem INT,
--     tipo VARCHAR(50),
--     alcance INT,
--     CONSTRAINT FK_ARMA_ITEM FOREIGN KEY (idItem) REFERENCES ITEM(idItem)
-- );

-- CREATE TABLE IF NOT EXISTS ARMA_BRANCA (
--     idArma INT PRIMARY KEY,
--     danoCorte INT,
--     durabilidade INT,
--     danoPerfurante INT,
--     CONSTRAINT FK_ARMA_BRANCA_ARMA FOREIGN KEY (idArma) REFERENCES ARMA(idArma)
-- );

-- CREATE TABLE IF NOT EXISTS ARMA_DE_FOGO (
--     idArma INT PRIMARY KEY,
--     precisao INT,
--     inicioVeloz INT,
--     tempoRecarga INT,
--     capacidade INT,
--     CONSTRAINT FK_ARMA_DE_FOGO_ARMA FOREIGN KEY (idArma) REFERENCES ARMA(idArma)
-- );

-- CREATE TABLE IF NOT EXISTS EXPLOSIVO (
--     idArma INT PRIMARY KEY,
--     danoArea INT,
--     CONSTRAINT FK_EXPLOSIVO_ARMA FOREIGN KEY (idArma) REFERENCES ARMA(idArma)
-- );

-- CREATE TABLE IF NOT EXISTS ESPINGARDA_SERRADA (
--     idArma INT PRIMARY KEY,
--     danoExtraCurto INT,
--     CONSTRAINT FK_ESPINGARDA_SERRADA_ARMA FOREIGN KEY (idArma) REFERENCES ARMA_DE_FOGO(idArma)
-- );

-- CREATE TABLE IF NOT EXISTS RIFLE (
--     idArma INT PRIMARY KEY,
--     penetracao INT,
--     CONSTRAINT FK_RIFLE_ARMA FOREIGN KEY (idArma) REFERENCES ARMA_DE_FOGO(idArma)
-- );

-- CREATE TABLE IF NOT EXISTS COLT_45 (
--     idArma INT PRIMARY KEY,
--     CONSTRAINT FK_COLT_45_ARMA FOREIGN KEY (idArma) REFERENCES ARMA_DE_FOGO(idArma)
-- );

-- CREATE TABLE IF NOT EXISTS REVOLVER (
--     idArma INT PRIMARY KEY,
--     CONSTRAINT FK_REVOLVER_ARMA FOREIGN KEY (idArma) REFERENCES ARMA_DE_FOGO(idArma)
-- );

-- CREATE TABLE IF NOT EXISTS PISTOLA_DERRINGER (
--     idArma INT PRIMARY KEY,
--     CONSTRAINT FK_PISTOLA_DERRINGER_ARMA FOREIGN KEY (idArma) REFERENCES ARMA_DE_FOGO(idArma)
-- );

-- CREATE TABLE IF NOT EXISTS INVENTARIO (
--     idInventario SERIAL PRIMARY KEY,
--     idPersonagem INT,
--     item VARCHAR(255),
--     CONSTRAINT FK_INVENTARIO_PERSONAGEM FOREIGN KEY (idPersonagem) REFERENCES PERSONAGEM(idPersonagem)
-- );
