from diagrams import Diagram, Cluster
from diagrams.programming.flowchart import StartEnd, Process, Decision

# Save the flowchart as a PNG
with Diagram("Data Analysis Flowchart", show=False, direction="TB", filename="output/flowchart", outformat="png"):
    start = StartEnd("Start")
    cleaning = Process("Data Cleaning")
    processing = Process("Data Processing")
    visualization = Process("Data Visualization")
    analysis = Process("Data Analysis")
    end = StartEnd("End")

    # Define the flow
    start >> cleaning >> processing >> analysis >> visualization >> end
