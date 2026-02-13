let url= "http://127.0.0.1:8000/sumar"

let myAPI= url+ "?a=5&b=45"; 

//Se usa await para que el programa espere a que la API se conecte, y de etsa manera no se desincronize

async function crearPeticion() {
    let response = await fetch(myAPI);
    let datos= response.json();    
}
