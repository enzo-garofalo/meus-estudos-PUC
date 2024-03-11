
print(f"Múltiplos de sete entre 100 e 450!\n")
i = 100

while i <= 450:
    if i % 7 == 0:    
        print(f"\t7 x {i//7} = {i}")
        i += 1
    else:
        i += 1