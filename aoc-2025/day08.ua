# We love Union-Find with path compression

Parsed  ← ⋕°csv &fras "day08.in"       # Raw data
Sorted  ← ⊏⊃(⍏≡(/+ⁿ2/-)|˜⨂)⊸⧅₂< Parsed # Indicies of points, sorted by distance
Merge   ← ⍜⊏(◌≡⊙∘) ⊸(⊚∊⊸⊏) ⟜⤙(/↧⊏)     # (Merge [a b] parents) adds edge [a b] to parents list
Unequal ← ≠0/+≠⊸⊢                      # Check if list has unequal elements

# Part 1: Union-Find on first 1000 edges, then get 3 largest components
/×↙¯3⍆°⊚⊛ ∧Merge ↙1000Sorted ⇡⧻Parsed

# Part 2: Union-Find until 1 component, then get last added edge and multiply their x-coords
/×≡⊢˜⊏Parsed ⊢⊙◌⍢(⊙Merge˜⊙∘⊸⊢↻₁|⋅Unequal) Sorted ⇡⧻Parsed
