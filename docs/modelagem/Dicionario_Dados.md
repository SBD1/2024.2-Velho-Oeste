# Dicionário de Dados

O dicionário de dados são informações sobre os dados armazenados que são pertinentes para o banco de dados. Ele documenta a estrutura, os tipos, os relacionamentos e outras características dos dados, servindo como uma referência essencial para o desenvolvimento.

---

## Entidade: **Personagem**

**Descrição:** Entidade genérica que representa todos os personagens do jogo.

| Nome Variável     | Tipo       | Descrição                               | Valores Permitidos   | Permite Valores Nulos? | É Chave? |
|-------------------|------------|-----------------------------------------|----------------------|------------------------|----------|
| id_personagem     | INT        | Identificador único do personagem       | 1-10000              | não                    | PK       |
| nome              | VARCHAR    | Nome do personagem                      | 1-255 caracteres     | não                    | -        |
| classe              | VARCHAR    | Classe de personagem (NPC, Jogador, etc.) | 1-255 caracteres     | não                    | -        |
| vidaMax              | INT    | Nivél da vida do personagem | 1-10000     | sim                    | -        |

---

## Entidade: **Personagem Principal**

**Descrição:** Subentidade de Personagem, representando o personagem controlado pelo jogador.

| Nome Variável     | Tipo       | Descrição                  | Valores Permitidos   | Permite Valores Nulos? | É Chave? |
|-------------------|------------|----------------------------|----------------------|------------------------|----------|
| id_pers_principal    | INT        | Identificador do personagem (herdado) | 1-10000              | não                    | FK  |
| inventario        | VARCHAR       | Itens do personagem        | -                    | sim                    | -        |
| reputacao         | INT        | Reputação do personagem    | 0-100                | não                    | -        |
| dinheiro         | INT        | Dinheiro que o personagem possui    | 0-10000                | não                    | -        |

---

## Entidade: **NPC**

**Descrição:** Subentidade genérica de Personagem. Representa os personagens não jogáveis que interagem com o jogador.

| Nome Variável  | Tipo       | Descrição                          | Valores Permitidos   | Permite Valores Nulos? | É Chave? |
|----------------|------------|------------------------------------|----------------------|------------------------|----------|
| id_NPC  | INT        | Identificador do personagem (herdado) | 1-10000              | não                    | FK  |
| funcao            | VARCHAR       | Função desempenhada no jogo             | -                    | não                   | -        |

---

## Entidade: **Sheriff**

**Descrição:** Subentidade de NPC, representando o xerife do jogo.

| Nome Variável     | Tipo       | Descrição                  | Valores Permitidos   | Permite Valores Nulos? | É Chave? |
|-------------------|------------|----------------------------|----------------------|------------------------|----------|
| id_Sheriff     | INT        | Identificador do personagem (herdado) | 1-10000              | não                    | FK  |
| missão     | VARCHAR       | Missões disponíveis        | -                    | sim                    | -        |

---

## Entidade: **Xamã**

**Descrição:** Subentidade de NPC, representando o curandeiro do jogo.

| Nome Variável     | Tipo       | Descrição                  | Valores Permitidos   | Permite Valores Nulos? | É Chave? |
|-------------------|------------|----------------------------|----------------------|------------------------|----------|
| id_Xama     | INT        | Identificador do personagem (herdado) | 1-10000              | não                    | FK  |
| tipos_cura        | VARCHAR       | Tipos de cura disponíveis  | -                    | sim                    | -        |
| buffs             | VARCHAR      | Buffs criados pelo xamã    | -                    | sim                    | -        |

---

## Entidade: **Bandido**

**Descrição:** Subentidade de NPC, representando os bandidos do jogo.

| Nome Variável         | Tipo       | Descrição                  | Valores Permitidos   | Permite Valores Nulos? | É Chave? |
|-----------------------|------------|----------------------------|----------------------|------------------------|----------|
| id_Bandido         | INT        | Identificador do personagem (herdado) | 1-10000              | não                    | FK  |
| especialidade         | VARCHAR    | Tipo de crime cometido     | 1-255 caracteres     | não                    | -        |
| periculosidade  | INT        | Nível de periculosidade    | 1-10                 | não                    | -        |
| recompensa            | VARCHAR    | Recompensa oferecida       | 1-255 caracteres     | sim                    | -        |

