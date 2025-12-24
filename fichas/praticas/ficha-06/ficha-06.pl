% ficha-06.pl

% base de conhecimento

% geração 1 (tetravós)
filho(manuel, antonio).
filho(ana, antonio).

filho(maria, joaquim).
filho(jose, joaquim).

% geração 2 (bisavós)
filho(carlos, manuel).
filho(luisa, manuel).

filho(helena, ana).
filho(rui, ana).

filho(paulo, maria).
filho(sara, maria).

filho(fernando, jose).
filho(clara, jose).

% geração 3 (avós)
filho(pedro, carlos).
filho(ines, carlos).

filho(sofia, luisa).

filho(bruno, helena).
filho(rita, rui).

filho(miguel, paulo).
filho(diana, sara).

filho(tiago, fernando).
filho(beatriz, clara).

% geração 4 (pais / filhos)
filho(joao, pedro).
filho(laura, pedro).

filho(marco, ines).

filho(tomas, miguel).
filho(catarina, diana).

filho(andre, tiago).
filho(ines2, beatriz).


% regras

pai(P,F) :- filho(F,P).

avo(A,N) :- filho(N,X), pai(A,X).

neto(N,A) :- avo(A,N).

descendente(X,Y) :- filho(X,Y).
descendente(X,Y) :- filho(X,P), descendente(P,Y).

grau(X,Y,1) :- filho(X,Y).
grau(X,Y,G) :- filho(X,P), grau(P,Y,G1), G is G1 + 1.

avoG(A,N) :- grau(N,A,2).

bisavo(X,Y) :- grau(Y,X,3).

trisavo(X,Y) :- grau(Y,X,4).

tetraneto(X,Y) :- grau(X,Y,4).

