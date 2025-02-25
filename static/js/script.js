function imprimirTabela(i){
    var cssEstilos = '';
    var imp = window.open('', 'div', 'width='+window.innerWidth+',height='+window.innerWidth);

    let btns = document.querySelectorAll('.print');

    for(let i = 0; i < btns.length; i++) {
        btns[i].style.display = "none";
    }

    var cSs = document.querySelectorAll("link[rel='stylesheet']");
    for(x=0; x < cSs.length; x++){
       cssEstilos += '<link rel="stylesheet" href="'+cSs[x].href+'">';
    }

    imp.document.write('<html><head><title>' + document.title  + '</title>');
    imp.document.write(cssEstilos+'</head><body>');
    imp.document.write(document.getElementById(i).innerHTML);
    imp.document.write('</body></html>');

    setTimeout(function(){
       imp.print();
    },500);

    for(let i = 0; i < btns.length; i++) {
        btns[i].style.display = "block";
    }
}