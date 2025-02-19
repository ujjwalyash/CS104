function makeChanges() {

    // TODO 1
    const imgs = document.getElementsByTagName("img");
    const n_imgs = imgs.length;
    for(let i = 0; i < n_imgs; i++){
        imgs[i].src = "timepass.png"
    }

    // TODO 2
    const h1s = document.getElementsByTagName("h1")
    const n_h1s = h1s.length
    for(let i = 0; i < n_h1s; i++){
        h1s[0].remove();
    }

    // TODO 3
    const ps = document.getElementsByTagName("p")
    const n_ps = ps.length
    for(let i = 0; i < n_ps; i++){
        ps[i].innerHTML = "Enough of JavaScript, lets stop.";
    }

    // TODO 4
    const h2s = document.getElementsByTagName("h2")
    const n_h2s = h2s.length
    for(let i = 0; i < n_h2s; i++){
        h2s[i].innerHTML = h2s[i].innerHTML.toUpperCase();
    }

    // TODO 5
    document.getElementById("div1").appendChild(document.createElement("h3"));
    document.re
}