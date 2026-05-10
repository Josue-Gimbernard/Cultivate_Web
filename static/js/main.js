document.documentElement.classList.add("js-ready");

document.querySelectorAll("[data-walkthrough]").forEach((root) => {
  const slides = [...root.querySelectorAll("[data-walkthrough-slide]")];
  const jumps = [...root.querySelectorAll("[data-walkthrough-jump]")];
  const progress = root.querySelector("[data-walkthrough-progress]");
  const count = root.querySelector("[data-walkthrough-count]");
  const prev = root.querySelector("[data-walkthrough-prev]");
  const next = root.querySelector("[data-walkthrough-next]");
  const present = root.querySelector("[data-walkthrough-present]");
  let activeIndex = 0;

  function render(index) {
    activeIndex = Math.max(0, Math.min(index, slides.length - 1));

    slides.forEach((slide, slideIndex) => {
      slide.classList.toggle("is-active", slideIndex === activeIndex);
    });

    jumps.forEach((jump, jumpIndex) => {
      jump.classList.toggle("is-active", jumpIndex === activeIndex);
    });

    if (progress) {
      progress.style.width = `${((activeIndex + 1) / slides.length) * 100}%`;
    }

    if (count) {
      count.textContent = `${activeIndex + 1} of ${slides.length}`;
    }

    if (prev) {
      prev.disabled = activeIndex === 0;
    }

    if (next) {
      next.disabled = activeIndex === slides.length - 1;
    }
  }

  jumps.forEach((jump) => {
    jump.addEventListener("click", (event) => {
      event.preventDefault();
      render(Number(jump.dataset.walkthroughJump));
    });
  });

  prev?.addEventListener("click", () => render(activeIndex - 1));
  next?.addEventListener("click", () => render(activeIndex + 1));
  present?.addEventListener("click", () => {
    root.classList.toggle("is-presenting");
    present.textContent = root.classList.contains("is-presenting")
      ? "Exit focus"
      : "Focus slides";
  });

  document.addEventListener("keydown", (event) => {
    if (!root.matches(":hover") && document.activeElement === document.body) {
      return;
    }

    if (event.key === "ArrowRight") {
      render(activeIndex + 1);
    }

    if (event.key === "ArrowLeft") {
      render(activeIndex - 1);
    }
  });

  render(0);
});
