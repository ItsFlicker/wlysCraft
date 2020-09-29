var Video = document.getElementById("video");
var Last = document.getElementById("lastP");
var Next = document.getElementById("nextP");
var Text = document.getElementById("text");
var P = 1;

Next.addEventListener("click", function () {
    if(P === 45) {
        P = 1;
    }
    else {
        P++;
    }
    Video["src"] = "https://player.bilibili.com/player.html?aid=48489320&cid=84920721&page=" + P;
    Text.innerHTML = "当前是第" + P + "节";
});

Last.addEventListener("click", function () {
    if(P === 1) {
        P = 45;
    }
    else {
        P--;
    }
    Video["src"] = "https://player.bilibili.com/player.html?aid=48489320&cid=84920721&page=" + P;
    Text.innerHTML = "当前是第" + P + "节";
});