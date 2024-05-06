function markCompleted(index) {
    var checkbox = document.getElementById("task" + index);
    var label = checkbox.nextElementSibling;

    if (checkbox.checked) {
        label.classList.add("completed");
    } else {
        label.classList.remove("completed");
    }

    fetch("/mark_completed/" + index, { method: "POST" });
}
