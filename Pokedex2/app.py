from flask import (
    Blueprint, render_template, request
)

from flask import Flask

app = Flask(__name__)

bp = Blueprint('app', __name__)


@bp.route('/', methods=('GET', 'POST'))
def index():
    pokemons = [
        {
            'numero': '001',
            'nome': 'Bulbasaur',
            'disponivel': True,
            'descricao': 'There is a plant seed on its back right from the day this Pokémon is born. The seed slowly grows larger.',
            'altura': '0,7 m',
            'categoria': 'Seed',
            'peso': '6,9 kg',
            'habilidade': 'Overgrow',
            'tipo': 'Grama e Veneno',

        },
        {
            'numero': '002',
            'nome': 'Ivysaur',
            'disponivel': True,
            'descricao': 'When the bulb on its back grows large, it appears to lose the ability to stand on its hind legs.',
            'altura': '1,0 m',
            'categoria': 'Seed',
            'peso': '13,0 kg',
            'habilidade': 'Overgrow',
            'tipo': 'Grama e Veneno',
        },
        {
            'numero': '003',
            'nome': 'Venusaur',
            'disponivel': True,
            'descricao': 'Its plant blooms when it is absorbing solar energy. It stays on the move to seek sunlight.',
            'altura': '2,0 m',
            'categoria': 'Seed',
            'peso': '100,0 kg',
            'habilidade': 'Overgrow',
            'tipo': 'Grama e Veneno',
        },
        {
            'numero': '004',
            'nome': 'Charmander',
            'disponivel': True,
            'descricao': 'It has a preference for hot things. When it rains, steam is said to spout from the tip of its tail.',
            'altura': '0,6 m',
            'categoria': 'Lizard',
            'peso': '8,5 kg',
            'habilidade': 'Blaze',
            'tipo': 'Fogo',
        },
        {
            'numero': '005',
            'nome': 'Charmeleon',
            'disponivel': True,
            'descricao': 'It has a barbaric nature. In battle, it whips its fiery tail around and slashes away with sharp claws.',
            'altura': '1,1 m',
            'categoria': 'Flame',
            'peso': '19,0 kg',
            'habilidade': 'Blaze',
            'tipo': 'Fogo',
        },
        {
            'numero': '006',
            'nome': 'Charizard',
            'disponivel': True,
            'descricao': 'It spits fire that is hot enough to melt boulders. It may cause forest fires by blowing flames.',
            'altura': '1,7 m',
            'categoria': 'Flame',
            'peso': '90,5 kg',
            'habilidade': 'Blaze',
            'tipo': 'Fogo Voador',
        },
        {
            'numero': '007',
            'nome': 'Squirtle',
            'disponivel': True,
            'descricao': 'When it retracts its long neck into its shell, it squirts out water with vigorous force.',
            'altura': '0,5 m',
            'categoria': 'Tiny Turtle',
            'peso': '9,0 kg',
            'habilidade': 'Torrent',
            'tipo': 'Água',
        },
        {
            'numero': '008',
            'nome': 'Wartotle',
            'disponivel': True,
            'descricao': 'It is recognized as a symbol of longevity. If its shell has algae on it, that Wartortle is very old.',
            'altura': '1,0 m',
            'categoria': 'Turtle',
            'peso': '22,5 kg',
            'habilidade': 'Torrent',
            'tipo': 'Água',
        },
        {
            'numero': '009',
            'nome': 'Blastoise',
            'disponivel': True,
            'descricao': 'It crushes its foe under its heavy body to cause fainting. In a pinch, it will withdraw inside its shell.',
            'altura': '1,6 m',
            'categoria': 'Shellfish',
            'peso': '85,5 kg',
            'habilidade': 'Torrent',
            'tipo': 'Água',
        }
    ]

    caminho_base_imagem = 'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/'
    
    if request.method == "POST":
        num_pokemon = request.form['nr_pokemon']
        selecionado = True
        num_pokemon_int = int(num_pokemon)
    else:
        selecionado = False
        num_pokemon = '000'
        num_pokemon_int = 0


    return render_template(
        'index.html',
        pokemons=pokemons,
        caminho_base_imagem=caminho_base_imagem,
        selecionado=selecionado,
        num_pokemon=num_pokemon,
        num_pokemon_int=num_pokemon_int
    )


app.register_blueprint(bp)

# Habilitando o hot reload (execução via python app.py em vez de flask run):
if __name__ == "__main__":
    app.run(debug=True)
