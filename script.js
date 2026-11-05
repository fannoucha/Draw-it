const canvas = document.getElementById("drawing");
const ctx = canvas.getContext("2d");
const width = document.getElementById("width");
let color = "black";
let drawing = false;

canvas.width = 1200;
canvas.height = 700;

document.querySelectorAll("[data-color]").forEach(button => {
    button.addEventListener("click", () => {
        color = button.dataset.color;
    });
});

canvas.addEventListener("pointerdown", event => {
    drawing = true;
    canvas.setPointerCapture(event.pointerId);
    ctx.beginPath();
    ctx.moveTo(...position(event));
});
function position(event) {
    const rect = canvas.getBoundingClientRect();
    return [
        (event.clientX - rect.left) * canvas.width / rect.width,
        (event.clientY - rect.top) * canvas.height / rect.height
    ];
}

canvas.addEventListener("pointermove", event => {
    if (!drawing) return;
    ctx.lineTo(...position(event));
    ctx.strokeStyle = color;
    ctx.lineWidth = width.value;
    ctx.lineCap = "round";
    ctx.stroke();
});

canvas.addEventListener("pointerup", () => drawing = false);
canvas.addEventListener("pointercancel", () => drawing = false);
