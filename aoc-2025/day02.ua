# Horrible solution not using any forks, many dips

Parsed   ← ⊜(⊜⋕⊸≠@-)⊸≠@, ⊏⊚⊸≠@\n &fras "day02.in"
Range    ← +⊙(⇡+1)⟜-
IsDouble ← ≍°⊟⬚(¯1)↯⊂2⌈÷2⊢⊸△ ⊥10
/+≡(/+⊏⊚⊸(≡IsDouble)∘°□)≡(□Range°⊟)Parsed

# [IsMultiple 4 123123123123] checks if substr repeats 4 times in 123123123123
IsMultiple ← ≍ ˜↯ ⊸⊙△⊢⟜∘ ↯⊂⟜÷ ⊙(⊢⊸△⊥10)

# Divisors 10 = [2 5 10]
Divisors ← ↘1÷⊏⊚⊸=⌊⟜∘÷↘1⊸(⇡+1) ⟜∘

IsSolution ← >0/+≡(IsMultiple) Divisors ⧻⊥ 10 ⟜∘

/+≡(/+⊏⊚⊸(≡IsSolution)∘°□)≡(□Range°⊟)Parsed
