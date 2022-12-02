from sympy import *


def calcIDH(EV, AME, AEE, PIBpc):
    EV = int(EV)
    AME = int(AME)
    AEE = int(AEE)
    PIBpc = int(PIBpc)

    IEV = (EV - 20) / (83.4 - 20)  # Indice de expectativa de vida.

    IAME = AME / 13.2  # Anos médios de escolaridade (quantidade de anos em que um adulto de 25 anos frequentou escolas)
    IAEE = AEE / 20.6  # Anos esperados de escolaridade (quantidade de anos em que uma criança de 5 anos frequentará escolas)
    IE = sqrt(IAME * IAEE) / 0.951

    IR = ln(PIBpc) - log(163) / ln(108.211) - ln(163)  # Indice de Renda

    IDH = N(cbrt(IEV * IE * IR))

    IEV = N(IEV)
    IE = N(IE)
    IR = N(IR)

    return IDH, IEV, IE, IR
