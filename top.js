window.onscroll = function() { scrollFunction() };  // функция прокрутки

function scrollFunction() {
    if(document.body.scrollTop > 200 || document.documentElement > 200) {  // как только прокрутились от верха более 200 px
        document.getElementById("top-btn").style.display = "block"; // ищем по Id, т.к. js; сделайся блоком и им отображайся
    } else {
        document.getElementById("top-btn").style.display = "none";// противном случае не отображайся
    }
}

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
