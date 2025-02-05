# Autonomous_Driving

## Objective

Implementation of longitudinal control of an autonomous agent that manages traffic lights and intersections

## 1. Project setup

1. Download or clone the **Agent project** via git [this repository](https://bitbucket.org/tonegas/basic_agent_st/src/master/);
2. Install one of the following IDE: - Visual studio code (https://code.visualstudio.com/) - CLion jetbrains (https://www.jetbrains.com/clion/)
3. Follow the guide for the Agent Setup;
4. Download or clone the **simulation environment** (https://github.com/tonegas/PyDrivingSim);
5. Follow the guide for the environment setup;

### 1.1 Agent Setup

#### Window

##### Setup using visual studio:

1. Install visual studio professional (https://visualstudio.microsoft.com/it/vs/professional/)
2. Install cmake, clang and make
3. Copy from the folder lib/win_visual_studio the communication library to the folder lib/
4. Compile the agent: - In Clion:
   1. Open the folder project (in CLion: create Debug and Release profile);
   2. Select the correct compiler Visual Studio (https://www.jetbrains.com/help/clion/how-to-create-toolchain-in-clion.html)
   3. Compile the agent
5. Run the agent



### 1.2 Simulation Environment Setup

> Minimal driving simulator for testing high level and low level control, in the context of autonomous driving

#### Setup on windows

1. Follow the visual studio code guide for setup python on windows (up to the "Install and use packages" section)
2. Execute:
   - Go the project folder
   - Create the virtual env: `py -3 -m venv .venv`
   - enable the environment: `. .venv\scripts\activate`
   - Install packages: `pip install -r requirements.txt`
3. Open the file simulator.py
4. Run the simulator: `python simulator.py`