---

## Entidade: **Ferreiro**

**Descrição:** Subentidade de NPC, representando ferreiros no jogo.

| Nome Variável         | Tipo       | Descrição                         | Valores Permitidos   | Permite Valores Nulos? | É Chave? |
|-----------------------|------------|-----------------------------------|----------------------|------------------------|----------|
| id_Ferreiro        | INT        | Identificador do personagem (herdado) | 1-10000              | não                    | FK  |
| tipos_item      | VARCHAR       | Itens que podem ser melhorados | -                    | sim                    | -        |
| materiais             | VARCHAR       | Materiais necessários para reparo | -                    | sim                    | -        |

---

## Entidade: **Comerciante**

**Descrição:** Subentidade de NPC, representando os comerciantes no jogo.

| Nome Variável     | Tipo       | Descrição                         | Valores Permitidos   | Permite Valores Nulos? | É Chave? |
|-------------------|------------|-----------------------------------|----------------------|------------------------|----------|
| id_Comerciante     | INT        | Identificador do personagem (herdado) | 1-10000              | não                    | FK  |
| itens_venda       | VARCHAR       | Itens disponíveis para venda      | -                    | sim                    | -        |

---

## Entidade: **Dama do Saloon**

**Descrição:** Subentidade de NPC, representando a NPC Dama do Saloon.

| Nome Variável     | Tipo       | Descrição                         | Valores Permitidos   | Permite Valores Nulos? | É Chave? |
|-------------------|------------|-----------------------------------|----------------------|------------------------|----------|
| id_Dama    | INT        | Identificador do personagem (herdado) | 1-10000              | não                    | FK   |
| missoes  | VARCHAR       | Pequenas missões disponíveis      | -                    | sim                    | -        |

---

## Entidade: **Animal**

**Descrição:** Entidade genérica que representa todos os tipos de animais no jogo, seja para trabalho, transporte ou interação.

| Nome Variável  | Tipo       | Descrição                    | Valores Permitidos   | Permite Valores Nulos? | É Chave? |
|----------------|------------|------------------------------|----------------------|------------------------|----------|
| id_animal      | INT        | Identificador único do animal | 1-1000               | não                    | PK       |
| nome           | VARCHAR    | Nome do animal               | 1-255 caracteres     | não                    | -        |
| tipo           | VARCHAR    | Tipo de animal (Gado, Cavalo, Cachorro) | 1-255 caracteres     | não                    | -        |
| cor            | VARCHAR    | Cor do animal                | 1-255 caracteres     | sim                    | -        |
| vidaMax        | INT        | Vida que o animal possui     | 1-100                | não                    | -        |

---

## Entidade: **Gado**

**Descrição:** Subentidade de Animal, representando o gado no jogo.

| Nome Variável  | Tipo       | Descrição                      | Valores Permitidos   | Permite Valores Nulos? | É Chave? |
|----------------|------------|--------------------------------|----------------------|------------------------|----------|
| id_gado      | INT        | Identificador único do animal (herdado) | 1-1000              | não                    | FK  |
| especie      | VARCHAR    | Espécie de gado (Vaca, Búfalo, etc.) | 1-255 caracteres     | não                    | -        |

---

## Entidade: **Cavalo**

**Descrição:** Subentidade de Animal, representando os cavalos no jogo.

| Nome Variável  | Tipo       | Descrição                      | Valores Permitidos   | Permite Valores Nulos? | É Chave? |
|----------------|------------|--------------------------------|----------------------|------------------------|----------|
| id_cavalo      | INT        | Identificador único do animal (herdado) | 1-1000              | não                    | FK   |
| categoria    | VARCHAR    | Tipo de cavalo (Cavalo de Corrida, Cavalo de Trabalho, etc.) | 1-255 caracteres     | não                    | -        |
| velocidade     | INT        | Velocidade do cavalo (quanto maior, mais rápido) | 1-100                | sim                    | -        |
| pesoMax     | INT        | Peso máximo que o cavalo consegue carregar | 1-100                | não                    | -        |
| força     | INT        | Quanto de força o cavalo tem (Quanto mais forte mais resistente) | 1-100                | não                   | -        |

