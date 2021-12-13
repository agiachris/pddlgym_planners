# Planner Interface for [PDDLGym](https://github.com/tomsilver/pddlgym)

**This library is under development by [Tom Silver](http://web.mit.edu/tslvr/www/) and [Rohan Chitnis](https://rohanchitnis.com/). Correspondence: <tslvr@mit.edu> and <ronuchit@mit.edu>.**

This is a lightweight Python interface for using off-the-shelf classical planners like [FastForward](https://fai.cs.uni-saarland.de/hoffmann/ff.html) and [FastDownward](http://www.fast-downward.org/ObtainingAndRunningFastDownward) with [PDDLGym](https://github.com/tomsilver/pddlgym).

**Extensions to this library** have been made by [Mohamed Khodeir](https://github.com/Khodeir) and [Christopher Agia](https://agiachris.github.io/) to support a wider range of satisficing and optimal symbolic planners encapsulated in a pip-installable package.

## System Requirements

This repository has been mostly tested on MacOS Mojave and Catalina with Python 3.6. We would like to make it accessible on more systems; please let us know if you try another and run into any issues.

## Installation

1. Install [PDDLGym](https://github.com/tomsilver/pddlgym).
2. If on MacOS, `brew install coreutils`.
3. Install docker.
4. Clone this repository.

## Example Usage

**Important Note:** When you invoke a planner for the first time, the respective external package will be installed automatically. This will take up to a few minutes. This step will be skipped the next time you run the same planner.

```python
import pddlgym
from pddlgym_planners.ff import FF  # FastForward
from pddlgym_planners.fd import FD  # FastDownward

# Planning with FastForward
ff_planner = FF()
env = pddlgym.make("PDDLEnvBlocks-v0")
state, _ = env.reset()
print("Plan:", ff_planner(env.domain, state))
print("Statistics:", ff_planner.get_statistics())

# Planning with FastDownward (--alias seq-opt-lmcut)
fd_planner = FD()
env = pddlgym.make("PDDLEnvBlocks-v0")
state, _ = env.reset()
print("Plan:", fd_planner(env.domain, state))
print("Statistics:", fd_planner.get_statistics())

# Planning with FastDownward (--alias lama-first)
lama_first_planner = FD(alias_flag="--alias lama-first")
env = pddlgym.make("PDDLEnvBlocks-v0")
state, _ = env.reset()
print("Plan:", lama_first_planner(env.domain, state))
print("Statistics:", lama_first_planner.get_statistics())
```

## Extended Usage

Upon importing this package in your python script, you'll simple access to both satisficing and optimal planners through the `pddlgym_planners.PlannerHandler` object; a dictionary returning a planner (after auto-installing it) given the specified planner key name. We provide an example below:

```python 
# pyexample.py script

import pddlgym
import pddlgym_planners

# Instantiate planner handler (dict)
planners = pddlgym_planners.PlannerHandler()

# Planning with Cerberus-agl (satisficing)
cerberus_planner = planners["Cerberus-agl"]
env = pddlgym.make("PDDLEnvBlocks-v0")
state, _ = env.reset()
print("Plan:", cerberus_planner(env.domain, state))
print("Statistics:", cerberus_planner.get_statistics())

# Planning with Delfi (optimal)
delfi_planner = planners["Delfi"]
env = pddlgym.make("PDDLEnvBlocks-v0")
state, _ = env.reset()
print("Plan:", delfi_planner(env.domain, state))
print("Statistics:", delfi_planner.get_statistics())
```

Please refer to [pddlgym_planners/__init__,py](https://github.com/agiachris/pddlgym_planners/blob/master/pddlgym_planners/__init__.py) for the names of possible planners to choose from.
