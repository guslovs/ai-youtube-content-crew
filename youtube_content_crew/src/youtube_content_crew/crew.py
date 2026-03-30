from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from pydantic import BaseModel
from crewai_tools import SerperDevTool


@CrewBase
class YoutubeContentCrew:
    """YoutubeContentCrew crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    class SEOPackage(BaseModel):
        titles: list[str]
        description: str
        tags: list[str]

    @agent
    def research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["research_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def fact_checker_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["fact_checker_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def script_writer_agent(self) -> Agent:
        return Agent(config=self.agents_config["script_writer_agent"], verbose=True)

    @agent
    def seo_agent(self) -> Agent:
        return Agent(config=self.agents_config["seo_agent"], verbose=True)

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config["research_task"])

    @task
    def fact_checking_task(self) -> Task:
        return Task(config=self.tasks_config["fact_checking_task"])

    @task
    def script_writing_task(self) -> Task:
        return Task(config=self.tasks_config["script_writing_task"])

    @task
    def seo_task(self) -> Task:
        return Task(
            config=self.tasks_config["seo_task"], output_pydantic=self.SEOPackage
        )

    @crew
    def crew(self) -> Crew:
        """Creates the YoutubeContentCrew crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=True,
            embedder={
                "provider": "openai", 
                "config": 
                    {"model": "text-embedding-3-small"}
            }
        )
