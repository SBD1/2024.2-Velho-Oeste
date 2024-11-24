# Modelo Entidade Relacionamento

## Entidades

- Personagem
    - Personagem Principal
    - NPC
        - Sheriff
        - Xamã
        - Bandido
        - Ferreiro
        - Comerciante
        - Dama do Saloon

- Animal 
    - Gado
    - Cavalo 
    - Cachorro

- Cidades

- Missões

- Locais

- Inventário

- Item
    - Item Especial
    - Arma
        - Espingarda Serrada
        - Colt .45
        - Rifle
        - Revolver
        - Faca 
        - Pólvora
        - Pistola Derringer

## Atributos

- Personagem: {id_personagem, nome, classe}
    - Personagem Principal: {id_pers_principal, inventario, reputacao}
    - NPC: {id_NPC, funcao}
        - Sheriff: {id_Sheriff, delegacia, lista_missoes}
        - Xamã: {id_Xama, tipos_cura, buffs}
        - Bandido: {id_bandido, especialidade, nivel_periculosidade, recompensa}
        - Ferreiro: {id_Ferreiro, tipos_equipamentos, materiais}
        - Comerciante: {id_COmerciante,itens_venda, local_atuacao}
        - Dama do Saloon: {id_Dama, dicas, pequenas_missoes}

- Animal: {id_animal, nome, tipo, cor, vidaMax}
    - Gado: {id_gado, tipo_gado}
    - Cavalo: {id_cavalo, tipo_cavalo, velocidade}
    - Cachorro: {id_cachorro, especie, habilidade}

- Cidade: {id_cidade, nome, localizacao}

- Missão: {id_missao, nome, descricao, recompensa, tipo}

- Local: {id_local, nome, tipo}

- Inventário: {id_inventario, PesoMax}

- Item: {id_item, nome, categoria, descricao}
    - Item Especial: {id_item_especial, efeito_especial, origem}
    - Arma:{id_arma, tipo_arma, dano, alcance}
        - Espingarda Serrada: {id_Espingarda_Serrada, cartuchos, dano_extra_curto}
        - Colt .45: {id_Colt_45, municao, tempo_recarga}
        - rifle: {id_rifle, alcance_max, precisao}
        - Revolver: {id_revolver, municao, velocidade_tiro}
        - Faca: {id_faca, dano_corte, durabilidade}
        - Pólvora Explosiva: {id_polvora, raio_explosao, dano_area}
        - Pistola Derringer: {id_pistola, agilidade_tiro, recuo}

## Relacionamentos

- **Personagem referencia InstanciaPersonagem**
- **InstanciaPersonagem está na Sala**
- **Sala tem Região**
- **Sala está Conectada a outra Sala**
- **Região possui Mundo**
- **InstanciaPersonagem carrega Cavalo**
- **Personagem Principal possui Inventário**
- **Inventário tem InstanciaItem**
- **InstanciaItem referência Item**
- **Arma usa Munição**
- **Personagem Principal faz Missão**
- **Animal referencia InstanciaAnimal**



## Histórico de Versão

| Versão |    Data    |                     Descrição                     |                                                                                                Autor(es)                                                                                                 |
| :----: | :--------: | :-----------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| `1.0`  | 24/11/2024 | Primeira versão do Modelo Entidade Relacionamento | [Jefferson Sena](https://github.com/JeffersonSenaa) |                                                |