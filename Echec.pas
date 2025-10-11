program Echec;

uses TypeUnit;
uses Initialisation;
uses Affichage;


var 
    Plateau: TPlateau;
    Pieces: array[1..32] of TPiece;
    PiecesMangees: TPieceMangee;
    nbPiecesMangees: integer;
  

begin
  AfficherPlateau(Plateau);
  AfficherPiecesMangees(PiecesMangees, nbPiecesMangees);
end.