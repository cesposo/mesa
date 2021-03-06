import random

from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from basic.model import Walker, ShapesModel


def agent_draw(agent):
    portrayal = None
    if agent is None:
        # Actually this if part is unnecessary, but still keeping it for
        # aesthetics
        pass
    elif isinstance(agent, Walker):
        print("Uid: {0}, Heading: {1}".format(agent.unique_id, agent.heading))
        portrayal = {"Shape": "arrowHead",
                     "Filled": "true",
                     "Layer": 2,
                     "Color": "green",
                     "Filled": "true",
                     "heading0": agent.heading[0],
                     "heading1": agent.heading[1],
                     "text": agent.unique_id,
                     "text_color": "white",
                     "scale": 0.8,
                     }
    return portrayal


def launch_basic():
    width = 15
    height = 10
    num_agents = 2
    pixel_ratio = 50
    grid = CanvasGrid(agent_draw, width, height,
                      width * pixel_ratio, height * pixel_ratio)
    server = ModularServer(ShapesModel, [grid], "Basic Example",
                           num_agents, width, height)
    server.max_steps = 0
    server.port = 8888
    server.launch()

if __name__ == "__main__":
    random.seed(3)
    launch_basic()
