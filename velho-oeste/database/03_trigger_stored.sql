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
