var count = 0;
var heart = document.getElementById("heart");
var disp = document.getElementById("disp");

function count_likes() {
  heart.classList.add("fas");
  count++;
  disp.innerHTML = count;
}
