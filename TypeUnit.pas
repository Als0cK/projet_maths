unit TypeUnit;

interface

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
        type_piece: string;
        position: TCase;
        deplacee: boolean;
    end;

type TPlateau = array[1..8, 'a'..'h'] of TCase;



implementation

end.
