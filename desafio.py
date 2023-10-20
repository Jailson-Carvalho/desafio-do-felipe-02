vitorias = 6
derrotas = 5


def pontuacao(vitorias, derrotas):
    if vitorias - derrotas <= 10:
        print(f"O Herói tem saldo de  {vitorias - derrotas}, está no nível: Ferro")


pontuacao(vitorias, derrotas)


def pontuacao(vitorias, derrotas):
    if vitorias - derrotas >= 11 and vitorias - derrotas <= 20:
        print(f"O Herói tem saldo de  {vitorias - derrotas}, está no nível: Bronze")


pontuacao(vitorias, derrotas)


def pontuacao(vitorias, derrotas):
    if vitorias - derrotas >= 21 and vitorias - derrotas <= 50:
        print(f"O Herói tem saldo de  {vitorias - derrotas}, está no nível: Prata")


pontuacao(vitorias, derrotas)


def pontuacao(vitorias, derrotas):
    if vitorias - derrotas >= 51 and vitorias - derrotas <= 80:
        print(f"O Herói tem saldo de  {vitorias - derrotas}, está no nível: Ouro")


pontuacao(vitorias, derrotas)


def pontuacao(vitorias, derrotas):
    if vitorias - derrotas >= 81 and vitorias - derrotas <= 90:
        print(
            f"O Herói tem saldo de  {vitorias - derrotas}, está no nível: Diamante"
        )


pontuacao(vitorias, derrotas)


def pontuacao(vitorias, derrotas):
    if vitorias - derrotas >= 91 and vitorias - derrotas <= 100:
        print(f"O Herói tem saldo de {vitorias - derrotas}, está no nível: Lendário")


pontuacao(vitorias, derrotas)


def pontuacao(vitorias, derrotas):
    if vitorias - derrotas >= 101:
        print(f"O Herói tem saldo de  {vitorias - derrotas}, está no nível: Imortal")


pontuacao(vitorias, derrotas)