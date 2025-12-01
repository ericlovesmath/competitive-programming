# PARSING

Data    ← ⊜□⊸≠ "\n" &fras "day01.in"
Signs   ← ≡(-1×2=@R⊢°□)Data
Numbers ← ≡(⋕↘1°□)Data
Parsed  ← × Signs Numbers

# PART 1

Zeros ← /+=0
Zeros \(◿100+) ⊂50 Parsed

# PART 2

Range  ← +⊙⇡⊸>0
Split  ← ⊙⊣⊢⟜∘
Folder ← ⊂⊣ ⊙(+Zeros) ⟜∘ ◿100 +Range ⊙Split
⊣ ∧Folder Parsed [50 0]

# NOTES

# °□ = unbox, ≡ = map
# Data: Reads and split by newline
# Signs: map (head = "R" ? 1 : -1)
# Numbers: Drops "L" and "R" and parses ints
# Part 1: count -. scanl (mod 100 . +) . cons 50
# Range: Range, but both positive and negative numbers start at 1 and -1
# Split: [a b] -> a b
# Folder: Given [a b], a is the sum acc while b is the 0-count acc
# - We generate the whole range every rotation and count the zeros
