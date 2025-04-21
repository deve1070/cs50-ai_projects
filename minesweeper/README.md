# Minesweeper AI

This project implements an AI agent that plays the game of Minesweeper using logical reasoning. The AI uses a knowledge base to make safe moves and identify where mines are located on the board.

---

##  Project Overview

The classic Minesweeper game is played on a grid with hidden mines. The player must uncover all safe cells without detonating a mine. This AI attempts to play optimally by:
- Marking known mines
- Making safe moves
- Inferring new knowledge from existing known facts

---

## AI Concepts Used

- **Propositional Logic**
- **Inference Rules**
- **Knowledge Base** with logical sentences (like "these 3 cells contain 1 mine")
- **Constraint Propagation** to deduce safe/mine cells

---

## Project Files

- `minesweeper.py` — Contains the game logic, board structure, and AI agent
- `runner.py` — Runs the AI through random boards and outputs its moves

---

## ▶ How to Run

```bash
python runner.py
