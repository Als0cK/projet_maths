unit AffichageUnit;


interface

uses TypeUnit;
uses Initialisation;

procedure AfficherPlateau(Plateau: TPlateau);
procedure AfficherPiecesMangees(PiecesMangees: TPieceMangee; nbPiecesMangees: integer);


implementation

procedure AfficherPlateau(Plateau: TPlateau);
    var
        i, j: integer;
    begin
        writeln('  a b c d e f g h');
        writeln(' +-----------------+');
        for i := 8 downto 1 do
        begin
            write(i, '|');
            for j := ord('a') to ord('h') do
            begin
                if Plateau[i][chr(j)].occupee then
                begin
                    case Plateau[i][chr(j)].id_piece of
                        1: write('♜ ');
                        2: write('♞ ');
                        3: write('♝ ');
                        4: write('♚ ');
                        5: write('♛ ');
                        6: write('♝ ');
                        7: write('♞ ');
                        8: write('♜ ');
                        9..16: write('♟ ');
                        17..24: write('♙ ');
                        25: write('♖ ');
                        26: write('♘ ');
                        27: write('♗ ');
                        28: write('♔ ');
                        29: write('♕ ');
                        30: write('♗ ');
                        31: write('♘ ');
                        32: write('♖ ');
                    end;
                end
                else
                begin
                    if (i + j - ord('a')) mod 2 = 0 then
                        write('□ ')
                    else
                        write('■ ');
                end;
            end;
            writeln('|', i);
        end;
        writeln(' +-----------------+');
        writeln('  a b c d e f g h');
    end;

procedure AfficherPiecesMangees(PiecesMangees: TPieceMangee; nbPiecesMangees: integer);
    var
        i: integer;
    begin
        writeln('Pièces mangées :');
        for i := 1 to nbPiecesMangees do
        begin
            write(PiecesMangees[i].nom, ' ');
        end;
        writeln;
    end;

end.