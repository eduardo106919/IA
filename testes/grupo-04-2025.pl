% grupo-04-2025.pl

% base de conhecimento

% filmes(id_f, nome, tipo, rating)
filmes(1, 'Dragões Furiosos', 	  'Ação', 			   3.5).
filmes(2, 'Infinito', 			  'Romance', 		   4.0).
filmes(3, 'Lua e Marte',          'Ficção Científica', 3.0).
filmes(4, 'Perdidos na Rua',      'Comédia',           2.8).
filmes(5, 'Aventura no Deserto',  'Romance',           1.9).
filmes(6, 'Babysitter',           'Comédia', 		   4.7).
filmes(7, 'Cavaleiro Intemporal', 'Aventura', 		   3.9).
filmes(8, 'Isto é demais',        'Comédia', 		   3.3).

% clientes(id_c, nome, idade)
clientes(1, 'Maria',   32).
clientes(2, 'José',    46).
clientes(3, 'Mariana', 40).
clientes(4, 'João',    23).
clientes(5, 'Miguel',  52).
clientes(6, 'Débora',  49).

% requisicoes(id_c, id_f, data, preco)
requisicoes(2, 4, data(11, 02, 2022), 3.60).
requisicoes(6, 6, data(24, 07, 2022), 5.00).
requisicoes(1, 7, data(08, 11, 2023), 3.80).
requisicoes(4, 3, data(03, 08, 2022), 2.90).
requisicoes(3, 1, data(01, 04, 2022), 3.60).


% regras

% quantos filmes existem do tipo comédia

comprimento([],0).
comprimento([_|T],N) :- comprimento(T,N1), N is N1+1.

nrComedias(N) :- findall(_, filmes(_,_,'Comédia',_), L), comprimento(L,N).

% quais os nomes dos filmes requisitados com rating superior a 3

filmesS3(L) :- findall(Nome, ( filmes(IDF, Nome, _, R), R > 3, requisicoes(_,IDF,_,_) ), L).

% que clientes requisitaram filmes em 2022 com um preço superior a 3,50€ e com idade superior a 40 anos

clientesS40(L) :- findall(Nome, ( requisicoes(IDC,_,data(_,_,2022),P), P > 3.5, clientes(IDC,Nome,I), I > 40 ), L).

