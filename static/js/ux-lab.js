const copy = {
  sprout: "Little ones take root while parents stay close to the community.",
  stones: "Middle kids build confidence through hands-on projects and warm structure.",
  summit: "Teens practice real skills, real responsibility, and belonging.",
  ready: "Families leave each term with proof of growth and a clearer next step."
};

const output = document.querySelector("#journey-copy");
document.querySelectorAll("[data-journey]").forEach((button) => {
  button.addEventListener("click", () => {
    document.querySelectorAll("[data-journey]").forEach((item) => {
      item.classList.remove("is-active");
    });
    button.classList.add("is-active");
    output.textContent = copy[button.dataset.journey];
  });
});

