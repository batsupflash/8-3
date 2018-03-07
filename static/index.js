   var clicks = 0;
function addTIEP() {
var container = document.getElementById('TIEP');
container.innerHTML += "tiếp ";
clicks +=1;
if (clicks == 6) {
        $("a").attr("href", "/pick");

}
}
