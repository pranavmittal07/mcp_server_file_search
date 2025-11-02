from fastmcp import FastMCP

app = FastMCP()

@app.tool
def search_keyword(file: str, keyword: str):
    with open(file, "r") as f:
        lines = f.readlines()
    results = []
    for i, line in enumerate(lines):
        start = line.find(keyword)
        if start != -1:
            results.append({
                "line": i + 1,          # human readable line (1-based)
                "index": start,         # character index (0-based)
                "text": line.strip()    # the line content
            })

    return {"results": results}


if __name__ == "__main__":
    app.run()
