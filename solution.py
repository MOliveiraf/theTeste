def seven_segmentify(time):
    segments = {
        '0': [" _ ", "| |", "|_|"],
        '1': ["   ", "  |", "  |"],
        '2': [" _ ", " _|", "|_ "],
        '3': [" _ ", " _|", " _|"],
        '4': ["   ", "|_|", "  |"],
        '5': [" _ ", "|_ ", " _|"],
        '6': [" _ ", "|_ ", "|_|"],
        '7': [" _ ", "  |", "  |"],
        '8': [" _ ", "|_|", "|_|"],
        '9': [" _ ", "|_|", " _|"],
        ':': ["   ", " . ", "   "],
        ' ': ["   ", "   ", "   "]  # Espaço em branco para suportar '0' à esquerda nas horas
    }

    # Separar horas e minutos
    hours, minutes = time.split(':')

    # Substituir '0' inicial em horas por espaço em branco para manter o formato
    if hours[0] == '0':
        hours = ' ' + hours[1]

    # Construção das três linhas
    line1 = ""
    line2 = ""
    line3 = ""

    for char in hours + ':' + minutes:
        line1 += segments[char][0] + " "
        line2 += segments[char][1] + " "
        line3 += segments[char][2] + " "

    # Limpar espaços no final
    line1 = line1.rstrip()
    line2 = line2.rstrip()
    line3 = line3.rstrip()

    # Retorno do resultado formatado
    return "\n".join([line1, line2, line3])
