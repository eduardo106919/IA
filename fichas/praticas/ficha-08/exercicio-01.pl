% exercicio-01.pl

% base de conhecimento

% aluno(id,nome,genero)
aluno(1,joao,m).
aluno(2,antonio,m).
aluno(3,carlos,m).
aluno(4,luisa,f).
aluno(5,maria,f).
aluno(6,isabel,f).

% curso(id,sigla)
curso(1,lei).
curso(2,miei).
curso(3,lcc).

% disciplina(cod,sigla,ano,curso)
disciplina(1,ed,2,1).
disciplina(2,ia,3,1).
disciplina(3,fp,1,2).

% inscrito(aluno,disciplina)
inscrito(1,1).
inscrito(1,2).
inscrito(5,3).
inscrito(5,5).
inscrito(2,5).

% nota(aluno,disciplina,nota)
nota(1,1,15).
nota(1,2,16).
nota(1,5,20).
nota(2,5,10).
nota(3,5,8).

% copia(id_aluno,id_aluno)
copia(1,2).
copia(2,3).
copia(3,4).


% regras

naoInscritos(L) :- findall(Nome, ( aluno(N,Nome,_), not(inscrito(N,_)) ), L).

inscricoesValidas(N) :- inscrito(N,D), disciplina(D,_,_,_).

naoInscritos2(L) :- findall(Nome, ( aluno(N,Nome,_), not(inscricoesValidas(N)) ), L).

comprimento([],0).
comprimento([_|T],C) :- comprimento(T,C1), C is C1+1.

somaL([],0).
somaL([H|T],S) :- somaL(T,S1), S is H+S1.

media(L,M) :- comprimento(L,C), somaL(L,S), M is S / C.

mediaAluno(N,M) :- findall(Nota, nota(N,_,Nota) , L), L \= [], media(L,M).

mediaGlobal(G) :- findall(Nota, nota(_,_,Nota), L), media(L,G).

alunosAcimaMedia(L) :- findall(Nome, ( aluno(N,Nome,_), mediaGlobal(G), mediaAluno(N,M), M > G ), L).

alunosCopiaram(L) :- findall(Nome, ( aluno(N,Nome,_), copia(N,_) ), L).

copias(X,Y) :- copia(X,Y).
copias(X,Y) :- copia(X,W), copias(W,Y).

copiaDirIndir(X,L) :- findall(Nome, ( aluno(N,Nome,_), copias(N,X) ), L).

mapToNome([],[]).
mapToNome([ID|T],[Nome|Ns]) :- aluno(ID,Nome,_), mapToNome(T,Ns).
mapToNome([_|T],Ns) :- mapToNome(T,Ns).
