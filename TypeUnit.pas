unit TypeUnit;

interface

type TTypePiece = (Roi, Reine, Tour, Fou, Cavalier, Pion);

type TCouleur = (Blanc, Noir);

type TCase = 
    record
        lettre: char;
        chiffre: integer;
        couleur: TCouleur;
        occupee: boolean;
        id_piece: integer;
    end;

type TPiece =
    record
        id: integer;
        couleur: TCouleur;
        type_piece: TTypePiece;
        position: TCase;
        deplacee: boolean;
    end;

type TPlateau = array[1..8, 'a'..'h'] of TCase;

type TPieceMangee = array[1..32] of TPiece;

implementation

end.