---

## Entidade: **Cachorro**

**Descrição:** Subentidade de Animal, representando os cachorros no jogo.

| Nome Variável  | Tipo       | Descrição                      | Valores Permitidos   | Permite Valores Nulos? | É Chave? |
|----------------|------------|--------------------------------|----------------------|------------------------|----------|
| id_cachorro      | INT        | Identificador único do animal (herdado) | 1-1000              | não                    | FK   |
| especie  | VARCHAR    | Espécie do cachorro (Pastor, Labrador, etc.) | 1-255 caracteres     | não                    | -        |
| habilidade     | VARCHAR    | Habilidade especial do cachorro (Protetor, Caçador, etc.) | 1-255 caracteres     | sim                    | -        |

---

## Entidade: **Cidade**

**Descrição:** Representa as cidades presentes no jogo, que podem ser exploradas pelos jogadores e onde ocorrem interações.

| Nome Variável  | Tipo       | Descrição                  | Valores Permitidos   | Permite Valores Nulos? | É Chave? |
|----------------|------------|----------------------------|----------------------|------------------------|----------|
| id_cidade      | INT        | Identificador único da cidade | 1-1000              | não                    | PK       |
| nome           | VARCHAR    | Nome da cidade             | 1-255 caracteres     | não                    | -        |
| localizacao    | VARCHAR    | Localização geográfica     | 1-255 caracteres     | não                    | -        |

---

## Entidade: **Missão**

**Descrição:** Representa missões disponíveis para os jogadores, com diferentes objetivos e recompensas.

| Nome Variável  | Tipo       | Descrição                  | Valores Permitidos   | Permite Valores Nulos? | É Chave? |
|----------------|------------|----------------------------|----------------------|------------------------|----------|
| id_missao      | INT        | Identificador único da missão | 1-1000              | não                    | PK       |
| nome           | VARCHAR    | Nome da missão             | 1-255 caracteres     | não                    | -        |
| descricao      | VARCHAR      | Descrição da missão        | -                    | sim                    | -        |
| recompensa     | VARCHAR    | Recompensa dada pela missão | 1-255 caracteres     | sim                    | -        |
| tipo           | VARCHAR    | Tipo de missão (Primária ou Secundária) | Primária, Secundária | não                    | -        |
| reputação          | INT    | Quantidade de reputação ganha ou perdida pela missão | 1-10 | não                    | -        |

---

## Entidade: **Local**

**Descrição:** Representa locais específicos no mapa do jogo, como pontos de interesse ou áreas interativas.

| Nome Variável  | Tipo       | Descrição                  | Valores Permitidos   | Permite Valores Nulos? | É Chave? |
|----------------|------------|----------------------------|----------------------|------------------------|----------|
| id_local       | INT        | Identificador único do local | 1-1000              | não                    | PK       |
| nome           | VARCHAR    | Nome do local (Saloon, Mina, Vila, etc.)             | 1-255 caracteres     | não                    | -        |

---

## Entidade: **Inventário**

**Descrição:** Representa os itens possuídos pelo Personagem Principal, como armas, equipamentos e itens especiais.

| Nome da Variável      | Tipo     | Descrição                                              | Valores Permitidos | Permite Valores Nulos? | É Chave?           |
|-----------------------|----------|--------------------------------------------------------|--------------------|------------------------|--------------------|
| id_inventario         | INT      | Identificador único do inventário                     | 1-10000            | não                    | PK                 |
| id_pers_principal | INT     | Identificador do personagem principal                 | 1-10000            | não                    | FK |
| id_item               | INT      | Identificador do item presente no inventário          | 1-10000            | não                    | FK          |
| PesoMax            | INT      | Peso máximo que o inventário suporta (Quantidade de itens)       | 1-100              | sim                    | -                  |

---

