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