const equationbox = document.getElementById('equationbox');
const answerbox = document.getElementById('answerbox');

buttons.forEach(button => {
    button.addEventListener('click', () => {
        const buttonId = button.id;
        const buttonText = button.textContent.trim();

        switch (buttonId) {
            case 'buttonac':
                equationbox.textContent = '';
                answerbox.textContent = '';
                break;
            case 'buttondel':
                equationbox.textContent = equationbox.textContent.slice(0, -1);
                break;
            case 'buttonequal':
                equationbox.textContent = answerbox.textContent;
                answerbox.textContent = '';
                break;
            case 'buttoninverse':
                break;
            default:
                equationbox.textContent += buttonText
                    .replace(/sin(?:⁻¹)?|cos(?:⁻¹)?|tan(?:⁻¹)?/g, (match) => match.includes("⁻¹") ? match + "(" : match + "(")
                    .replace(/log/g, 'log₁₀(')
                    .replace(/xⁿ/g, '^(')
                    .replace(/10ⁿ/g, '10^(')
                    .replace(/n!/g, '!');
                break;
        }

        try {
            const formattedEquation = equationbox.textContent

                .replace(/\s/g, '')  // spaces
                .replace(/÷/g,  '/') // division
                .replace(/×/g,  '*') // multiplication

                // trigonometry
                .replace(/sin(?:⁻¹)?/g, (match) => match === "sin⁻¹" ? "Math.asin" : "Math.sin")
                .replace(/cos(?:⁻¹)?/g, (match) => match === "cos⁻¹" ? "Math.acos" : "Math.cos")
                .replace(/tan(?:⁻¹)?/g, (match) => match === "tan⁻¹" ? "Math.atan" : "Math.tan")

                // log
                .replace(/log₁₀/g,  'Math.log10')

                // constants
                .replace(/PI/g,     'Math.PI')
                .replace(/\be\b/g,  'Math.E')

                // power
                .replace(/(\d+)\^\(([^)]+)\)/g, (match, base, exponent) => Math.pow(Number(base), eval(exponent)))

                // factorial
                .replace(/(\d+)!/g, (match, n) => {
                    let result = 1;
                    for (let i = 1; i <= Number(n); i++) result *= i;
                    return result;
                });

            answerbox.textContent = eval(formattedEquation);
        } 

        catch (error) {
            answerbox.textContent = error instanceof SyntaxError ? '' : error.message;
        }
    });
});
