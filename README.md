# Nand2Tetris Capstone Project

**Student:** Bhavya  
**Roll Number:** 2501350086  
**University:** K.R. Mangalam University

## Project Overview

This capstone project is based on the Nand2Tetris course. It focuses on building a Hack Computer using HDL and developing a two-pass Python Assembler that converts Hack Assembly programs (`.asm`) into machine code (`.hack`).

The project includes CPU, Memory, and Computer components, assembler testing with Add, Max, Rect, and Pong programs, and duplicate-label detection as an additional assembler feature.

The Box Drawing Program displays a black rectangle of **48 pixels width and 20 rows height**, starting at row **86**, while a keyboard key is pressed, and clears it when the key is released.

## Technologies Used

- HDL
- Hack Assembly
- Python
- Nand2Tetris Hardware Simulator
- CPU Emulator

## Project Structure

```text
Your-Lab-Repository/
├── README.md
└── capstone/
    ├── Add.asm
    ├── Add.hack
    ├── Box.asm
    ├── Box.hack
    ├── Computer.hdl
    ├── CPU.hdl
    ├── Memory.hdl
    ├── assembler.py
    ├── Max.asm
    ├── Max.hack
    ├── Rect.asm
    ├── Rect.hack
    ├── Pong.asm
    ├── Pong.hack
    ├── DuplicateTest.asm
    ├── DuplicateTest.hack
    └── Proof/
        └── (screenshots and image evidence)
```

## Capstone Proof / Screenshots

All proof images are embedded below and stored in `capstone/Proof/`.

### Screenshot 2026-11-20 204218

![Screenshot 2026-11-20 204218.png](<capstone/Proof/Screenshot 2026-11-20 204218.png>)

### WhatsApp Image 2026-11-22 at 9.03.26 PM

![WhatsApp Image 2026-11-22 at 9.03.26 PM.jpeg](<capstone/Proof/WhatsApp Image 2026-11-22 at 9.03.26 PM.jpeg>)

### WhatsApp Image 2026-11-22 at 9.03.51 PM

![WhatsApp Image 2026-11-22 at 9.03.51 PM.jpeg](<capstone/Proof/WhatsApp Image 2026-11-22 at 9.03.51 PM.jpeg>)

### WhatsApp Image 2026-11-22 at 9.04.02 PM

![WhatsApp Image 2026-11-22 at 9.04.02 PM.jpeg](<capstone/Proof/WhatsApp Image 2026-11-22 at 9.04.02 PM.jpeg>)

### WhatsApp Image 2026-11-22 at 9.04.25 PM

![WhatsApp Image 2026-11-22 at 9.04.25 PM.jpeg](<capstone/Proof/WhatsApp Image 2026-11-22 at 9.04.25 PM.jpeg>)

### WhatsApp Image 2026-11-22 at 9.04.36 PM

![WhatsApp Image 2026-11-22 at 9.04.36 PM.jpeg](<capstone/Proof/WhatsApp Image 2026-11-22 at 9.04.36 PM.jpeg>)

### WhatsApp Image 2026-11-22 at 9.04.46 PM

![WhatsApp Image 2026-11-22 at 9.04.46 PM.jpeg](<capstone/Proof/WhatsApp Image 2026-11-22 at 9.04.46 PM.jpeg>)

### WhatsApp Image 2026-11-22 at 9.04.54 PM

![WhatsApp Image 2026-11-22 at 9.04.54 PM.jpeg](<capstone/Proof/WhatsApp Image 2026-11-22 at 9.04.54 PM.jpeg>)

### WhatsApp Image 2026-11-22 at 9.05.07 PM

![WhatsApp Image 2026-11-22 at 9.05.07 PM.jpeg](<capstone/Proof/WhatsApp Image 2026-11-22 at 9.05.07 PM.jpeg>)

### WhatsApp Image 2026-11-22 at 9.05.16 PM

![WhatsApp Image 2026-11-22 at 9.05.16 PM.jpeg](<capstone/Proof/WhatsApp Image 2026-11-22 at 9.05.16 PM.jpeg>)

### WhatsApp Image 2026-11-22 at 9.05.56 PM

![WhatsApp Image 2026-11-22 at 9.05.56 PM.jpeg](<capstone/Proof/WhatsApp Image 2026-11-22 at 9.05.56 PM.jpeg>)

## Assembler

Run the assembler from the `capstone` directory:

```bash
python assembler.py Add.asm
```

Use another `.asm` file name to assemble a different program. The generated machine-code file uses the `.hack` extension.

## Notes

- The `.asm` files contain Hack Assembly source programs.
- The `.hack` files contain the corresponding machine-code output.
- HDL files describe the Hack Computer hardware components.
- The `Proof/` folder contains the project screenshots supplied with this repository.
