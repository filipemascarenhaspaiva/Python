const vidaPorPersonagem = {
    'globin': 8,
    'orc': 12,
    'feiticeira': 18,
};

const danoPorArma = {
    'soco': 2,
    'arco': 5,
    'espada': 10,
};

let personagemSelecionado;
let armaSelecionada;

function iniciar() {
    const elementos = document.getElementsByClassName('elemento');

    for (const elemento of elementos) {
        elemento.addEventListener('click', marcarElementoSelecionado);
    }

    document.getElementById('calcular').addEventListener('click', calcularDano);
}

function marcarElementoSelecionado(evento) {
    const elementoSelecionado = evento.target.parentElement;

    // Se o bloco clicado não possui a classe 'elemento', consideramos que não
    // é um clique válido e encerramos a função, retornando algo vazio.
    if (!elementoSelecionado.classList.contains('elemento')) {
        return;
    }

    const idElementoSelecionado = elementoSelecionado.getAttribute('id');

    if (elementoSelecionado.classList.contains('personagem')) {
        personagemSelecionado = idElementoSelecionado;
        limparElementosSelecionados('personagem');
    } else {
        armaSelecionada = idElementoSelecionado;
        limparElementosSelecionados('arma');
    }

    elementoSelecionado.classList.add('selecionado');
}

function calcularDano() {
    if (!personagemSelecionado || !armaSelecionada) {
        alert('Selecione o personagem e a arma para calcular o dano');
        return;
    }

    const danoDados = rolarOsDados();
    const danoArma = danoPorArma[armaSelecionada];
    const danoTotal = danoDados + danoArma;
    const vidaPersonagem = vidaPorPersonagem[personagemSelecionado];

    let resultado = 'Dano: ' + danoTotal + '! ';

    if (danoTotal >= vidaPersonagem) {
        resultado += 'Parabéns, você matou ' + personagemSelecionado;
    } else {
        resultado += 'Putz, não foi dessa vez, tente novamente!';
    }

    document.getElementById('dano').innerHTML = resultado;
}

function limparElementosSelecionados(tipo) {
    const elementos = document.getElementsByClassName('elemento');

    for (const elemento of elementos) {
        if (elemento.classList.contains(tipo)) {
            elemento.classList.remove('selecionado');
        }
    }
}

function rolarOsDados() {
    const min = Math.ceil(1);
    const max = Math.floor(10);

    return Math.floor(Math.random() * (max - min + 1)) + min;
}
