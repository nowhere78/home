#!/usr/bin/env python3
"""
Karpathy Interview Analyzer
Extracts insights from Andrej Karpathy's interviews
"""

import json
import re
from typing import Dict, List
from dataclasses import dataclass
from datetime import datetime


@dataclass
class InterviewInsight:
    """Represents a single insight from an interview"""
    topic: str
    content: str
    timestamp: str = ""
    source: str = ""
    tags: List[str] = None

    def __post_init__(self):
        if self.tags is None:
            self.tags = []

    def to_dict(self) -> Dict:
        return {
            "topic": self.topic,
            "content": self.content,
            "timestamp": self.timestamp,
            "source": self.source,
            "tags": self.tags
        }


class KarpathyInterviewAnalyzer:
    """Analyzes Karpathy interview content and extracts insights"""

    # Core topics Karpathy frequently discusses
    CORE_TOPICS = {
        "llm": ["LLM", "language model", "GPT", "transformer"],
        "autonomous_driving": ["Tesla", "self-driving", "autonomous", "FSD"],
        "neural_networks": ["neural networks", "deep learning", "CNN", "backpropagation"],
        "ai_education": ["learning", "education", "tutorial", "course", "training"],
        "safety": ["safety", "alignment", "interpretability", "bias"],
        "reasoning": ["reasoning", "thinking", "planning", "agent"],
        "multimodal": ["vision", "image", "video", "multimodal", "cross-modal"],
    }

    def __init__(self):
        self.insights: List[InterviewInsight] = []
        self.topics_mentioned: Dict[str, int] = {topic: 0 for topic in self.CORE_TOPICS}

    def extract_topics(self, text: str) -> List[str]:
        """Extract topics from text based on keywords"""
        found_topics = []
        text_lower = text.lower()

        for topic, keywords in self.CORE_TOPICS.items():
            for keyword in keywords:
                if keyword.lower() in text_lower:
                    if topic not in found_topics:
                        found_topics.append(topic)
                    self.topics_mentioned[topic] += 1
                    break

        return found_topics

    def add_insight(self, topic: str, content: str, source: str = "",
                   timestamp: str = "", tags: List[str] = None) -> None:
        """Add a single insight"""
        if tags is None:
            tags = self.extract_topics(content)

        insight = InterviewInsight(
            topic=topic,
            content=content,
            timestamp=timestamp,
            source=source,
            tags=tags
        )
        self.insights.append(insight)

    def analyze_text(self, text: str, source: str = "Unknown") -> Dict:
        """Analyze interview transcript or description"""
        result = {
            "source": source,
            "total_insights_found": 0,
            "topics_identified": [],
            "key_quotes": [],
            "summary": ""
        }

        # Extract sentences
        sentences = re.split(r'[.!?]+', text)

        # Find key sentences (insights)
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) > 20:  # Filter very short sentences
                topics = self.extract_topics(sentence)
                if topics:
                    self.add_insight(
                        topic=topics[0],
                        content=sentence,
                        source=source,
                        tags=topics
                    )

        result["total_insights_found"] = len(self.insights)
        result["topics_identified"] = list(set([t for insight in self.insights for t in insight.tags]))

        return result

    def get_insights_by_topic(self, topic: str) -> List[InterviewInsight]:
        """Get all insights for a specific topic"""
        return [insight for insight in self.insights if topic in insight.tags]

    def get_summary(self) -> Dict:
        """Get summary of all insights"""
        return {
            "total_insights": len(self.insights),
            "topics_mentioned": self.topics_mentioned,
            "most_discussed": max(self.topics_mentioned, key=self.topics_mentioned.get),
            "sources": list(set([insight.source for insight in self.insights])),
            "all_tags": list(set([tag for insight in self.insights for tag in insight.tags]))
        }

    def export_json(self, filepath: str) -> None:
        """Export all insights to JSON"""
        data = {
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "total_insights": len(self.insights),
                "topics_summary": self.get_summary()
            },
            "insights": [insight.to_dict() for insight in self.insights]
        }

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def export_markdown(self, filepath: str) -> None:
        """Export insights to Markdown format"""
        output = []
        output.append("# Karpathy Interview Insights\n")
        output.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        output.append(f"Total Insights: {len(self.insights)}\n\n")

        # Summary section
        summary = self.get_summary()
        output.append("## Summary\n")
        output.append(f"- Most discussed topic: {summary['most_discussed']}\n")
        output.append(f"- Topics identified: {', '.join(summary['all_tags'])}\n\n")

        # By topic
        output.append("## Insights by Topic\n\n")
        for topic in sorted(set([tag for insight in self.insights for tag in insight.tags])):
            insights_for_topic = self.get_insights_by_topic(topic)
            output.append(f"### {topic.replace('_', ' ').title()}\n")
            output.append(f"*{len(insights_for_topic)} insights*\n\n")

            for insight in insights_for_topic[:3]:  # Show top 3 per topic
                output.append(f"- **{insight.topic}**: {insight.content[:100]}...\n")
                if insight.source:
                    output.append(f"  - Source: {insight.source}\n")
            output.append("\n")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(output)


def demo_analysis():
    """Demo the analyzer with sample interview content"""
    analyzer = KarpathyInterviewAnalyzer()

    # Sample insights from various Karpathy interviews
    sample_insights = [
        (
            "Neural Networks Foundation",
            "Neural networks are not magic, they're just mathematical functions that we optimize through backpropagation",
            "Neural Networks Zero to Hero"
        ),
        (
            "Tesla Autonomy Approach",
            "We use real-world data from Tesla fleet to train end-to-end neural networks for autonomous driving",
            "Tesla AI Day 2021"
        ),
        (
            "LLM Capabilities & Limitations",
            "LLMs are incredible at pattern recognition but they lack true reasoning and world modeling",
            "Lex Fridman Podcast"
        ),
        (
            "AI Education",
            "The best way to learn AI is to build projects, start simple and iterate",
            "Various Interviews"
        ),
        (
            "Multimodal Future",
            "The next wave of AI will integrate vision, language, and reasoning capabilities",
            "AI Conference 2024"
        ),
        (
            "Safety and Interpretability",
            "We need better interpretability tools to understand what large models are doing",
            "AI Safety Discussion"
        ),
    ]

    for topic, content, source in sample_insights:
        analyzer.add_insight(topic, content, source=source)

    return analyzer


if __name__ == "__main__":
    # Demo run
    print("🚀 Karpathy Interview Analyzer")
    print("=" * 50)

    analyzer = demo_analysis()

    # Print summary
    summary = analyzer.get_summary()
    print("\n📊 Analysis Summary:")
    print(f"Total Insights: {summary['total_insights']}")
    print(f"Topics: {summary['all_tags']}")
    print(f"Most Discussed: {summary['most_discussed']}")

    # Export results
    analyzer.export_json("karpathy_insights.json")
    analyzer.export_markdown("karpathy_insights.md")

    print("\n✅ Analysis complete!")
    print("📁 Files generated:")
    print("  - karpathy_insights.json")
    print("  - karpathy_insights.md")
