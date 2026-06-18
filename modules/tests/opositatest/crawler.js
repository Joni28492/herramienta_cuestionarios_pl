var collapsables = document.querySelectorAll('.CollapsiblePanel-header')
collapsables.forEach( async c => { await c.click() });

//todo hacer git pull cada vez que venga

//segunda parte
var cards = document.querySelectorAll('.Card')
var filteredCards = []

// eliminamos las cards que no necesitamos
for (let i = 5; i < cards.length; i++) {
    filteredCards.push(cards[i])
}

var Arr = [] 

filteredCards.map( card => {

    var container = card.children[0].children[0].children

    //Cabecera
    var header = container[0]
    var id = header.children[0].children[0].id 
    var pregunta =  header.children[0].children[0].textContent 

    //filtro para saber si la pregunta contiene imagen
    var img = (header.children[0].children.length === 2) ? header.children[0].children[1].src   : null

    //Respuestas // todo preparar para cuando las respuestas tengan imagenes
    var respuestas_li = container[1].children[0].children
    var [a, b, c, d] =[
           respuestas_li[0].children[0].children[0].children[1].children[0].textContent,
           respuestas_li[1].children[0].children[0].children[1].children[0].textContent,
           respuestas_li[2].children[0].children[0].children[1].children[0].textContent,
        //    respuestas_li[3].children[0].children[0].children[1].children[0].textContent
        ]

        if (respuestas_li.length>=4){
            d = respuestas_li[3].children[0].children[0].children[1].children[0].textContent
        }else{
            d = undefined
        }

   

  

    //todo -> obtener respuesta correcta
    var solucion = null
    var ulListedLi = container[1].children[0].childNodes

    //className is-correct
    // console.log(ulListedLi[2].childNodes[0].childNodes[0].className)
    ulListedLi.forEach((li, i) => {
        if(li.childNodes[0].childNodes[0].className.includes('is-correct')){
            switch (i) {
                case 0:
                    solucion = 'a'
                    break;

                case 1:
                    solucion = 'b'
                    break;
                case 2:
                    solucion = 'c'
                    break;

                case 3:
                    solucion = 'd'
                    break;

            
                default:
                    break;
            }
        }
    });

    //Footer
    var footer = container[2]
    var details = footer.children[0] //todo, es necesario que la explicacion este desplegada
    var html_details = details.children[1].children[0].innerHTML
    var temaPregunta = footer.children[1].children[0].textContent

    Arr.push({
        id,
        pregunta: 
            (header.children[0].children.length === 2)
            ? {pregunta, img}
            :pregunta,
        respuestas: {
            "a":a,
            "b":b,
            "c":c,
            "d":d,
        },
        tema: temaPregunta,
        solucion,
        // explicacion: `${html_details.replace('"', '\'')}`
        explicacion: html_details
    })
})


// console.table(Arr)
console.log(JSON.stringify(Arr))


