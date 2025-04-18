# Knights and Knaves

This project explores logical reasoning by solving logic puzzles involving a fictional island with two types of people: **Knights**, who always tell the truth, and **Knaves**, who always lie.

## 🧩 Problem Overview

Each puzzle presents a scenario where inhabitants make statements. The goal is to determine, using propositional logic, who is a knight and who is a knave based on what they say.

For example:
- A says: "We are both knaves."
  - If A were telling the truth, then A is a knight — but then the statement would be false, creating a contradiction.

## 🧠 AI Concept

This project uses **propositional logic** and **model checking**:
- Each character's identity is encoded as logical symbols.
- The program builds a **knowledge base (KB)** for each puzzle.
- It then checks all models to determine which symbols must be true.

## 📄 Project Files

- `logic.py` — Defines the basic logical constructs like `Symbol`, `And`, `Or`, etc.
- `puzzle.py` — Contains the actual puzzle definitions and uses `model_checking` to solve them.

## ▶️ How to Run

```bash
python puzzle.py
