

document.getElementById('login-btn').addEventListener.EventListener('click', async () => {
    const matricula =document.querySelector('.inputizinho[type="text"]').value;
    const senha = document.querySelector('inputizinho[type="password"]').value;

    const response = await fetch('/autenticar', {
        method: 'POST',
        headers: {
            'Contente-Type': 'application/json'
        },
        body: JSON.stringify({
            matricula: matricula,
            senha: senha
        })
    });
    const data = await response.json();

    if (data.sucess) {
        window.location.href = '/homepage';
    } else {
        alert('Erro: Matrícula ou senha inválidos');
    }
})