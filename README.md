# MCP Keyword Search Tool (Python + fastmcp)

This project implements an **MCP Server** using `fastmcp` which searches for a specific keyword inside a file and returns:

- the exact line number
- the character index where the keyword is found
- the line text

### ✅ Features
- fast & lightweight MCP tool
- returns keyword match positions instead of whole content
- tested using **MCP Inspector**

---

## 📦 Setup Instructions

### 1) Create Virtual Environment

```bash
python -m venv myenv
```

### 2) Activate Virtual Environment

```bash
./myenv/Scripts/activate
```
### 3) Install Dependencies

```bash
pip install fastmcp
```

Running MCP Inspector and Server
```bash
npx @modelcontextprotocol/inspector
```







