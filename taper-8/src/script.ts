function setup(){
    // pull text and clear
    let block = document.querySelector('#t')
    let text :string = block!.innerHTML
    block!.innerHTML = '';
    // split, convert to binary, add anchor and event
    text.split('').map(function (char: string) {
       let anc = document.createElement('a');
       let x : string[] = [',', ' ', '.', "'"];
       if (!x.includes(char)) {
           anc.setAttribute("class", char);
       } else if (char == ' ') {
           anc.setAttribute("class", "xs");
       } else if (char == "'") {
           anc.setAttribute("class", "xa");
       } else if (char == ',') {
           anc.setAttribute("class", "xc");
       } else {
           anc.setAttribute("class", "xp")
       }

       let bin = char.charCodeAt(0).toString(2);
       anc.innerText = new Array(9 - bin.length).join('0') + bin;
       block!.append(anc)
       block!.append('\u200b')
       anc.addEventListener('click', function(){
           converter(this)
       });
    });
    
};

function converter(e: any){
    let letter: string = e.className;
    let letters = document.querySelectorAll('.'+ letter)
    var newText: string;
    var inText = e.innerText
    if (inText.length >= 2 && inText.indexOf('&') != 0){ // i.e., is a bin
        newText = '&x'+letter.charCodeAt(0)+';';
    } else if (inText.indexOf('&') === 0) {
        if (letter.length === 1) {
            newText = letter;
        } else if (letter === 'xs') {
            newText = " ";
        } else if (letter === 'xa') {
            newText = "'";
        } else if (letter === 'xp') {
            newText = "."
        } else {
            newText = ","
        }
    } else {
        newText = letter.charCodeAt(0).toString(2);
    };
    // add 'em back in
    for (var i = 0; i < letters.length; i++){
        letters[i].innerHTML = newText;
    }
}

window.onload = setup;
