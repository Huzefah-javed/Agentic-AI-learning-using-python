from typing import TypedDict, Literal, Callable, Any
# from collections.abc import Callable

# TASK 1
ExecutionResult = TypedDict("ExecutionResult", {
    "tool_name": str,
    "status": str,
    "payload": Any,
    
    "error_message": str | None ,
}) 
# TASK 2
AllowedTools = Literal["web_search", "sql_query", "python_interpreter"]

# TASK 3
ToolRunner = Callable[[ str, dict[str, Any]], None ]

def hii(greet, data):
    print(f"{greet} {data.get('name')}")

def dummy(func: ToolRunner)->None:
    func("hello", {"name":"huzefa"})
    pass

dummy(hii)

def process_tool_request(
    tool: AllowedTools,     
    params: dict[str, str | int | None],      
    runner: ToolRunner | None,     
    history: list[str],    
) -> ExecutionResult:
    
    return {
        "tool":tool,     
"params":params,      
          "runner": runner,     
           "history": history
    }
