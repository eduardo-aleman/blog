document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("pre > code").forEach((codeBlock) => {
    const button = document.createElement("button");
    button.className = "copy-button";
    button.type = "button";
    button.innerText = "Copiar";

    button.addEventListener("click", () => {
      navigator.clipboard.writeText(codeBlock.innerText).then(() => {
        button.innerText = "¡Copiado!";
        setTimeout(() => {
          button.innerText = "Copiar";
        }, 2000);
      });
    });

    const pre = codeBlock.parentNode;
    pre.style.position = "relative";
    button.style.position = "absolute";
    button.style.top = "0.5em";
    button.style.right = "0.5em";
    button.style.padding = "0.2em 0.6em";
    button.style.fontSize = "0.75em";
    pre.appendChild(button);
  });
});
// This script adds a "Copy" button to each code block in the documentation.
// When clicked, it copies the code to the clipboard and changes the button text to "Copied!" for 2 seconds.
// It uses the Clipboard API for copying text.
// The button is styled to appear in the top-right corner of each code block.
// Ensure the script runs after the DOM is fully loaded.
// This is useful for making code snippets easily shareable in documentation or tutorials.
// The script is designed to be lightweight and does not require any external libraries.
// It can be included in any HTML page that contains code blocks within <pre><code> tags.