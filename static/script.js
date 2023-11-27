function updateCarYearModel(modelo) {
    fetch('/pesquisar_ano_modelo?modelo=' + modelo)
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    var select = document.getElementById('ano_modelo');
                    for (var key in data) {
                        var option = document.createElement("option");
                        option.value = data[key];
                        option.text = data[key];
                        select.add(option);
                    }

                })
                .catch(error => console.error('Erro na requisição:', error));

}