## Entidade: **Item**

**Descrição:** Entidade genérica que representa todos os itens disponíveis no jogo, desde consumíveis a armas.

| Nome Variável  | Tipo       | Descrição                          | Valores Permitidos     | Permite Valores Nulos? | É Chave? |
|----------------|------------|------------------------------------|------------------------|------------------------|----------|
| id_item        | INT        | Identificador único do item        | 1-1000                | não                    | PK       |
| nome           | VARCHAR    | Nome do item                      | 1-255 caracteres       | não                    | -        |
| categoria      | VARCHAR    | categoria do item (Ex.: Arma, item especial, munição, etc) | 1-255 caracteres | não                    | -        |
| descricao      | VARCHAR       | Descrição detalhada do item        | -                      | sim                    | -        |
| valor      | INT       | Quanto o item vale (Em dinheiro)       | -                      | não                | -        |

---

## Entidade: **Item Especial**

**Descrição:** Subentidade de Item. Representa itens raros ou únicos no jogo, que podem ser obtidos em missões ou eventos.

| Nome Variável      | Tipo       | Descrição                          | Valores Permitidos     | Permite Valores Nulos? | É Chave? |
|--------------------|------------|------------------------------------|------------------------|------------------------|----------|
| id_item_especial           | INT        | Identificador único do item (herdado) | 1-1000                | não                    | FK   |
| efeito_especial    | VARCHAR      | Efeito único proporcionado pelo item | -                      | sim                    | -        |
| origem             | VARCHAR    | Onde o item foi obtido             | 1-255 caracteres       | sim                    | -        |

---

## Entidade: **Arma**

**Descrição:** Subentidade Genérica de Item. Representa armas usadas no jogo, que podem ser de diferentes tipos e ter atributos específicos.

| Nome Variável      | Tipo       | Descrição                          | Valores Permitidos     | Permite Valores Nulos? | É Chave? |
|--------------------|------------|------------------------------------|------------------------|------------------------|----------|
| id_arma            | INT        | Identificador único do item (herdado) | 1-1000                | não                    | FK  |
| tipo          | VARCHAR    | Tipo de arma (Ex.: Espingarda, Pistola, etc.) | 1-255 caracteres | não                    | -        |
| dano               | INT        | Dano causado pela arma             | 1-100                 | não                    | -        |
| alcanceMax            | INT        | Alcance da arma (em metros)        | 1-100                 | sim                    | -        |
| velocidade            | INT        | Velocidade de ataque da arma       | 1-100                 | não                    | -        |

---

## Entidade: **Armas Brancas**

**Descrição:** Subentidade de arma.

| Nome Variável     | Tipo       | Descrição                              | Valores Permitidos | Permite Valores Nulos? | É Chave? |
|-------------------|------------|----------------------------------------|--------------------|------------------------|----------|
| id_Arma_Branca          | INT        | Identificador único do item (herdado) | 1-1000             | não                    | FK   |
| dano_corte        | INT        | Dano causado por golpes de corte       | 1-50               | não                    | -        |
| dano_perfuração         | INT        | Dano causado por golpes perfurantes                  | 1-50             | não                    | -        |
| durabilidade      | INT        | Durabilidade da arma                  | 1-100              | sim                    | -        |

---

## Entidade: **Explosivos**

**Descrição:** Subentidade de arma.

| Nome Variável     | Tipo       | Descrição                              | Valores Permitidos | Permite Valores Nulos? | É Chave? |
|-------------------|------------|----------------------------------------|--------------------|------------------------|----------|
| id_Explosivos          | INT        | Identificador único do item (herdado) | 1-1000             | não                    | FK   |
| raio_explosao     | INT        | Raio da explosão (em metros)           | 1-20               | não                    | -        |
| dano_area         | INT        | Dano em área                          | 1-100              | não                    | -        |

---

## Entidade: **Armas de Fogo**

**Descrição:** Subentidade de arma.

