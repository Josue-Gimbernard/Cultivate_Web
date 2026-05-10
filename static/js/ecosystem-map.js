const spaces = window.CULTIVATE_SPACES || [];
const nodes = document.querySelectorAll("[data-space-index]");
const phase = document.querySelector("#map-phase");
const name = document.querySelector("#map-name");
const audience = document.querySelector("#map-audience");
const copy = document.querySelector("#map-detail-copy");
const dependencies = document.querySelector("#map-dependencies");

function renderSpace(index) {
  const space = spaces[index];
  if (!space) return;
  nodes.forEach((node) => node.classList.remove("is-active"));
  nodes[index].classList.add("is-active");
  phase.textContent = space.phase;
  name.textContent = space.name;
  audience.textContent = space.audience;
  copy.textContent = space.detail;
  dependencies.innerHTML = "";
  space.dependencies.forEach((dependency) => {
    const item = document.createElement("li");
    item.textContent = dependency;
    dependencies.appendChild(item);
  });
}

nodes.forEach((node) => {
  node.addEventListener("click", () => {
    renderSpace(Number(node.dataset.spaceIndex));
  });
});
