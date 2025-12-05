Data    ← =@@⊜∘⊸≠@\n &fras "day04.in"
Pad     ← ⌝↘¯⟜⌝↘1_1               # Pads border of 0s
Movable ← ×⊃(=1|<5 ⧈(⧻⊚) 3_3 Pad) # Check if cell is 1 and sum of neighbors < 4

Part₁ ← ⧻⊚ Movable
Part₂ ← ⧻⊚ - ⊃(⍥(-⊸Movable)∞|∘) # Fixed point iteration

Part₁ Data
Part₂ Data
