Parse   ← ⊜(="@")⊸≠"\n"
Border  ← ⍉⊂⊂0⍉⊂0⊂⊙(0 0)              # Adds border of 0s
Movable ← × ⊃(=1|<5 ⧈(⧻⊚) 3_3 Border) # Check if cell is 1 and sum of neighbors < 4

Part₁ ← ⧻⊚ Movable
Part₂ ← ⧻⊚ - ⊃(⍥(-⊸Movable)∞|∘) # Fixed point iteration

Data ← Parse &fras "day04.in"
Part₁ Data
Part₂ Data
