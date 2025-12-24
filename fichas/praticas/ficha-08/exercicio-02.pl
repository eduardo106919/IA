% exercicio-02.pl

% base de conhecimento

% biblioteca(id, nome, localidade)
biblioteca(1, uminhogeral, braga).
biblioteca(2, luciocracveiro, braga).
biblioteca(3, municipal, porto).
biblioteca(4, publica, viana).
biblioteca(5, ajuda, lisboa).
biblioteca(6, cidade, coimbra).


% livros( id, nome, biblioteca)
livros(1, gameofthrones, 1). 
livros(2, codigodavinci, 2).
livros(3, setimoselo, 1).
livros(4, fireblood, 4).
livros(5, harrypotter, 6).
livros(6, senhoradosneis, 7).
livros(7, oalgoritmomestre, 9).

% leitores(id, nome, genero)
leitores(1, pedro, m).
leitores(2, joao, m).
leitores(3, lucia, f).
leitores(4, sofia, f).
leitores(5, patricia, f).
leitores(6, diana, f).

% requisicoes(id_requisicao,id_leitor, id_livro, data(A,M,D)
requisicoes(1,2,3,data(2022,5,17)).
requisicoes(2,1,2,data(2022,7,10)).
requisicoes(3,1,3,data(2021,11,2)).
requisicoes(4,1,4,data(2022,2,1)).
requisicoes(5,5,3,data(2022,4,23)).
requisicoes(6,4,2,data(2021,3,9)).
requisicoes(7,4,1,data(2022,5,5)).
requisicoes(8,2,6,data(2021,7,18)).
requisicoes(9,5,7,data(2022,4,12)).

% devolucoes(id_requisicao, data(A,M, D))
devolucoes(2, data(2022, 7, 26)).
devolucoes(4, data(2022, 2, 4)).
devolucoes(5, data(2022, 6, 13)).
devolucoes(1, data(2022, 5, 23)).
devolucoes(6, data(2022, 4, 9)).


% regras

comprimento([],0).
comprimento([_|T],N) :- comprimento(T,N1), N is N1+1.

leitoras(N) :- findall(ID, leitores(ID,_,f), L), comprimento(L,N).

livrosInvalidos(L) :- findall(Nome, ( requisicoes(_,_,IDL,_), livros(IDL,Nome,B), not(biblioteca(B,_,_)) ) , L).

livrosLeitoresBraga(L) :- findall((Livro,Nome), ( requisicoes(_,IDN,IDL,_), leitores(IDN,Nome,_), livros(IDL,Livro,B), biblioteca(B,_,braga) ), L).

livrosNaoRequisitados(L) :- findall(Nome, (livros(IDL,Nome,_), not(requisicoes(_,_,IDL,_))), L).

livrosRequisitados2022(L) :- findall((Nome,data(2022,M,D)), ( requisicoes(_,_,IDL,data(2022,M,D)), livros(IDL,Nome,_) ), L).

requisicoesVerao(L) :- findall(Nome, ( requisicoes(_,IDL,_,data(_,M,_)), M > 6, M < 10, leitores(IDL,Nome,_)), L).

% apenas verifica no mesmo mes
datasValidas(data(A,M,D1),data(A,M,D2)) :- D2 > D1, D2 =< D1+15.

devolucoesValidas(L) :- findall(Nome, ( devolucoes(IDR,DD), requisicoes(IDR,IDL,_,DR), datasValidas(DR,DD), leitores(IDL,Nome,_) ), L).
