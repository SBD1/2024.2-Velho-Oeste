-- SQLBook: Code
CREATE OR REPLACE FUNCTION function_npc() RETURNS TRIGGER AS $function_npc$
BEGIN
    IF EXISTS (SELECT 1 FROM NPC WHERE funcao = NEW.funcao AND idNpc <> NEW.idNpc) THEN
        RAISE EXCEPTION 'Já existe um NPC com essa função';
    END IF;
    RETURN NEW;
END;
$function_npc$ LANGUAGE plpgsql;

CREATE TRIGGER function
BEFORE INSERT OR UPDATE ON NPC
FOR EACH ROW
EXECUTE FUNCTION function_npc();

CREATE OR REPLACE FUNCTION criar_personagem_npc(nome_personagem VARCHAR, classe_personagem VARCHAR, funcao_npc VARCHAR, tipo_npc VARCHAR, dados_npc TEXT) RETURNS VOID AS $criar_npc$
DECLARE
    id_personagem INT;
    id_npc INT;
BEGIN
    -- Criando o personagem
    INSERT INTO PERSONAGEM (nome, classe) VALUES (nome_personagem, classe_personagem) RETURNING idPersonagem INTO id_personagem;

    -- Criando o NPC relacionado ao personagem
    INSERT INTO NPC (idPersonagem, funcao) VALUES (id_personagem, funcao_npc) RETURNING idNpc INTO id_npc;

    --Definindo a classe
    IF tipo_npc = 'Comerciante' THEN
        INSERT INTO COMERCIANTE (idNpc, itensVenda, localAtuacao) VALUES (id_npc, dados_npc, 'Mercado Geral');
    ELSIF tipo_npc = 'Xamã' THEN
        INSERT INTO XAMA (idNpc, tiposCura, buffs) VALUES (id_npc, 'Poções de Vida, Antídotos', 'Força Espiritual, Resistência ao Fogo');
    ELSIF tipo_npc = 'Bandido' THEN
        INSERT INTO BANDIDO (idNpc, especialidade, nivelPericulosidade, recompensa) VALUES (id_npc, 'Assaltante de Diligências', 8, 500.00);
    ELSIF tipo_npc = 'Ferreiro' THEN
        INSERT INTO FERREIRO (idNpc, tipoEquipamento, materiais) VALUES (id_npc, 'Armaduras e Ferraduras', 'Ferro, Couro, Aço');
    ELSIF tipo_npc = 'Sheriff' THEN
        INSERT INTO SHERIFF (idNpc, delegacia) VALUES (id_npc, 'Delegacia de Dusty Town');
    ELSIF tipo_npc = 'Dama do Saloon' THEN
        INSERT INTO DAMA_SALOON (idNpc, dicas, pequenasMissoes) VALUES (id_npc, 'Cuidado com estranhos na estrada.', 'Entregar uma carta secreta para um cliente.');
    END IF;
END;
$criar_npc$ LANGUAGE plpgsql;


CREATE TRIGGER trg_criar_personagem_npc
AFTER INSERT ON NPC
FOR EACH ROW
EXECUTE FUNCTION criar_personagem_npc(
    NEW.funcao,
    'Classe do ' || NEW.funcao,
    NEW.funcao,
    NEW.funcao,
    NULL
);
