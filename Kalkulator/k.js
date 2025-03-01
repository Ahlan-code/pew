function appendToDisplay(value) {
    document.getElementById('display').value += value;
}

function clearDisplay() {
    document.getElementById('display').value = '';
}

function calculate() {
    const display = document.getElementById('display');
    try {
        // Mengganti fungsi sin, cos, tan, log, sqrt dengan fungsi JavaScript
        let result = display.value
            .replace(/sin/g, 'Math.sin')
            .replace(/cos/g, 'Math.cos')
            .replace(/tan/g, 'Math.tan')
            .replace(/log/g, 'Math.log')
            .replace(/sqrt/g, 'Math.sqrt')
            .replace(/\*\*/g, '^'); // Pangkat

        // Menghitung hasil
        result = eval(result);
        display.value = result;
    } catch