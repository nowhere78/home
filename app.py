#!/usr/bin/env python3
"""
Karpathy Interview Analyzer - Flask Web Application
API server for serving interview insights with real-time analysis capabilities
"""

from flask import Flask, render_template_string, jsonify, request
from karpathy_interview_processor import KarpathyInterviewAnalyzer, InterviewInsight
import json
from datetime import datetime
import os

app = Flask(__name__)

# Initialize analyzer
analyzer = KarpathyInterviewAnalyzer()

# Sample data loading
def load_sample_data():
    """Load sample interview data into the analyzer"""
    sample_data = [
        {
            "topic": "Neural Networks Foundation",
            "content": "Neural networks are not magic, they're just mathematical functions that we optimize through backpropagation. Understanding the fundamentals is crucial.",
            "source": "Neural Networks Zero to Hero",
            "timestamp": "2024",
            "tags": ["neural_networks", "ai_education"]
        },
        {
            "topic": "Tesla Autonomy Approach",
            "content": "We use real-world data from Tesla fleet to train end-to-end neural networks for autonomous driving. Data quality matters more than data quantity.",
            "source": "Tesla AI Day 2021",
            "timestamp": "2021",
            "tags": ["autonomous_driving", "neural_networks"]
        },
        {
            "topic": "LLM Capabilities & Limitations",
            "content": "LLMs are incredible at pattern recognition but they lack true reasoning and world modeling. The next breakthrough will be in reasoning capabilities.",
            "source": "Lex Fridman Podcast",
            "timestamp": "2023",
            "tags": ["llm", "reasoning"]
        },
        {
            "topic": "AI Education Philosophy",
            "content": "The best way to learn AI is to build projects, start simple and iterate. Theory without practice leads to shallow understanding.",
            "source": "Various Interviews",
            "timestamp": "2024",
            "tags": ["ai_education", "learning"]
        },
        {
            "topic": "Multimodal AI Future",
            "content": "The next wave of AI will integrate vision, language, and reasoning capabilities. Multimodal models will become the standard.",
            "source": "AI Conference 2024",
            "timestamp": "2024",
            "tags": ["multimodal", "llm"]
        },
        {
            "topic": "Safety and Interpretability",
            "content": "We need better interpretability tools to understand what large models are doing. Safety and transparency are not optional.",
            "source": "AI Safety Discussion",
            "timestamp": "2024",
            "tags": ["safety", "interpretability"]
        },
        {
            "topic": "Scaling Laws and Efficiency",
            "content": "There are diminishing returns on pure scaling. We need smarter architectures and better data, not just bigger models.",
            "source": "Recent Interviews 2025",
            "timestamp": "2025",
            "tags": ["neural_networks", "reasoning"]
        },
        {
            "topic": "Real-World Applications",
            "content": "Production AI systems need robustness, latency constraints, and cost efficiency. Academic metrics don't capture real-world challenges.",
            "source": "Industry Talks",
            "timestamp": "2024",
            "tags": ["autonomous_driving", "llm"]
        }
    ]

    for item in sample_data:
        analyzer.add_insight(
            topic=item["topic"],
            content=item["content"],
            source=item["source"],
            timestamp=item["timestamp"],
            tags=item["tags"]
        )


# Routes
@app.route('/')
def index():
    """Serve the main dashboard"""
    return render_template_string(open('karpathy_dashboard.html').read())


@app.route('/api/insights', methods=['GET'])
def get_insights():
    """Get all insights with optional filtering"""
    topic_filter = request.args.get('topic', '')
    search_query = request.args.get('search', '').lower()

    filtered_insights = []

    for insight in analyzer.insights:
        # Filter by topic
        if topic_filter and topic_filter not in insight.tags:
            continue

        # Filter by search query
        if search_query and search_query not in insight.content.lower() and search_query not in insight.topic.lower():
            continue

        filtered_insights.append(insight.to_dict())

    return jsonify({
        "status": "success",
        "count": len(filtered_insights),
        "insights": filtered_insights
    })


@app.route('/api/summary', methods=['GET'])
def get_summary():
    """Get analysis summary"""
    summary = analyzer.get_summary()
    return jsonify({
        "status": "success",
        "summary": summary
    })


@app.route('/api/topics', methods=['GET'])
def get_topics():
    """Get all topics with their insight counts"""
    topics = {}

    for insight in analyzer.insights:
        for tag in insight.tags:
            if tag not in topics:
                topics[tag] = 0
            topics[tag] += 1

    return jsonify({
        "status": "success",
        "topics": topics
    })


@app.route('/api/insights/by-topic/<topic>', methods=['GET'])
def get_insights_by_topic(topic):
    """Get all insights for a specific topic"""
    insights = analyzer.get_insights_by_topic(topic)

    return jsonify({
        "status": "success",
        "topic": topic,
        "count": len(insights),
        "insights": [insight.to_dict() for insight in insights]
    })


@app.route('/api/analyze', methods=['POST'])
def analyze_text():
    """Analyze new interview transcript"""
    data = request.json

    if not data or 'text' not in data:
        return jsonify({
            "status": "error",
            "message": "Missing 'text' field"
        }), 400

    text = data['text']
    source = data.get('source', 'User Input')

    result = analyzer.analyze_text(text, source)

    return jsonify({
        "status": "success",
        "result": result,
        "insights_added": len(analyzer.insights)
    })


@app.route('/api/export/<format>', methods=['GET'])
def export_data(format):
    """Export insights in different formats"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    if format == 'json':
        filepath = f'karpathy_insights_{timestamp}.json'
        analyzer.export_json(filepath)
        with open(filepath) as f:
            data = json.load(f)
        os.remove(filepath)
        return jsonify(data)

    elif format == 'markdown':
        filepath = f'karpathy_insights_{timestamp}.md'
        analyzer.export_markdown(filepath)
        with open(filepath) as f:
            content = f.read()
        os.remove(filepath)
        return {
            "status": "success",
            "format": "markdown",
            "content": content
        }

    else:
        return jsonify({
            "status": "error",
            "message": "Unsupported format. Use 'json' or 'markdown'"
        }), 400


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get detailed statistics"""
    stats = {
        "total_insights": len(analyzer.insights),
        "unique_topics": len(set([tag for insight in analyzer.insights for tag in insight.tags])),
        "unique_sources": len(set([insight.source for insight in analyzer.insights])),
        "topics_distribution": analyzer.topics_mentioned,
        "generated_at": datetime.now().isoformat()
    }

    return jsonify({
        "status": "success",
        "stats": stats
    })


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "status": "error",
        "message": "Endpoint not found"
    }), 404


@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "status": "error",
        "message": "Internal server error"
    }), 500


if __name__ == '__main__':
    # Load sample data
    load_sample_data()

    print("\n" + "="*60)
    print("🚀 Karpathy Interview Analyzer - Starting Server")
    print("="*60)
    print(f"\n📊 Loaded {len(analyzer.insights)} insights")
    print(f"🏷️  Topics: {', '.join(analyzer.get_summary()['all_tags'])}")
    print(f"\n📍 Dashboard: http://localhost:5000")
    print(f"📡 API Docs: http://localhost:5000/api/summary")
    print("\n" + "="*60 + "\n")

    # Run Flask app
    app.run(debug=True, port=5000, host='localhost')
