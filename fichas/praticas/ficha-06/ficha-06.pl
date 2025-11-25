% ficha-06.pl

% predicado filho: Filho,Pai -> {V,F}

filho(joao,jose).
filho(jose,manuel).
filho(carlos,jose).
filho(manuel,diogo).
filho(marco,diogo).
filho(tiago,joao).

% predicado pai: Pai,Filho -> {V,F}

pai(P,F) :- filho(F,P).

% predicado avo: Avo,Neto -> {V,F}

avo(A,N) :- filho(N, X), pai(A,X).

% predicado neto: Neto,Avo -> {V,F}

neto(N,A) :- avo(A, N).

% predicado bisavo: Bisavo,Bisneto -> {V,F}

bisavo(B,N) :- avo(B,X), pai(X,N).

% predicado bisneto: Bisneto,Bisavo -> {V,F}

bisneto(N,B) :- bisavo(B,N).

% predicado descendente: Descendente,Ascendente -> {V,F}

descendente(X,Y) :- filho(X,Y).
descendente(X,Y) :- filho(X,A), descendente(A,Y).

% predicado ascendente: Ascendente,Descendente -> {V,F}

ascendente(X,Y) :- pai(X,Y).
ascendente(X,Y) :- pai(X,A), ascendente(A,Y).

% predicado grau: Descendente,Ascendente,Grau -> {V,F}

grau(X,Y,1) :- filho(X,Y).
grau(X,Y,G) :- filho(X,A), grau(A,Y,G1), G is G1 + 1.

% predicado avograu: Avo,Neto -> {V,F}
% atraves do predicado grau

avograu(A,N) :- grau(N,A,2).

% predicado bisavograu: Bisavo,BisNeto -> {V,F}
% atraves do predicado grau

bisavograu(B,N) :- grau(N,B,3).

% predicado trisavo: Trisavo,TrisNeto -> {V,F}
% atraves do predicado grau

trisavo(T,N) :- grau(N,T,4).

% predicado tetraneto: Tetraneto,TetraAvo -> {V,F}
% atraves do predicado grau

tetraneto(N,T) :- grau(N,T,5).
