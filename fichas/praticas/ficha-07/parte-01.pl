% ficha-07.pl

% parte 01

soma(X,Y,Z,S) :- S is X+Y+Z.

somaL([],0) :- !.
somaL([H|T],S) :- somaL(T,S1), S is H+S1.

maximo(X,Y,X) :- X > Y.
maximo(X,Y,Y) :- X =< Y.

maximoL([X],X) :- !.
maximoL([H|T],M) :- maximoL(T,M1), maximo(M1,H,M).

comprimento([],0) :- !.
comprimento([_|T],C) :- comprimento(T,C1), C is C1+1.

media(L,M) :- comprimento(L,C), somaL(L,S), M is S / C.

insere(X,[],[X]) :- !.
insere(X,[H|T],[X,H|T]) :- X =< H.
insere(X,[H|T],S) :- insere(X,T,S1), S = [H|S1].

ordena([],[]) :- !.
ordena([H|T],S) :- ordena(T,S1), insere(H,S1,S).

par(X,true) :- 0 is X mod 2, !.
par(_,false).

