let state = [1,2,3,4,0,6,7,5,8];
const grid = document.getElementById("grid");

function render() {
  grid.innerHTML = "";
  state.forEach(num => {
    const div = document.createElement("div");
    div.className = "tile";
    if (num === 0) {
      div.classList.add("empty");
      div.innerText = "";
    } else {
      div.innerText = num;
    }
    grid.appendChild(div);
  });
}

function shuffle() {
  state.sort(() => Math.random() - 0.5);
  render();
}

async function solve() {
  const algo = document.getElementById("algo").value;

  const res = await fetch("http://localhost:5000/solve", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ state: state, algorithm: algo })
  });

  const data = await res.json();

  if (data.solution) {
    document.getElementById("info").innerText = "Steps: " + data.steps;
    animate(data.solution);
  }
}

function animate(solution) {
  let i = 0;
  function step() {
    if (i < solution.length) {
      state = solution[i];
      render();
      i++;
      setTimeout(step, 500);
    }
  }
  step();
}

render();
