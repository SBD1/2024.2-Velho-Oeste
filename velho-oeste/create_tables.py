import psycopg2
from database import create_connection

connection = create_connection()
cur = connection.cursor()

def create_tables():
    """ create tables in the PostgreSQL database """
    comandos = (
        """
        create table PERSONAGEM (
            idPersonagem int not null auto_increment,
            nome varchar(40) not null,
            classe varchar(40) not null,
            constraint PERSONAGEM_PK primary key (idPersonagem)
        ) ENGINE = INNODB;
        """,
        """
        create table PERSONAGEM_PRINCIPAL (
            idPersonagem int not null,
            inventario varchar(255),
            reputacao int,
            constraint PERSONAGEM_PRINCIPAL_PK primary key (idPersonagem),
            constraint FK_PERSONAGEM_PRINCIPAL_PERSONAGEM foreign key (idPersonagem) references PERSONAGEM(idPersonagem)
        ) ENGINE = INNODB;
        """,
        """
        create table MISSAO (
            idMissao int not null auto_increment,
            tipo varchar(50),
            dinheiro decimal(10, 2),
            descricao text,
            reputacao int,
            constraint MISSAO_PK primary key (idMissao)
        ) ENGINE = INNODB;
        """,
        """
        create table PERSONAGEM_PRINCIPAL_MISSAO (
            idPersonagem int not null,
            idMissao int not null,
            constraint PERSONAGEM_PRINCIPAL_MISSAO_PK primary key (idPersonagem, idMissao),
            constraint FK_PERSONAGEM_PRINCIPAL_MISSAO_PERSONAGEM foreign key (idPersonagem) references PERSONAGEM_PRINCIPAL(idPersonagem),
            constraint FK_PERSONAGEM_PRINCIPAL_MISSAO_MISSAO foreign key (idMissao) references MISSAO(idMissao)
        ) ENGINE = INNODB;
        """,
        """
        create table NPC (
            idNpc int not null auto_increment,
            idPersonagem int not null,
            funcao varchar(100),
            constraint NPC_PK primary key (idNpc),
            constraint FK_NPC_PERSONAGEM foreign key (idPersonagem) references PERSONAGEM(idPersonagem)
        ) ENGINE = INNODB;
        """,
        """
        create table DAMA_SALOON (
            idNpc int not null,
            dicas text,
            pequenasMissoes text,
            constraint DAMA_SALOON_PK primary key (idNpc),
            constraint FK_DAMA_SALOON_NPC foreign key (idNpc) references NPC(idNpc)
        ) ENGINE = INNODB;
        """,
        """
        create table XAMA (
            idNpc int not null,
            tiposCura text,
            buffs text,
            constraint XAMA_PK primary key (idNpc),
            constraint FK_XAMA_NPC foreign key (idNpc) references NPC(idNpc)
        ) ENGINE = INNODB;
        """,
        """
        create table BANDIDO (
            idNpc int not null,
            especialidade varchar(100),
            nivelPericulosidade int,
            recompensa decimal(10,2),
            constraint BANDIDO_PK primary key (idNpc),
            constraint FK_BANDIDO_NPC foreign key (idNpc) references NPC(idNpc)
        ) ENGINE = INNODB;
        """,
        """
        create table COMERCIANTE (
            idNpc int not null,
            itensVenda text,
            localAtuacao varchar(100),
            constraint COMERCIANTE_PK primary key (idNpc),
            constraint FK_COMERCIANTE_NPC foreign key (idNpc) references NPC(idNpc)
        ) ENGINE = INNODB;
        """,
        """
        create table SHERIFF (
            idNpc int not null,
            delegacia varchar(100),
            constraint SHERIFF_PK primary key (idNpc),
            constraint FK_SHERIFF_NPC foreign key (idNpc) references NPC(idNpc)
        ) ENGINE = INNODB;
        """,
        """
        create table FERREIRO (
            idNpc int not null,
            tipoEquipamento varchar(100),
            materiais text,
            constraint FERREIRO_PK primary key (idNpc),
            constraint FK_FERREIRO_NPC foreign key (idNpc) references NPC(idNpc)
        ) ENGINE = INNODB;
        """,
        """
        create table CIDADE (
            idCidade int not null,
            idLocal int not null,
            nome varchar(100) not null,
            localizacao varchar(100) not null,
            constraint CIDADE_PK primary key (idCidade),
            constraint FK_CIDADE_LOCALIZACAO foreign key (idLocal) references LOCALIZACAO (idLocal)
        ) ENGINE = INNODB;
        """,
        """
        create table LOCALIZACAO (
            idLocal int not null auto_increment,
            nome varchar(100) not null,
            idMundo int not null,
            constraint LOCAL_PK primary key (idLocal),
            constraint FK_LOCALIZACAO_MUNDO foreign key (idMundo) references MUNDO(idMundo)
        ) ENGINE = INNODB;
        """,
        """
        create table MUNDO (
            idMundo int not null auto_increment,
            nome varchar(100) not null,
            constraint MUNDO_PK primary key (idMundo)
        ) ENGINE = INNODB;
        """,
        """
        create table ANIMAL (
            idAnimal int not null auto_increment,
            nome varchar(100) not null,
            tipo varchar(50),
            idGaiola int,
            constraint ANIMAL_PK primary key (idAnimal)
        ) ENGINE = INNODB;
        """,
        """
        create table CAVALO (
            idAnimal int not null,
            idPersonagem int,
            tipoCavalo varchar(50),
            velocidade int,
            constraint CAVALO_PK primary key (idAnimal),
            constraint FK_CAVALO_ANIMAL foreign key (idAnimal) references ANIMAL(idAnimal),
            constraint FK_CAVALO_PERSONAGEM foreign key (idPersonagem) references PERSONAGEM(idPersonagem)
        ) ENGINE = INNODB;
        """,
        """
        create table CACHORRO (
            idAnimal int not null,
            especie varchar(50),
            habilidade varchar(50),
            constraint CACHORRO_PK primary key (idAnimal),
            constraint FK_CACHORRO_ANIMAL foreign key (idAnimal) references ANIMAL(idAnimal)
        ) ENGINE = INNODB;
        """,
        """
        create table GADO (
            idAnimal int not null,
            tipoGado varchar(50),
            constraint GADO_PK primary key (idAnimal),
            constraint FK_GADO_ANIMAL foreign key (idAnimal) references ANIMAL(idAnimal)
        ) ENGINE = INNODB;
        """,
        """
        create table ITEM (
            idItem int not null auto_increment,
            nome varchar(100) not null,
            categoria varchar(50),
            descricao text,
            constraint ITEM_PK primary key (idItem)
        ) ENGINE = INNODB;
        """,
        """
        create table ITEM_ESPECIAL (
            idItemEspecial int not null,
            idItem int not null,
            atributoEspecial varchar(255),
            constraint ITEM_ESPECIAL_PK primary key (idItemEspecial),
            constraint FK_ITEM_ESPECIAL_ITEM foreign key (idItem) references ITEM(idItem)
        ) ENGINE = INNODB;
        """,
        """
        create table ARMA (
            idArma int not null auto_increment,
            idItem int,
            tipo varchar(50),
            alcance int,
            constraint ARMA_PK primary key (idArma),
            constraint FK_ARMA_ITEM foreign key (idItem) references ITEM(idItem)
        ) ENGINE = INNODB;
        """,
        """
        create table ARMA_BRANCA (
            idArma int not null,
            danoCorte int,
            durabilidade int,
            danoPerfurante int,
            constraint ARMA_BRANCA_PK primary key (idArma),
            constraint FK_ARMA_BRANCA_ARMA foreign key (idArma) references ARMA(idArma)
        ) ENGINE = INNODB;
        """,
        """
        create table ARMA_DE_FOGO (
            idArma int not null,
            precisao int,
            inicioVeloz int,
            tempoRecarga int,
            capacidade int,
            constraint ARMA_DE_FOGO_PK primary key (idArma),
            constraint FK_ARMA_DE_FOGO_ARMA foreign key (idArma) references ARMA(idArma)
        ) ENGINE = INNODB;
        """,
        """
        create table EXPLOSIVO (
            idArma int not null,
            danoArea int,
            constraint EXPLOSIVO_PK primary key (idArma),
            constraint FK_EXPLOSIVO_ARMA foreign key (idArma) references ARMA(idArma)
        ) ENGINE = INNODB;
        """,
        """
        create table ESPINGARDA_SERRADA (
            idArma int not null,
            danoExtraCurto int,
            constraint ESPINGARDA_SERRADA_PK primary key (idArma),
            constraint FK_ESPINGARDA_SERRADA_ARMA foreign key (idArma) references ARMA_DE_FOGO(idArma)
        ) ENGINE = INNODB;
        """,
        """
        create table RIFLE (
            idArma int not null,
            penetracao int,
            constraint RIFLE_PK primary key (idArma),
            constraint FK_RIFLE_ARMA foreign key (idArma) references ARMA_DE_FOGO(idArma)
        ) ENGINE = INNODB;
        """,
        """
        create table COLT_45 (
            idArma int not null,
            constraint COLT_45_PK primary key (idArma),
            constraint FK_COLT_45_ARMA foreign key (idArma) references ARMA_DE_FOGO(idArma)
        ) ENGINE = INNODB;
        """,
        """
        create table REVOLVER (
            idArma int not null,
            constraint REVOLVER_PK primary key (idArma),
            constraint FK_REVOLVER_ARMA foreign key (idArma) references ARMA_DE_FOGO(idArma)
        ) ENGINE = INNODB;
        """,
        """
        create table PISTOLA_DERRINGER (
            idArma int not null,
            constraint PISTOLA_DERRINGER_PK primary key (idArma),
            constraint FK_PISTOLA_DERRINGER_ARMA foreign key (idArma) references ARMA_DE_FOGO(idArma)
        ) ENGINE = INNODB;
        """,
        """
        create table INVENTARIO (
            idInventario int not null auto_increment,
            idPersonagem int,
            item varchar(255),
            constraint INVENTARIO_PK primary key (idInventario),
            constraint FK_INVENTARIO_PERSONAGEM foreign key (idPersonagem) references PERSONAGEM(idPersonagem)
        ) ENGINE = INNODB;
        """)
    try:
        for comando in comandos:
            cur.execute(comando)

        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        print("Tabelas criadas com sucesso")

if __name__ == '__main__':
    create_tables()