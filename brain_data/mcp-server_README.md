# MacroMicro MCP Server - Official Documentation

## Overview

The MacroMicro MCP Server provides Claude with real-time access to MacroMicro, a comprehensive financial and economic data analysis platform. This enables Claude to answer questions about economic indicators, market trends, and financial data with up-to-date information and professional-grade analysis.

**Server Name**: MacroMicro MCP Server
**Version**: 1.0
**Protocol**: MCP (Model Context Protocol)
**Transport**: HTTP (Streamable HTTP)
**Deployment**: AWS Lambda (Python 3.13)

## What is MacroMicro?

MacroMicro is a financial data analysis platform that provides:
- Real-time economic indicators and market data
- Cross-country economic comparisons
- Historical financial data analysis
- Market trend visualizations and insights
- Professional-grade financial research tools

## Capabilities

### Tool: `ask_MacroMicro`

**Description**: Send natural language questions about financial and economic data to the MacroMicro platform.

**Parameters**:
- `question` (string, required): A natural language question about financial markets, economic indicators, or data analysis

**Returns**: A markdown-formatted response containing:
- Direct answers to the question
- Relevant data points and statistics
- Charts and visualizations (as markdown)
- Historical context and analysis
- Data sources and references

**Response Time**: Queries typically take 40-60 seconds as the platform performs comprehensive data analysis and chart generation.

### Example Use Cases

1. **Economic Analysis**
   - "What's the current trend in US inflation rates compared to historical averages?"
   - "How does China's GDP growth compare to other major economies?"

2. **Market Research**
   - "What are the recent trends in global semiconductor demand?"
   - "How has the Federal Reserve's interest rate policy affected bond yields?"

3. **Investment Insights**
   - "What's the correlation between oil prices and energy sector performance?"
   - "Show me the historical volatility of the S&P 500 during recession periods"

4. **Comparative Analysis**
   - "Compare unemployment rates across G7 countries over the past 5 years"
   - "What's the relationship between housing prices and interest rates?"

## Target Users

This MCP server is designed for:
- **Financial Analysts**: Professionals needing quick access to economic data and trends
- **Investors**: Individual and institutional investors researching market conditions
- **Economists**: Researchers analyzing macroeconomic indicators
- **Business Leaders**: Executives making data-driven strategic decisions
- **Students & Educators**: Those learning about economics and financial markets

## Setup Instructions

Go to [Claude.ai/settings/connectors](https://claude.ai/settings/connectors)

## Security & Privacy

### Data Handling
- **No Data Storage**: The server does not store any user queries or responses
- **Stateless Design**: Each request is independent with no session state
- **Direct Proxy**: Questions are forwarded directly to MacroMicro API; responses are returned as-is
- **No Logging of Content**: Only system-level logs (timestamps, success/failure) are maintained

### API Security
- **Environment Variables**: API credentials are stored securely as Lambda environment variables
- **HTTPS Only**: All communications use encrypted HTTPS connections
- **Request Timeout**: 90-second timeout prevents hanging connections
- **Error Handling**: Sensitive error details are not exposed to end users

### Privacy Considerations
- User questions are sent to MacroMicro for processing
- MacroMicro may have its own data retention policies
- No personally identifiable information (PII) is collected by this server
- Recommend reviewing MacroMicro's privacy policy with end users

## Technical Architecture

### Components
1. **FastMCP Framework**: Provides MCP protocol implementation
2. **AWS Lambda**: Serverless compute platform for scalability
3. **Python 3.13**: Modern Python runtime with improved performance
4. **Uvicorn/ASGI**: High-performance async HTTP server
5. **Requests Library**: HTTP client for MacroMicro API integration

### Request Flow
```
Claude Client → MCP Protocol → AWS Lambda (this server) → MacroMicro API
                                        ↓
Claude Client ← Markdown Response ← AWS Lambda ← MacroMicro API
```

### Response Format
All responses from MacroMicro are in markdown format and may contain:
- Text explanations and analysis
- Embedded chart references
- Tables of data
- Bullet-point summaries
- Data source citations

**Important**: The markdown formatting should be preserved and rendered by the client for optimal user experience.

## Error Handling

The server handles common error scenarios gracefully:

1. **Timeout Errors**: If MacroMicro takes >90 seconds, returns user-friendly timeout message
2. **API Unavailable**: If MacroMicro is down, returns error without exposing internal details
3. **Invalid Requests**: Validates input and returns clear error messages
4. **Configuration Errors**: Checks for required environment variables on startup

## Performance

- **Cold Start**: ~2-3 seconds (Lambda container initialization)
- **Warm Request**: <100ms (server processing only)
- **MacroMicro Query**: 40-50 seconds (data analysis and chart generation)
- **Total Response Time**: 40-60 seconds typical

## Limitations

1. **Query Complexity**: Very complex queries may timeout at 90 seconds
2. **Rate Limiting**: Subject to MacroMicro API rate limits (if any)
3. **Data Currency**: Data freshness depends on MacroMicro's update schedule
4. **Language**: Currently supports English language queries
5. **Geographic Data**: Focus on major economies and markets

## Support & Maintenance

- **Source Code**: Available on GitHub (provide link)
- **Issues**: Report via GitHub Issues
- **Updates**: Server is stateless; updates require Lambda function redeployment
- **Monitoring**: CloudWatch logs available for administrators

## License & Attribution

This MCP server is built using:
- **FastMCP**: Open-source MCP framework (MIT License)
- **AWS Lambda**: Amazon Web Services serverless platform
- **MacroMicro**: Financial data platform (separate license/subscription required)

## Changelog

### Version 1.0 (Current)
- Initial release
- Single tool: `ask_MacroMicro`
- AWS Lambda deployment
- HTTP transport with stateless mode
- 90-second timeout for long-running queries

## Contact

For questions about:
- **Technical Issues**: phil@macromicro.me
- **General Issues**: support@macromicro.me

---

*This server is designed to integrate financial data capabilities into Claude, enabling users to get real-time, professional-grade economic and market analysis through natural language conversations.*
