document.addEventListener("DOMContentLoaded", () => {
  const prefersReducedMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;

  /* ---------- Header scroll state ---------- */
  const header = document.querySelector(".site-header");
  if (header) {
    const onScroll = () => {
      header.classList.toggle("scrolled", window.scrollY > 40);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---------- Mobile nav toggle ---------- */
  const toggle = document.querySelector(".nav-toggle");
  const links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", () => {
      const isOpen = links.classList.toggle("open");
      toggle.textContent = isOpen ? "✕" : "☰";
      document.body.style.overflow = isOpen ? "hidden" : "";
    });
    links.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => {
        links.classList.remove("open");
        toggle.textContent = "☰";
        document.body.style.overflow = "";
      });
    });
  }

  /* ---------- Scroll reveal ---------- */
  const revealEls = document.querySelectorAll(".reveal");
  if (revealEls.length) {
    if (prefersReducedMotion || !("IntersectionObserver" in window)) {
      revealEls.forEach((el) => el.classList.add("in-view"));
    } else {
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add("in-view");
              observer.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.15, rootMargin: "0px 0px -60px 0px" }
      );
      revealEls.forEach((el) => observer.observe(el));
    }
  }

  /* ---------- Animated counters ---------- */
  const counters = document.querySelectorAll("[data-count-to]");
  if (counters.length) {
    const animateCounter = (el) => {
      const target = parseFloat(el.dataset.countTo);
      const suffix = el.dataset.suffix || "";
      const duration = 1600;
      const start = performance.now();

      const step = (now) => {
        const progress = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        const value = target * eased;
        el.textContent =
          (target % 1 === 0 ? Math.round(value) : value.toFixed(1)) + suffix;
        if (progress < 1) requestAnimationFrame(step);
      };
      if (prefersReducedMotion) {
        el.textContent = target + suffix;
      } else {
        requestAnimationFrame(step);
      }
    };

    if ("IntersectionObserver" in window) {
      const counterObserver = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              animateCounter(entry.target);
              counterObserver.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.5 }
      );
      counters.forEach((el) => counterObserver.observe(el));
    } else {
      counters.forEach(animateCounter);
    }
  }

  /* ---------- 3D tilt cards ---------- */
  const tiltCards = document.querySelectorAll(".tilt-card");
  if (tiltCards.length && !prefersReducedMotion && window.matchMedia("(hover: hover)").matches) {
    tiltCards.forEach((card) => {
      const strength = 10;
      card.addEventListener("mousemove", (e) => {
        const rect = card.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width - 0.5;
        const y = (e.clientY - rect.top) / rect.height - 0.5;
        card.style.transform = `perspective(800px) rotateY(${x * strength}deg) rotateX(${-y * strength}deg) translateY(-4px)`;
      });
      card.addEventListener("mouseleave", () => {
        card.style.transform = "perspective(800px) rotateY(0) rotateX(0) translateY(0)";
      });
    });
  }

  /* ---------- Gallery filter ---------- */
  const filterButtons = document.querySelectorAll(".filter-btn");
  const galleryItems = document.querySelectorAll("[data-category]");
  if (filterButtons.length && galleryItems.length) {
    filterButtons.forEach((btn) => {
      btn.addEventListener("click", () => {
        filterButtons.forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        const filter = btn.dataset.filter;
        galleryItems.forEach((item) => {
          const match = filter === "all" || item.dataset.category === filter;
          item.style.display = match ? "" : "none";
        });
      });
    });
  }

  /* ---------- Contact form ---------- */
  const form = document.getElementById("contact-form");
  const status = document.getElementById("form-status");
  if (form && status) {
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const name = form.name.value.trim();
      const email = form.email.value.trim();
      const message = form.message.value.trim();
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

      status.classList.remove("success", "error");

      if (!name || !email || !message) {
        status.textContent = "Merci de remplir tous les champs.";
        status.classList.add("error", "visible");
        return;
      }
      if (!emailPattern.test(email)) {
        status.textContent = "Merci de saisir une adresse email valide.";
        status.classList.add("error", "visible");
        return;
      }

      status.textContent =
        "Merci pour votre message ! Nous vous répondrons dans les meilleurs délais.";
      status.classList.add("success", "visible");
      form.reset();
    });
  }

  /* ---------- Hero floating leaves canvas ---------- */
  const canvas = document.getElementById("leaves");
  if (canvas && !prefersReducedMotion) {
    const ctx = canvas.getContext("2d");
    let width, height, particles;
    const COUNT = 34;

    const resize = () => {
      width = canvas.width = canvas.offsetWidth * devicePixelRatio;
      height = canvas.height = canvas.offsetHeight * devicePixelRatio;
    };

    const makeParticle = () => ({
      x: Math.random() * width,
      y: Math.random() * height,
      r: (Math.random() * 3 + 1.5) * devicePixelRatio,
      speedY: (Math.random() * 0.35 + 0.08) * devicePixelRatio,
      speedX: (Math.random() - 0.5) * 0.3 * devicePixelRatio,
      drift: Math.random() * Math.PI * 2,
      driftSpeed: Math.random() * 0.015 + 0.005,
      opacity: Math.random() * 0.4 + 0.15,
      color: Math.random() > 0.5 ? "211,164,92" : "247,244,238",
    });

    const init = () => {
      resize();
      particles = Array.from({ length: COUNT }, makeParticle);
    };

    const tick = () => {
      ctx.clearRect(0, 0, width, height);
      particles.forEach((p) => {
        p.drift += p.driftSpeed;
        p.y -= p.speedY;
        p.x += p.speedX + Math.sin(p.drift) * 0.4 * devicePixelRatio;

        if (p.y < -10) {
          p.y = height + 10;
          p.x = Math.random() * width;
        }
        if (p.x < -10) p.x = width + 10;
        if (p.x > width + 10) p.x = -10;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(${p.color},${p.opacity})`;
        ctx.fill();
      });
      requestAnimationFrame(tick);
    };

    init();
    window.addEventListener("resize", init);
    requestAnimationFrame(tick);
  }
});
