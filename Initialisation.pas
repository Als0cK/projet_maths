unit Initialisation

interface

uses TypeUnit;

procedure InitialiserPlateau(var Plateau: TPlateau);
procedure InitialiserPieces(var Pieces: array of TPiece; var Plateau: TPlateau);

implementation

procedure InitialiserPlateau(var Plateau: TPlateau);
    var
        i, j: integer;
        couleur_case: string;

    begin
    for i := 0 to High(Plateau) do
    begin
        for j := 0 to High(Plateau[i]) do
        begin
        if (i + j) mod 2 = 0 then
            couleur_case := '□'
        else
            couleur_case := '■';

        Plateau[i][j] := couleur_case;
        end;
    end;
end;

procedure InitialiserPieces(var Pieces: array of TPiece; var Plateau: TPlateau);
    var
        i: integer;
    begin
        Plateau[1]['a'] := '♜';
        Plateau[1]['b'] := '♞';
        Plateau[1]['c'] := '♝';
        Plateau[1]['d'] := '♚';
        Plateau[1]['e'] := '♛';
        Plateau[1]['f'] := '♝';
        Plateau[1]['g'] := '♞';
        Plateau[1]['h'] := '♜';
        for i := 1 to 8 do
            Plateau[2][chr(ord('a') + i - 1)] := '♟';
        for i := 1 to 8 do
            Plateau[7][chr(ord('a') + i - 1)] := '♙';
        Plateau[8]['a'] := '♖';
        Plateau[8]['b'] := '♘';
        Plateau[8]['c'] := '♗';
        Plateau[8]['d'] := '♔';
        Plateau[8]['e'] := '♕';
        Plateau[8]['f'] := '♗';
        Plateau[8]['g'] := '♘';
        Plateau[8]['h'] := '♖';
    end;

end.