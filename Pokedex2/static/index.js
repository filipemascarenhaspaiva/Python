const cardPokemons = document.querySelectorAll('.card_pokemon');
const input = document.getElementById('nr_pokemon');

let pokemonSelecionado;

// Lógica para selecionar o pokémon quando o usuário clicar em algum card
for (const cardPokemon of cardPokemons) {
    cardPokemon.addEventListener('click', function () {
        // Procura por cards que já estão selecionados
        const cardsSelecionados = document.querySelectorAll('.card_pokemon.selecionado');
		

        // Caso tenha um ou mais cards, remove as classes de selecionado deles.
        if (cardsSelecionados.length > 0) {
            for (const cardSelecionado of cardsSelecionados) {
                cardSelecionado.classList.remove('selecionado');
            }
        }

        if (!this.classList.contains('selecionado')) {
			this.classList.add('selecionado');
			
            // Coloca o card que foi clicado na variável 'pokemonSelecionado'
            pokemonSelecionado = this;
			const nrPokemon = pokemonSelecionado.getAttribute('data-numero');
			nr_pokemon.value = nrPokemon;
        } else {
            this.classList.remove('selecionado');
        }
    })
}

const botaoEscolher = document.getElementById('botao_escolher');
const blocoPokemonSelecionado = document.getElementById('pokemon_selecionado');
botaoEscolher.addEventListener('click', function () {
    if (pokemonSelecionado) {
        const nomePokemon = pokemonSelecionado.getAttribute('data-nome');
        blocoPokemonSelecionado.innerHTML = `Pokémon escolhido: <b>${nomePokemon}</b>`;
		
    } else {
        blocoPokemonSelecionado.innerHTML = `Nenhum pokémon foi selecionado`;
    }
});
