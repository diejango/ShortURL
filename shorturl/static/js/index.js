function url (e){
    var a = document.getElementById('url');
    if( a.value =='' || a.value == null) {
        e.preventDefault();
    }
    return a.value;
}
function gen (){
    return Math.floor(Math.random()*(99999999 - 1)) + 1;
}
function res(){
    var x = url();
    var y = gen();
    var rep = document.getElementById('res');
    fetch('http://127.0.0.1:8000/create/',{method:'POST',headers:{'Content-Type':'application/json',},body:'{"url": "'+x+'","get":"'+y+'"}'}).then((response)=>response.json()).then((data)=>{console.log('success:',data);})
    rep.innerHTML=('http://127.0.0.1:8000/r/'+y);
    rep.setAttribute('href','http://127.0.0.1:8000/r/'+y);
    return x;
}

