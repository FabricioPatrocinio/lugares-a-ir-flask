estado_select = document.querySelector('#estado');
cidade_select = document.querySelector('#cidade');

estado_select.onchange = function () {
    estado = estado_select.value;

    fetch('cidade/' + estado).then(function (response) {
        response.json().then(function (data) {
            optionHTML = '';
            for (cidade of data.cidadearray) {
                optionHTML += '<option value="' + cidade.id + '">' + cidade.nome + '</option>'
            }
            cidade_select.innerHTML = optionHTML;
        });
    });
}