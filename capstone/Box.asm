// Box Program - Nand2Tetris Capstone
// K = 86
// Starting row = 86
// Height = 20 rows
// Width = 48 pixels (3 words per row)

(START)
    // Check keyboard
    @KBD
    D=M
    @CLEAR
    D;JEQ

    // Key pressed: black color
    @R3
    M=-1
    @DRAW
    0;JMP

(CLEAR)
    // Key released: white color
    @R3
    M=0

(DRAW)
    // Starting screen address = SCREEN + 32*86 = 19136
    @19136
    D=A
    @R0
    M=D

    // 20 rows
    @20
    D=A
    @R1
    M=D

(ROW)
    // 3 words = 48 pixels
    @3
    D=A
    @R2
    M=D

(WORD)
    // Write black or white word
    @R3
    D=M
    @R0
    A=M
    M=D

    // Next screen word
    @R0
    M=M+1

    // Decrease word counter
    @R2
    MD=M-1
    @WORD
    D;JGT

    // Move to next screen row (32 - 3 = 29)
    @29
    D=A
    @R0
    M=D+M

    // Decrease row counter
    @R1
    MD=M-1
    @ROW
    D;JGT

    // Check keyboard again
    @START
    0;JMP
