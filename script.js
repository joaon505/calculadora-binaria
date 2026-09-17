const campoBinario = document.getElementById("binario");
const campoDecimal = document.getElementById("decimal");
const mensagem = document.getElementById("mensagem");
const btnBinarioDecimal = document.getElementById("btnBinarioDecimal");
const btnDecimalBinario = document.getElementById("btnDecimalBinario");
const btnLimpar = document.getElementById("btnLimpar");


function mostrarMensagem(texto) {
    mensagem.textContent = texto;
}


async function converter(tipo, valor) {
    try {
        const resposta = await fetch("/converter", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                tipo: tipo,
                valor: valor
            })
        });

        const dados = await resposta.json();

        if (dados.sucesso) {
            return dados.resultado;
        }

        throw new Error(dados.erro);
    } catch (erro) {
        mostrarMensagem(erro.message);
        return null;
    }
}


btnBinarioDecimal.addEventListener("click", async () => {
    const resultado = await converter("binario_decimal", campoBinario.value);

    if (resultado !== null) {
        campoDecimal.value = resultado;
        mostrarMensagem("Conversão realizada com sucesso.");
    }
});


btnDecimalBinario.addEventListener("click", async () => {
    const resultado = await converter("decimal_binario", campoDecimal.value);

    if (resultado !== null) {
        campoBinario.value = resultado;
        mostrarMensagem("Conversão realizada com sucesso.");
    }
});


btnLimpar.addEventListener("click", () => {
    campoBinario.value = "";
    campoDecimal.value = "";
    mostrarMensagem("");
    campoBinario.focus();
});


campoBinario.focus();
