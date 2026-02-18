const mainDiv = document.querySelector('.maindiv');
const displayDiv = document.querySelector('.displaydiv');
const buttonsDiv = document.querySelector('.buttonsdiv');

const modeButton = document.getElementById('modebutton');
const arrow = document.getElementById('arrow');
const sciButtons = document.querySelectorAll('.sci');
const buttons = document.querySelectorAll('.buttonclass');

const inverseButton = document.getElementById('buttoninverse');
const logButton = document.getElementById('buttonlog');
const sinButton = document.getElementById('buttonsin');
const cosButton = document.getElementById('buttoncos');
const tanButton = document.getElementById('buttontan');

const modeCss = document.getElementById('modeCss');

let isExpanded = true;
let isLightMode = false;
let isInversed = false;

arrow.addEventListener('click', () => {
    isExpanded = !isExpanded;
    displayDiv.style.height = isExpanded ? '25%' : '70%';
    sciButtons.forEach(button => button.classList.toggle('hidden', !isExpanded));
    arrow.textContent = isExpanded ? 'keyboard_arrow_down' : 'keyboard_arrow_up';
});

buttons.forEach(button => {
    button.addEventListener('mouseenter', () => button.style.filter = 'brightness(1.5)');
    button.addEventListener('mouseleave', () => button.style.filter = 'brightness(1)');
});

// light / dark mode
modeButton.addEventListener('click', () => {
    isLightMode = !isLightMode;
    modeCss.href = isLightMode ? 'stylesheet/lightMode.css' : 'stylesheet/darkMode.css';
    modeButton.textContent = isLightMode ? 'light_mode' : 'dark_mode';
});

inverseButton.addEventListener('click', () => {
    isInversed = !isInversed;
    logButton.textContent = isInversed ? '10ⁿ' : 'log';
    sinButton.textContent = isInversed ? 'sin⁻¹' : 'sin';
    cosButton.textContent = isInversed ? 'cos⁻¹' : 'cos';
    tanButton.textContent = isInversed ? 'tan⁻¹' : 'tan';
    inverseButton.textContent = isInversed ? 'NORMAL' : 'INVERSE';
});
