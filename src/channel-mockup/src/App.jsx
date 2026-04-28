import React, { useState } from 'react';
import { Search, Menu, Mic, Bell, User, PlayCircle, MoreVertical } from 'lucide-react';

const themes = [
  {
    id: 0,
    name: "Focus 워크스페이스",
    banner: "https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?auto=format&fit=crop&w=2560&q=80",
    profile: "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=300&q=80",
    title: "Focus Cafe | 집중을 위한 로파이",
    subscribers: "구독자 24.5만명 • 동영상 128개",
    desc: "코딩, 독서, 업무에 필요한 집중력을 200% 끌어올려줄 깔끔하고 정제된 로파이 비트를 굽습니다. 당신의 생산성을 높여줄 완벽한 백그라운드 뮤직을 만나보세요.",
    featured: {
      thumb: "https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?auto=format&fit=crop&w=800&q=80",
      title: "집중력 200% 폭발하는 코딩용 로파이 플레이리스트 💻 3시간 연속재생",
      stats: "조회수 120만회 • 2개월 전",
      desc: "카페에서 노트북을 펼치고 집중할 때 가장 듣기 좋은 리듬감 있는 로파이 음악 모음입니다. 뽀모도로 타이머와 함께 일하기 좋은 템포의 비트들로 채웠습니다."
    },
    sections: [
      {
        title: "💻 카페에서 일할 때 듣는 노동요",
        videos: [
          { thumb: "https://images.unsplash.com/photo-1542831371-29b0f74f9713?auto=format&fit=crop&w=400&q=80", title: "코딩할 때 듣기 좋은 신나는 Lofi 비트", stats: "조회수 45만회 • 1주 전", duration: "1:00:00" },
          { thumb: "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=400&q=80", title: "마감 1시간 전, 미친 집중력을 위한 음악", stats: "조회수 89만회 • 3주 전", duration: "2:00:00" },
          { thumb: "https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&w=400&q=80", title: "야근을 위로하는 심야 사무실 로파이", stats: "조회수 32만회 • 1개월 전", duration: "1:30:00" },
          { thumb: "https://images.unsplash.com/photo-1497215842964-222b430dc094?auto=format&fit=crop&w=400&q=80", title: "재택근무 생산성을 높여주는 홈 오피스 브금", stats: "조회수 56만회 • 2개월 전", duration: "3:00:00" }
        ]
      }
    ]
  },
  {
    id: 1,
    name: "나른한 오후의 칠링",
    banner: "https://images.unsplash.com/photo-1497935586351-b67a49e012bf?auto=format&fit=crop&w=2560&q=80",
    profile: "https://images.unsplash.com/photo-1511920170033-f8396924c348?auto=format&fit=crop&w=300&q=80",
    title: "Chill Out | 달콤한 휴식",
    subscribers: "구독자 58.2만명 • 동영상 210개",
    desc: "바쁜 일상 속 작은 쉼표. 따스한 햇살이 비치는 소파에 누워 멍때리기 좋은 나른하고 포근한 로파이 음악을 만듭니다. 지친 하루를 달래줄 음악 한 잔 하실래요?",
    featured: {
      thumb: "https://images.unsplash.com/photo-1525310072745-f49212b5ac6d?auto=format&fit=crop&w=800&q=80",
      title: "☕ 주말 오후 3시, 소파에 누워 멍때리기 좋은 따뜻한 로파이",
      stats: "조회수 350만회 • 5개월 전",
      desc: "아무것도 하기 싫은 주말 오후, 창문으로 들어오는 햇살을 맞으며 듣기 좋은 부드럽고 잔잔한 칠아웃 로파이 믹스입니다."
    },
    sections: [
      {
        title: "🌙 하루를 마무리하며 듣는 편안한 Lofi",
        videos: [
          { thumb: "https://images.unsplash.com/photo-1515871204537-4d2d5f15afe4?auto=format&fit=crop&w=400&q=80", title: "새벽 2시, 생각 비우기 좋은 잔잔한 수면 유도 음악", stats: "조회수 120만회 • 2주 전", duration: "4:00:00" },
          { thumb: "https://images.unsplash.com/photo-1499810631641-541e76d678a2?auto=format&fit=crop&w=400&q=80", title: "샤워 후 맥주 한 캔과 듣기 좋은 몽환적인 노래", stats: "조회수 88만회 • 3주 전", duration: "1:20:00" },
          { thumb: "https://images.unsplash.com/photo-1507120410856-1f35574c3b45?auto=format&fit=crop&w=400&q=80", title: "비 오는 밤, 따뜻한 이불 속에서 듣는 로파이", stats: "조회수 210만회 • 1개월 전", duration: "2:30:00" },
          { thumb: "https://images.unsplash.com/photo-1463171379579-3fdfb86d6285?auto=format&fit=crop&w=400&q=80", title: "아무 걱정 없이 잠들고 싶을 때", stats: "조회수 150만회 • 2개월 전", duration: "3:00:00" }
        ]
      }
    ]
  },
  {
    id: 2,
    name: "모닝 브루잉 힙스터",
    banner: "https://images.unsplash.com/photo-1498654896293-37aacf113fd9?auto=format&fit=crop&w=2560&q=80",
    profile: "https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&w=300&q=80",
    title: "Morning Brewing | 에너제틱 재즈 로파이",
    subscribers: "구독자 12.8만명 • 동영상 85개",
    desc: "신선한 원두 향기와 함께 여는 상쾌한 아침! 기분 좋은 하루의 시작을 돕는 경쾌한 재즈 로파이와 트렌디한 힙합 비트를 선사합니다. 기분 전환이 필요할 때 찾아오세요.",
    featured: {
      thumb: "https://images.unsplash.com/photo-1495474472207-464a4d965d33?auto=format&fit=crop&w=800&q=80",
      title: "출근길 텐션을 높여주는 상쾌하고 그루브 있는 재즈 로파이 ☀️",
      stats: "조회수 85만회 • 1개월 전",
      desc: "커피 한 잔을 내리며 듣는 힙한 재즈 로파이 믹스. 피곤한 아침 출근길이나 드라이브할 때 틀어놓으면 기분이 한결 산뜻해집니다."
    },
    sections: [
      {
        title: "☀️ 기분 좋은 하루의 시작, 모닝 플레이리스트",
        videos: [
          { thumb: "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&w=400&q=80", title: "주말 아침, 브런치 먹으며 듣는 기분 좋은 음악", stats: "조회수 62만회 • 1주 전", duration: "1:00:00" },
          { thumb: "https://images.unsplash.com/photo-1497935586351-b67a49e012bf?auto=format&fit=crop&w=400&q=80", title: "햇살 가득한 창가에서 내리는 커피 한 잔", stats: "조회수 45만회 • 3주 전", duration: "1:30:00" },
          { thumb: "https://images.unsplash.com/photo-1481833759220-07e3d4d5e714?auto=format&fit=crop&w=400&q=80", title: "드라이브 할 때 듣는 리드미컬 칠아웃 비트", stats: "조회수 98만회 • 1개월 전", duration: "2:00:00" },
          { thumb: "https://images.unsplash.com/photo-1501339817348-13c01a710f60?auto=format&fit=crop&w=400&q=80", title: "봄날의 피크닉 돗자리 위에서 듣는 몽글몽글한 노래", stats: "조회수 110만회 • 2개월 전", duration: "1:45:00" }
        ]
      }
    ]
  }
];

