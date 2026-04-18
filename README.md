<div align="center" class="text-center">
<img src="images\background_mcp.png" alt="AI Agents Playground Banner" width="100%">

<!-- <h1>MCP-PLAYGROUND</h1> -->
<!-- <p><em>Exploring and learning through MCP projects. This repository is a hands-on space for understanding how Model Context Protocol servers, clients, tools, resources, and prompts work in practice.</em></p> -->

<img alt="last-commit" src="https://img.shields.io/github/last-commit/jlopezsa/ai-agents-playground?style=flat&amp;logo=git&amp;logoColor=white&amp;color=0080ff" class="inline-block mx-1" style="margin: 0px 2px;">
<img alt="repo-top-language" src="https://img.shields.io/github/languages/top/jlopezsa/ai-agents-playground?style=flat&amp;color=0080ff" class="inline-block mx-1" style="margin: 0px 2px;">
<img alt="repo-language-count" src="https://img.shields.io/github/languages/count/jlopezsa/ai-agents-playground?style=flat&amp;color=0080ff" class="inline-block mx-1" style="margin: 0px 2px;">
<p><em>Proyectos creados utilizando las herramientas y tecnologías, entre otras, que se mencionan a continuación:</em></p>


<img alt="MCP" src="https://img.shields.io/badge/MCP-Model_Context_Protocol-0A7E8C?style=flat" style="margin: 0px 2px;">
<img alt="MCP Server" src="https://img.shields.io/badge/MCP-Server-1F6FEB?style=flat" style="margin: 0px 2px;">
<img alt="MCP Client" src="https://img.shields.io/badge/MCP-Client-2EA043?style=flat" style="margin: 0px 2px;">
<img alt="Python" src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&amp;logo=Python&amp;logoColor=white" class="inline-block mx-1" style="margin: 0px 2px;">

<img alt="Markdown" src="https://img.shields.io/badge/Markdown-000000.svg?style=flat&amp;logo=Markdown&amp;logoColor=white" class="inline-block mx-1" style="margin: 0px 2px;">

<div align="center" class="text-center"><h4>... a work in progress</h4></div>
</div>

# Projects

This section presents an index of the MCP-based projects contained in this repository, including links to their respective implementations and documentation.

- [Project 1: Supporting Features](./mcp_playground/Chapter02/supportingFeatures/README.md)
- [Project 2: Notifications, Reports, and Updates](./mcp_playground/Chapter02/notificationsReportsUpdates/README.md)
- [Project 3: First Server](./mcp_playground/Chapter03/firstServer/README.md)

# Introduction to the Model Context Protocol (MCP)

The Model Context Protocol (MCP) is an open protocol designed to standardize communication between artificial intelligence applications and external systems that provide tools, resources, and prompts. Its primary objective is to establish a consistent and interoperable interface through which a client application, such as an AI assistant, integrated development environment, or conversational agent, may interact with a server exposing structured capabilities. By adopting JSON-RPC as its underlying message format, MCP provides a uniform framework for exchanging requests, responses, and notifications across heterogeneous implementations.

## Evolution of MCP: Older and Newer Characteristics

In earlier versions of the protocol, particularly the **November 5, 2024** specification, MCP defined two principal transport mechanisms: `stdio` and `HTTP with Server-Sent Events (SSE)`. Within this earlier model, the `stdio` transport enabled direct communication between a client and a locally executed server process through standard input and standard output streams. In contrast, HTTP+SSE supported remote communication scenarios, allowing servers not only to respond to client requests but also to stream asynchronous updates and progress notifications over network connections. This design was especially suitable for implementations requiring incremental responses and event-driven communication.

In subsequent versions of the protocol, such as the **June 18, 2025** specification, MCP retained the `stdio` transport while revising its HTTP-based communication model. Specifically, the previous `HTTP with SSE` mechanism evolved into **Streamable HTTP**, a more flexible transport abstraction intended to support both standard request-response exchanges and streaming interactions in a more generalized manner. Although SSE remains relevant as a mechanism for server-to-client streaming within HTTP-based communication, the newer specification broadens the transport model beyond the narrower earlier formulation. This evolution reflects a maturation of the protocol toward greater extensibility, interoperability, and suitability for production-oriented distributed systems.

## MCP over STDIO

The `stdio` transport continues to be a central characteristic of MCP, particularly in local execution contexts. Under this model, the client initiates the MCP server as a subprocess and exchanges JSON-RPC messages through the server’s standard input and standard output channels. This approach offers several practical advantages, including reduced implementation complexity, minimal communication overhead, and the avoidance of network configuration. Consequently, `stdio` is frequently employed in development environments, local integrations, and command-line-based workflows.

## Conceptual Significance of SSE in MCP

Server-Sent Events (SSE) occupy an important place in the conceptual development of MCP because they illustrate how the protocol supports asynchronous and streaming communication from server to client. In the earlier HTTP+SSE transport model, SSE was explicitly central to enabling progressive delivery of notifications and intermediate results. In the newer Streamable HTTP model, SSE remains relevant as one possible streaming mechanism, but it is no longer framed as the sole defining feature of the HTTP transport. This shift demonstrates the protocol’s transition from a simpler streaming-oriented design toward a broader and more adaptable communication architecture.

## Summary

From an academic and architectural perspective, the progression from older MCP specifications to newer ones demonstrates the protocol’s evolution from a lightweight integration mechanism into a more comprehensive framework for structured AI-system interoperability. Earlier versions emphasized direct local interaction and HTTP-based streaming through SSE, whereas newer versions preserve these foundational ideas while introducing a more extensible HTTP transport model. As a result, MCP now provides a stronger basis for both experimental local integrations and more sophisticated distributed AI applications.

## References
1. [Christoffer Noring] Learn Model Context Protocol with Python. (2025)
