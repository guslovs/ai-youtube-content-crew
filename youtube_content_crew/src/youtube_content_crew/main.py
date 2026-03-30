#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from youtube_content_crew.crew import YoutubeContentCrew
from dotenv import load_dotenv

load_dotenv(override=True)

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Why AI Agents Will Replace Traditional Software in the Next 5 Years'
    }

    result = YoutubeContentCrew().crew().kickoff(inputs=inputs)
    print(result.raw)

if __name__ == "__main__":
    run()