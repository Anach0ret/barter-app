document.addEventListener("DOMContentLoaded", function () {
    const toasts = document.querySelectorAll(".toast");

    toasts.forEach((toast, index) => {
      setTimeout(() => {
        toast.style.transition = "opacity 0.5s ease, transform 0.5s ease";
        toast.style.opacity = "0";
        toast.style.transform = "translateY(-10px)";
        setTimeout(() => toast.remove(), 500); // удаляем из DOM
      }, 3000 + index * 500); // покадрово исчезают
    });
  });