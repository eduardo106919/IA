
% parte 02

pertence( X,[X|L] ).
pertence( X,[Y|L] ) :-
    X \= Y,
    pertence( X,L ).

comprimento([],0) :- !.
comprimento([_|T],C) :- comprimento(T,C1), C is C1+1.

diferentes([],0).
diferentes([H|T],D) :- pertence(H,T), diferentes(T,D).
diferentes([_|T],D) :- diferentes(T,D1), D is D1+1.

apaga1(_,[],[]).
apaga1(X,[X|T],T).
apaga1(X,[H|T],L) :- apaga1(X,T,L1), L = [H|L1].

apagaT(_,[],[]).
apagaT(X,[X|T],L) :- apagaT(X,T,L).
apagaT(X,[H|T],L) :- apagaT(X,T,L1), L = [H|L1].

adicionar(X,L,L) :- pertence(X,L).
adicionar(X,L,[X|L]).

concatenar([],L,L).
concatenar([H|T],L,C) :- concatenar(T,L,C1), C = [H|C1].

inverter([],[]).
inverter([H|T],L) :- inverter(T,L1), concatenar(L1,[H],L).

sublista(S,L) :- concatenar(L1,L2,L), concatenar(S,L3,L2).


