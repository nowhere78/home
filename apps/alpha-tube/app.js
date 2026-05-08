// Omega Dispatch - Dashboard Logic
document.addEventListener('DOMContentLoaded', () => {
    console.log("⚡ Omega Dispatch Dashboard Initialized");

    // Simulate real-time data updates
    const updateRiskValues = () => {
        const values = document.querySelectorAll('.divergence-value');
        values.forEach(v => {
            const current = parseFloat(v.innerText);
            const change = (Math.random() - 0.5) * 0.1;
            const newVal = (current + change).toFixed(2);
            v.innerText = (newVal > 0 ? "+" : "") + newVal;
            
            // Color feedback
            if (newVal > 2.0) {
                v.style.color = "#ff4757";
            } else if (newVal > 1.0) {
                v.style.color = "#D4AF37";
            } else {
                v.style.color = "#2ecc71";
            }
        });
    };

    setInterval(updateRiskValues, 3000);

    // Simple interaction logic
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('click', () => {
            const title = card.querySelector('h3').innerText;
            alert(`[오메가 분석 리포트] ${title}의 '인과관계(Why)' 분석 세션으로 이동합니다.`);
        });
    });
});
