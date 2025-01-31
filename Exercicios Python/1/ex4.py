'''Certa substância se decompõe, aproximadamente, segundo a equação Q(t) =
K*2^(-0.5t). Nessa equação, K é uma constante, t indica o tempo em minutos e Q(t)
indica a quantidade da substância, em gramas, no instante t. Considerando-se que
Q(t) é 2048 quando t = 2, qual é o valor de K?'''

K = 2048/(2**(-0.5*2))

print(K)