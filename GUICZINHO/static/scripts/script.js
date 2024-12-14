
// janela cinza quando clica nos tres tracinhos, presente em todas as telas

var linhas = document.getElementById("linhas")
var janela = document.getElementById("flutuante")

linhas.onclick = function(){
    if (janela.style.display === "block"){
        janela.style.display = "none"
    }
    else {
        janela.style.display = "block"
    }  
}



window.onclick = function(event) {
    if (event.target === janela) {
        janela.style.display = "block"
    }
}






let sair_tcc = document.querySelector('.back_doc')
let bnt_tcc = document.querySelector('#tcc')

let sair_rl = document.querySelector('.back_doc_2')
let bnt_rl = document.querySelector('#relatorio')

let tela_doc =document.querySelector('.visualizador')
let tela_doc_2 =document.querySelector('.visualizador_2')
let body = document.querySelector('body') 

bnt_tcc.onclick = function(){
    tela_doc.style.display = "block"
    body.style.overflow = "hidden"   
}

sair_tcc.onclick = function(){
    tela_doc.style.display = "none"
    body.style.overflow = "auto"
}


bnt_rl.onclick = function(){
    tela_doc_2.style.display = "block"
    body.style.overflow = "hidden"
} 

sair_rl.onclick = function(){
    tela_doc_2.style.display = "none"
    body.style.overflow = "auto"
}



// funcional do carrossel manual da pagina eventos

let bntNext = document.getElementById('next')
let bntBack = document.getElementById('back')

let contudo = document.querySelector('.container')
let banners = document.querySelector('.container .list-banner-atras')

let lista_acessos = document.querySelector(".tudo .list-acessos")

let lista_bolinha = document.querySelector('.botons .list-bolinhas')



bntNext.onclick = () => movimentarIntens('next')
bntBack.onclick = () => movimentarIntens('back')



function movimentarIntens(type){
    let listaritens = document.querySelectorAll('.list-banner-atras .objct')
    let listaracesso = document.querySelectorAll(".list-acessos .acesso")
    let listarboll = document.querySelectorAll('.list-bolinhas .boll')

    if (type === 'next'){
        banners.appendChild(listaritens[0])

        lista_acessos.appendChild(listaracesso[0])
        
        lista_bolinha.prepend(listarboll[listarboll.length-1]) 
        
        contudo.classList.add('next')

    }
    else{

        banners.prepend(listaritens[listaritens.length-1])

        lista_acessos.prepend(listaracesso[listaracesso.length-1])

        lista_bolinha.appendChild(listarboll[0])

        contudo.classList.add('back')
    }


    setTimeout(() => {
        contudo.classList.remove('next')
        contudo.classList.remove('next')
    }, 3000)

}


// carrosel automatico



// cabeçalho fixo



// window.addEventListener("scroll", function(){
//     let header = document.querySelector('.cabecalho')
//     header.classList.toggle('rolagem', window.scrollY > 100)
//     console.log(header)
    
// });


<<<<<<< HEAD
=======



// janela de adicionar setores

let tl_add = document.querySelector('.tela_adicionar')
let list_setores =document.querySelector('lista_setores')


let bnt_add = document.querySelector('#adicionar')
let sair_form = document.querySelector('.sair_formulario')

bnt_add.onclick = function(){
    body.style.overflow ='hidden'
    tl_add.style.display = 'block'
    console.log(oiiiiiiiiiiiiiiii)
}

sair_form.onclick = function(){
    body.style.overflow = 'block'
    tl_add.style.display = 'none'
    console.log(olaaaaaaaaaa)
}





>>>>>>> 6077cfe (quinto commit)
