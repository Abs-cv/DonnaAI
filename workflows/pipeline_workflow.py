from workflows.router import router
from langgraph.graph import StateGraph, END
from agents.planner_agent import create_planner_agent
from agents.data_analysis_agent import create_data_analysis_agent
from agents.reporting_agent import create_reporting_agent

def create_pipeline(task_type, dataset_paths, user_test_prompt, additional_info):
    """Builds and configures the multi-agent pipeline workflow."""
    workflow = StateGraph()

    # Add agents to the workflow
    planner_agent = create_planner_agent()
    data_analysis_agent = create_data_analysis_agent()
    reporting_agent = create_reporting_agent()

    workflow.add_node("Planner", planner_agent)
    workflow.add_node("DataAnalyst", data_analysis_agent)
    workflow.add_node("Reporter", reporting_agent)

    # Add routing logic
    workflow.add_conditional_edges("Planner", router, {
        "continue": "DataAnalyst", "call_tool": "call_tool", "__end__": END,
    })
    workflow.add_conditional_edges("DataAnalyst", router, {
        "continue": "Reporter", "call_tool": "call_tool", "__end__": END,
    })
    workflow.set_entry_point("Planner")

    return workflow
