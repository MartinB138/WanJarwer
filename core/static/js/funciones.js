var x;                                               //definicion de objeto, en este caso x
x=$(document);                                       //x, recibe el documento actual (web)
x.ready(inicializarEventos);

function inicializarEventos()
{
var x;                                              //objeto var local a la funcion
x=$("#title1");                                    //recuperamos un elemento, selector llamado #titulo1
x.click(presionTitulo1)                             //a través del método click invocamos la función.

x=$("#title2");
x.click(presionTitulo2)

x=$("#title3");
x.click(presionTitulo3)

x=$("#title4");
x.click(presionTitulo4)

x=$("#title5");
x.click(presionTitulo5)
}

function presionTitulo1()                           //definición de la función, modificamos estilo
{
var x;
x=$("#title1");
x.css("color","#BA4A00");
x.css("font-family","Courier");
}
function presionTitulo2()
{
var x;
x=$("#title2");
x.css("background-color","#D1F2EB");
x.css("font-family","Arial");
}
function presionTitulo3()
{
var x;
x=$("#title3");
x.css("background-color","#D1F2EB");
x.css("font-family","Arial");
}
function presionTitulo4()
{
var x;
x=$("#title4");
x.css("background-color","#D1F2EB");
x.css("font-family","Arial");
}
function presionTitulo5()
{
var x;
x=$("#title5");
x.css("background-color","#D1F2EB");
x.css("font-family","Arial");
}