function App() {
  const [currentTheme, setCurrentTheme] = useState(0);
  const theme = themes[currentTheme];

  return (
    <div className="app-container">
      {/* Theme Switcher */}
      <div className="theme-switcher">
        {themes.map((t, idx) => (
          <button 
            key={t.id} 
            className={`theme-btn ${currentTheme === idx ? 'active' : ''}`}
            onClick={() => setCurrentTheme(idx)}
          >
            {t.name}
          </button>
        ))}
      </div>

      {/* Top Nav */}
      <nav className="yt-nav">
        <div className="nav-left">
          <Menu size={24} />
          <div className="logo"><PlayCircle size={24} color="#ff0000" fill="#ff0000" /> YouTube</div>
        </div>
        <div className="search-bar">
          <input type="text" className="search-input" placeholder="검색" />
          <button className="search-btn"><Search size={20} /></button>
          <div style={{marginLeft: '10px', background: '#181818', borderRadius: '50%', padding: '8px'}}><Mic size={20} /></div>
        </div>
        <div className="nav-right">
          <Bell size={24} />
          <User size={24} />
        </div>
      </nav>

      {/* Channel Header */}
      <header className="channel-header">
        <div className="banner-container">
          <img src={theme.banner} alt="Channel Banner" className="banner-img" />
        </div>
        
        <div className="channel-info">
          <img src={theme.profile} alt="Profile" className="profile-pic" />
          <div className="channel-details">
            <h1 className="channel-title">{theme.title}</h1>
            <div className="channel-stats">{theme.subscribers}</div>
            <div className="channel-desc">{theme.desc}</div>
            <button className="subscribe-btn">구독</button>
          </div>
        </div>

        <div className="channel-nav">
          <div className="channel-nav-item active">홈</div>
          <div className="channel-nav-item">동영상</div>
          <div className="channel-nav-item">Shorts</div>
          <div className="channel-nav-item">라이브</div>
          <div className="channel-nav-item">재생목록</div>
          <div className="channel-nav-item">커뮤니티</div>
          <div className="channel-nav-item"><Search size={18} /></div>
        </div>
      </header>

      {/* Main Content */}
      <main className="main-content">
        {/* Featured Video */}
        <div className="featured-video">
          <img src={theme.featured.thumb} alt="Featured" className="featured-thumb" />
          <div className="featured-info">
            <h2 className="featured-title">{theme.featured.title}</h2>
            <div className="featured-stats">{theme.featured.stats}</div>
            <p className="featured-desc">{theme.featured.desc}</p>
          </div>
        </div>

        {/* Video Sections */}
        {theme.sections.map((section, sIdx) => (
          <div key={sIdx} className="video-section">
            <h3 className="section-title">{section.title}</h3>
            <div className="video-row">
              {section.videos.map((video, vIdx) => (
                <div key={vIdx} className="video-card">
                  <div className="video-thumb-container">
                    <img src={video.thumb} alt={video.title} className="video-thumb" />
                    <span className="video-duration">{video.duration}</span>
                  </div>
                  <div style={{display: 'flex', gap: '10px', marginTop: '10px'}}>
                    <div style={{flex: 1}}>
                      <h4 className="video-card-title">{video.title}</h4>
                      <div className="video-card-stats">{video.stats}</div>
                    </div>
                    <MoreVertical size={16} color="#aaa" />
                  </div>
                </div>
              ))}
            </div>
          </div>
        ))}
      </main>
    </div>
  );
}

export default App;
