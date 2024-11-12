// Mapeamento dos dígitos para o formato de 7 segmentos
const segments = {
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
  ':': ["   ", " . ", "   "]
};

// Função que retorna a representação de um dígito específico
const getSegment = (digit) => {
  return segments[digit] || ["   ", "   ", "   "];
};

// Função para exibir o horário em formato de display de 7 segmentos
const sevenSegmentify = (time) => {
  const displayLines = ["", "", ""];
  
  // Processa cada caractere da entrada de tempo
  for (const char of time) {
    const segment = getSegment(char);

    // Adiciona o segmento para cada linha, com espaçamento apropriado
    displayLines[0] += segment[0];
    displayLines[1] += segment[1];
    displayLines[2] += segment[2];
    
    // Adiciona um espaço entre os segmentos, exceto após o último dígito
    if (char !== time[time.length - 1]) {
      displayLines[0] += " ";
      displayLines[1] += " ";
      displayLines[2] += " ";
    }
  }

  // Junta as linhas em uma única string com quebras de linha
  const result = displayLines.join("\n");
  
  // Log para verificar o resultado final formatado
  console.log("\nResultado formatado para o tempo:", time);
  console.log(result);
  
  return result;
};

// Exporta a função sevenSegmentify para uso em testes
module.exports = sevenSegmentify;
