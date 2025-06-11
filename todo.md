# AsciiFication

A CLI in Python to transform images into ASCII characters and print them on terminal.


## Reasearch:

[DONE]1. 📷 Como funciona uma imagem digital (pixels e cores)

    Você precisa entender:

    O que é uma imagem em termos de pixels.

    O que é o valor RGB de um pixel (vermelho, verde, azul).

    Que um pixel pode ser transformado em tons de cinza.

    👉 Estude:

    Matriz de pixels

RGB → Grayscale conversion (ex: fórmula de luminância: 0.299*R + 0.587*G + 0.114*B)

    2. ⚖️ Mapeamento de tons de cinza para caracteres ASCII

    Depois de ter o valor de brilho (0 a 255), você vai:

    Mapear cada intervalo de brilho para um caractere ASCII.

    Usar uma “escala de densidade” com caracteres, tipo:
    "@%#*+=-:. "
(caracteres escuros → claros)

    👉 Estude:

    Relação entre densidade visual de um caractere e o brilho

    Como dividir 256 níveis de cinza entre os caracteres escolhidos

    3. 🖼️ Redimensionamento de imagem

    Como ASCII é texto (com largura/altura diferente de pixel real), você tem que:

    Redimensionar a imagem para o terminal ou área onde vai aparecer.

    Considerar que caracteres normalmente são mais altos do que largos.

    👉 Estude:

    Como redimensionar proporcionalmente uma imagem

    Ajustar a proporção para "text mode" (ex: largura x altura corrigida)

    4. 📤 Leitura e manipulação de imagem

    No Node.js ou qualquer linguagem, você vai precisar:

Carregar a imagem (JPEG, PNG, etc.)

    Ler os pixels da imagem

    Converter a imagem para grayscale

    👉 Estude:

Como ler pixels de imagem em Node (com bibliotecas como sharp ou jimp)

    5. 🧾 Saída em texto formatado

    Você precisa:

    Montar o texto linha por linha

    Garantir que cada caractere está na posição certa para formar a imagem

    👉 Estude:

Manipulação de strings e layout em monoespaçado (como terminal, <pre> no HTML, etc.)
