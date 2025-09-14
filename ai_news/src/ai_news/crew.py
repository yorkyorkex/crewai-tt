from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileWriterTool
from typing import List
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class AiNews():
	"""AiNews crew"""

	agents: List[BaseAgent]
	tasks: List[Task]

	def __init__(self):
		super().__init__()
		self.ollama_llm = LLM(model="ollama/llama3.2:1b", base_url="http://localhost:11434")

	@agent
	def retrieve_news(self) -> Agent:
		return Agent(
			config=self.agents_config['retrieve_news'], # type: ignore[index]
			tools=[SerperDevTool()],
			verbose=True,
			llm=self.ollama_llm
		)

	@agent
	def website_scraper(self) -> Agent:
		return Agent(
			config=self.agents_config['website_scraper'], # type: ignore[index]
			tools=[ScrapeWebsiteTool()],
			verbose=True,
			llm=self.ollama_llm
		)
	
	@agent
	def ai_news_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['ai_news_writer'], # type: ignore[index]
			tools=[],
			verbose=True,
			llm=self.ollama_llm
		)
	
	@agent
	def file_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['file_writer'], # type: ignore[index]
			tools=[FileWriterTool()],
			verbose=True,
			llm=self.ollama_llm
		)

	@task
	def retrieve_news_task(self) -> Task:
		return Task(
			config=self.tasks_config['retrieve_news_task'], # type: ignore[index]
		)

	@task
	def website_scrape_task(self) -> Task:
		return Task(
			config=self.tasks_config['website_scrape_task'], # type: ignore[index]
		)
	
	@task
	def ai_news_write_task(self) -> Task:
		return Task(
			config=self.tasks_config['ai_news_write_task'], # type: ignore[index]
		)
	
	@task
	def file_write_task(self) -> Task:
		return Task(
			config=self.tasks_config['file_write_task'], # type: ignore[index]
			output_file='news/{date}_news_article.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the AiNews crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)