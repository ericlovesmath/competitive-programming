Data ← &fras "day06.in"

Parsed₁ ← ⍉⊜(⊜(⍣⋕(⊢=@*))⊸≠@ )⊸≠@\nData
/+≡(⨬/+/×⊸⊣) Parsed₁

Parsed₂ ← ⊜□>0≡/+⊸≠@ ⇌⍉⊜∘⊸≠@\nData
°□/+⍚(⨬(/+)(/×)=@*⊃(⊣⊣|≡(⋕▽⊸≠@ ↙)-1⊣⊸△)) Parsed₂

# A not super fun string parsing day :(
