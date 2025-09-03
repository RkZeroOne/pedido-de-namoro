import time
from rich.console import Console
from rich.live import Live
from rich.text import Text

console = Console()

# Trecho da música
lyrics = [
    ("Eu sabia ia ser nossa ultima dança (nossa ultima dança)", 4),
    ("Foi embora sem eu ver igual a minha infância", 4),
    ("Só me liga quando ela quer transa", 3),
    ("Deu saudade, então ela me chama", 3),
    ("Deve ser tão triste dançar nos braços de quem não te ama", 5),
    ("Dormir em outros lugares e lembrar da minha cama", 5),
    ("Pediu meu último pedaço e eu te disse, 'toma'", 4),
    ("Garota 'cê tá em pedaços por que ainda se apaixona?", 5),
    ("O amor exige muito", 3),
    ("E você não tem nada (tem nada)", 4),
]

def show_lyrics():
    with Live(console=console, refresh_per_second=10) as live:
        for line, delay in lyrics:
            text = Text(line, style="bold cyan")
            live.update(text)
            time.sleep(delay)

if __name__ == "__main__":
    show_lyrics()