| Nome Variável     | Tipo       | Descrição                              | Valores Permitidos | Permite Valores Nulos? | É Chave? |
|-------------------|------------|----------------------------------------|--------------------|------------------------|----------|
| id_Arma_Fogo          | INT        | Identificador único do item (herdado) | 1-1000             | não                    | FK   |
| precisao          | FLOAT      | Precisão da arma (de 0 a 1)            | 0.1-1.0            | não                   | -        |
| recuo             | FLOAT      | Recuo da arma (impacto no jogador)     | 0.1-2.0            | não                    | -        |
| tempo_recarga          | INT        | Quanto tempo se demora para recarregar a arma | 1-100             | não                    | -   |
| qtd_munição     | INT        | Quantidade de munição que se tem para aquela arma         | 1-1000               | não                    | -        |
| capacidade     | INT        | Capacidade de munição do pente da arma                  | 1-6                | não                    | -        |
| classe         | VARCHAR        | Identificação de que tipo de arma de fogo                  | 1-255               | não                    | -        |

---

## Entidade: **Espingarda Serrada**

**Descrição:** Subentidade de armas de fogo.

| Nome Variável     | Tipo       | Descrição                              | Valores Permitidos | Permite Valores Nulos? | É Chave? |
|-------------------|------------|----------------------------------------|--------------------|------------------------|----------|
| id_Espingarda_Serrada          | INT        | Identificador único do item (herdado) | 1-1000             | não                    | FK   |
| dano_extra_curto  | INT        | Dano adicional em curtas distâncias    | 1-50               | sim                    | -        |

---

## Entidade: **Colt .45**

**Descrição:** Subentidade de arma de fogo.

| Nome Variável     | Tipo       | Descrição                              | Valores Permitidos | Permite Valores Nulos? | É Chave? |
|-------------------|------------|----------------------------------------|--------------------|------------------------|----------|
| id_Colt_45           | INT        | Identificador único do item (herdado) | 1-1000             | não                    | FK  |

---

## Entidade: **Rifle**

**Descrição:** Subentidade de arma.

| Nome Variável     | Tipo       | Descrição                              | Valores Permitidos | Permite Valores Nulos? | É Chave? |
|-------------------|------------|----------------------------------------|--------------------|------------------------|----------|
| id_rifle          | INT        | Identificador único do item (herdado) | 1-1000             | não                    | FK  |
| perfuração       | INT        | Quantidade de dano adicional a depender da armadura             | 1-200              | não                    | -        |

---

## Entidade: **Revolver**

**Descrição:** Subentidade de arma.

| Nome Variável     | Tipo       | Descrição                              | Valores Permitidos | Permite Valores Nulos? | É Chave? |
|-------------------|------------|----------------------------------------|--------------------|------------------------|----------|
| id_revolver           | INT        | Identificador único do item (herdado) | 1-1000             | não                    | FK  |

---

## Entidade: **Pistola Derringer**

**Descrição:** Subentidade de arma.

| Nome Variável     | Tipo       | Descrição                              | Valores Permitidos | Permite Valores Nulos? | É Chave? |
|-------------------|------------|----------------------------------------|--------------------|------------------------|----------|
| id_pistola           | INT        | Identificador único do item (herdado) | 1-1000             | não                    | FK  |

---

## Histórico de Versão

| Versão |    Data    |                     Descrição                     |                                                                                                Autor(es)                                                                                                 |
| :----: | :--------: | :-----------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| `1.0`  | 23/11/2024 | Primeira versão do Dicionário de Dados | [Brenno da Silva](https://github.com/brenno-silva01) |                                                |
| `2.0`  | 23/11/2024 | Adicionando Entidades NPC e Inventário | [Brenno da Silva](https://github.com/brenno-silva01) |                                                |
| `2.1`  | 23/11/2024 | Atualizando alguns atributos e seus nomes | [Brenno da Silva](https://github.com/brenno-silva01) |                                                |
| `2.2`  | 25/11/2024 | Adicionando alguns atributos e modificando o nome de outros | [Brenno da Silva](https://github.com/brenno-silva01) |                                                |
| `3.0`  | 25/11/2024 | Atualizando o dicionário com base no último DER| [Daniel Sousa](https://github.com/daniel-de-sousa) |                                                |