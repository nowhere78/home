# 💻 Developer — Researcher가 제공한 데이터를 기반으로, 경고적이고 인터랙티브한 UX/UI를 갖춘 '위험 괴리 지수 시각화 대시보드'의 프로토타입을 완성해야 합니다. API 입력 데이터는 JSON 배열 형태를 표준 포맷으로 사용하며, 핵심 위험 구간에서는 경고 애니메이션(Red/Gold)을 적용하는 코드를 구현하세요.

💻 Developer: 작업 시작합니다.

CEO님의 지시에 따라, Researcher가 제공한 핵심 데이터를 기반으로 '위험 괴리 지수(Risk Discrepancy Index)'를 시각화하고, 40대 타겟의 불안감을 극대화하는 경고적이고 인터랙티브한 대시보드 프로토타입을 완성했습니다.

이 프로토타입은 React 기반으로 구현되었으며, 데이터 입력은 JSON 배열 표준 포맷을 따릅니다. 핵심 위험 구간에서는 경고 색상(Red/Gold)을 적용하는 로직을 포함하고 있습니다.

### 📁 프로젝트 구조 및 사용 설명

**필수 전제 조건:** React 환경 (CRA 또는 Vite) 및 `react-chartjs-2`, `chart.js` 라이브러리가 설치되어 있어야 합니다.

**사용법:** `Dashboard.jsx` 파일을 컴포넌트에 추가하고, `<RiskDashboard data={...} />` 태그를 사용하여 실행합니다. `data` prop에 표준 JSON 배열을 전달하세요.

### 💻 `src/components/RiskDashboard.jsx`

```jsx
import React, { useState, useMemo } from 'react';
import { Line } from 'react-chartjs-2';
import { Chart, registerables } from 'chart.js';

// Chart.js 컴포넌트 등록
Chart.register(...registerables);

// --- 스타일 정의 ---
const styles = {
    dashboard: "p-6 bg-gray-50 rounded-xl shadow-2xl border-l-8 border-red-700",
    warningBox: "p-6 rounded-lg shadow-inner transition-all duration-500 ease-in-out border-l-4",
    redWarning: "bg-red-100 border-red-700 text-red-900",
    goldWarning: "bg-yellow-100 border-yellow-600 text-yellow-900",
    safe: "bg-green-100 border-green-700 text-green-900",
    metricCard: "p-4 bg-white rounded-md shadow-md flex justify-between items-center",
    title: "text-2xl font-bold mb-6 border-b pb-2 text-gray-800",
    interactiveControl: "p-4 bg-gray-100 rounded-lg mt-6",
};

/**
 * 위험 괴리 지수 대시보드 프로토타입 컴포넌트
 * @param {Object} props - props.data: JSON 배열 형태의 시계열 데이터
 */
const RiskDashboard = ({ data = [] }) => {
    // 1. 데이터 처리 및 위험 등급 산출 (Memoization을 통해 성능 최적화)
    const { overallRiskScore, riskLevel, warningClass } = useMemo(() => {
        if (!data || data.length === 0) {
            return { overallRiskScore: 0, riskLevel: 'N/A', warningClass: 'safe' };
        }

        // 최종 데이터 포인트만 가져와서 현재 위험 지수를 계산 (가장 최신 데이터)
        const latestData = data[data.length - 1];
        
        // 가상의 위험 괴리 지수 계산 (실제로는 복잡한 API 호출 필요)
        const score = parseFloat(latestData['괴리지수'] || 0).toFixed(2);
        
        let level = '안정';
        let warningClass = 'safe';

        if (score >= 1.5) {
            level = '🚨 극심한 경고 (CRITICAL)';
            warningClass = 'redWarning';
        } else if (score >= 0.8) {
            level = '⚠️ 주의 필요 (WARNING)';
            warningClass = 'goldWarning';
        }

        return { overallRiskScore: parseFloat(score), riskLevel: level, warningClass };
    }, [data]);

    // 2. 차트 데이터 가공
    const chartData = {
        labels: data.map(d => d.날짜),
        datasets: [
            {
                label: '위험 괴리 지수 (Risk Disparity Index)',
                data: data.map(d => d['괴리지수']),
                borderColor: '#b91c1c', // Red
                backgroundColor: 'rgba(185, 28, 28, 0.1)',
                tension: 0.3,
                fill: true,
                pointRadius: 5,
            },
            {
                label: '기준 임계치 (Threshold 1.0)',
                data: Array(data.length).fill(1.0),
                borderColor: '#f59e0b', // Yellow/Gold
                borderDash: [5, 5],
                pointRadius: 0,
                fill: false,
            }
        ]
    };

    const options = {
        responsive: true,
        plugins: {
            legend: { position: 'top' },
            title: { display: true, text: '시간 흐름에 따른 구조적 위험 괴리 추이' },
        },
        scales: {
            y: {
                min: 0,
                max: 2.5, // 적정 최대 범위 설정
                title: { display: true, text: '지수 값' }
            }
        }
    };

    // 3. 렌더링 로직
    return (
        <div className={`${styles.dashboard} max-w-6xl mx-auto`}>
            <h2 className={styles.title}>⚡ 오메가 위험 괴리 지수 대시보드</h2>
            
            {/* 🚨 최상단 경고 배너 (가장 중요) */}
            <div className={`${styles.warningBox} ${warningClass} mb-8`}>
                <h3 className="text-xl font-extrabold tracking-wider">
                    🚨 현재 위험 수준: {riskLevel
