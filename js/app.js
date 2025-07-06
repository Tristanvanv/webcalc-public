
/* particlesJS.load(@dom-id, @path-json, @callback (optional)); 
particlesJS.load('js/particles-js', 'json/particles.json', function() {
  console.log('callback - js/particles.js config loaded');
}); */

const calcinput = document.querySelector(".calc-txt");
const calcbtns = document.querySelectorAll(".btns")
const resultbtn = document.querySelector(".result-output")

calcbtns.forEach( btns => {
  btns.addEventListener("click", function () {
    const value = btns.textContent;
    if (value === "=") {
      const expression = calcinput.value;
      fetch("https://webcalc-hgcv.onrender.com/evaluate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ expression })
      })
      .then(response => response.json())
      .then(data => {
        if (data.result !== undefined) {
          calcinput.value = data.result;
        } else if (data.error) {
          alert("Fout: " + data.error);
        }
      })
      .catch(error => {
        console.error("Netwerkfout:", error);
        alert("Er ging iets mis met de verbinding");
      }) 
    } else if (value === "C") {
      calcinput.value = ""
    } else if (value === "⌫") {
      calcinput.value = calcinput.value.slice(0, -1);
    } else {
      calcinput.value += value;
    }
  })
})


