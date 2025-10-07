unit TypeUnit;

interface

type
  TPieceType = (Vide, Roi, Dame, Tour, Fou, Cavalier, Pion);
  TCouleur = (Aucun, Blanc, Noir);

  TCase = record
    Piece: TPieceType;
    Couleur: TCouleur;
  end;

  TPosition = record
    Ligne: Integer; // 1..8
    Colonne: Integer; // 1..8
  end;

  TPlateau = array[1..8, 1..8] of TCase;

implementation

end.
