#Exercício 7:
#Elabora um programa que pede ao utilizador que
#lhe forneça um inteiro correspondente a um
#número de segundos e calcula o numero de dia,
#horas, min e segundos correspondentes
#a esse número de segundos

segs = int (input ("Qual o número de segundos?"))

#converter para dias
dias = segs // 86400
#dias=segs // (24*60*60)
segs_aux=segs%86400

#converter para horas
horas = segs_aux // 3600
#horas=segs // (60*60)
segs_aux % 3600

#converter para minutos
minutos = segs_aux //60
segs_aux % 60

print("dias:", dias, "horas:", horas, "minutos:", minutos, "segs:", segs_aux)



