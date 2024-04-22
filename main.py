from dotenv import load_dotenv
from crewai import Crew
from task import MeetingPrepTasks
from agents import MeetingPrepAgent

# export LANGCHAIN_TRACING_V2=true
# export LANGCHAIN_API_KEY=<your-api-key>
#
# # The below examples use the OpenAI API, though it's not necessary in general
# export OPENAI_API_KEY=<your-openai-api-key>

def main():
    print("----------------------------------------")

    load_dotenv()
    meeting_participants = input("What are the emails for the participants (rather than you) in the meeting?")
    meeting_context = input("What is the context of the meeting \n")
    meeting_objective = input("what is your objective for this meeting\n")

    tasks = MeetingPrepTasks()
    agents = MeetingPrepAgent()

    #agents
    research_agents = agents.research_agent()
    industry_analysis_agent = agents.industry_analysis_agent()
    meeting_strategy_agent = agents.meeting_strategy_agent()
    summary_and_briefing_agent = agents.summary_and_briefing_agent()

    # create task

    research_task = tasks.research_task(research_agents, meeting_participants, meeting_context)
    industry_analysis_task = tasks.industry_analysis_task(industry_analysis_agent,meeting_participants, meeting_context)
    meeting_strategy_task = tasks.meeting_strategy_task(meeting_strategy_agent, meeting_context, meeting_objective)
    summary_and_briefing_task = tasks.summary_and_briefing_task(summary_and_briefing_agent, meeting_context, meeting_objective)

    meeting_strategy_task.context = [research_task, industry_analysis_task]

    summary_and_briefing_task.context = [research_task, industry_analysis_task, meeting_strategy_task]

    crew = Crew(
        agents = [
            research_agents,
            industry_analysis_agent,
            meeting_strategy_agent,
            summary_and_briefing_agent
        ],
        tasks = [
            research_task,
            industry_analysis_task,
            meeting_strategy_task,
            summary_and_briefing_task
        ]
    )

    result = crew.kickoff()
    print(result)




if __name__ == '__main__':
    main()