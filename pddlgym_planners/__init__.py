import pddlgym

from .ff import FF
from .ffx import FFX
from .fd import FD
from .cerberus import Cerberus
from .decstar import DecStar
from .delfi import Delfi
from .lapkt import LAPKTBFWS
from .satplan import SATPlan
# from lifted import Lifted # not yet open-sourced


PLANNERS = globals()

SATISFICING = {
    "FF": {
        "planner": FF,
        "planner_kwargs": {}
    },
    "FF-X": {
        "planner": FFX,
        "planner_kwargs": {}
    },
    "FD": {
        "planner": FD,
        "planner_kwargs": {"alias_flag": "--alias lama-first"}
    },
    "Cerberus-sat": {
        "planner": Cerberus,
        "planner_kwargs": {"alias": "seq-sat-cerberus2018"}
    },
    "Cerberus-agl": {
        "planner": Cerberus,
        "planner_kwargs": {"alias": "seq-agl-cerberus2018"}
    },
    "DecStar-agl": {
        "planner": DecStar,
        "planner_kwargs": {"alias": "agl-decoupled-fallback"}
    },
    "bfws": {
        "planner": LAPKTBFWS,
        "planner_kwargs": {}
    },
    # "lifted": {
    #     "planner": Lifted,
    #     "planner_kwargs": {}
    # }
}

OPTIMAL = {
    "FD-opt": {
        "planner": FD,
        "planner_kwargs": {"alias_flag": "--alias seq-opt-lmcut"}
    },
    # "SatPlan": {
    #     "planner": SATPlan,
    #     "planner_kwargs": {}
    # },
    "Delfi": {
        "planner": Delfi,
        "planner_kwargs": {}
    },
    "DecStar-opt": {
        "planner": DecStar,
        "planner_kwargs": {"alias": "opt-decoupled-fallback"}
    }
}


def get_planner(name, **kwargs):
    try:
        planner = PLANNERS[name](**kwargs)
    except:
        raise ValueError("Specified planner {} (alias {}) is not supported".format(name, kwargs))
    return planner
      

class PlannerHandler(dict):

    def __init__(self):        
        """Simplifies access to supported planners.
        """
        for k, v in SATISFICING.items():
            data = v.copy()
            data["planner_type"] = "satisficing"
            super().__setitem__(k, data)

        for k, v in OPTIMAL.items():
            data = v.copy()
            data["planner_type"] = "optimal"
            super().__setitem__(k, data)

    def __getitem__(self, k):
        """Get planner by name.
        """
        try:
            print("[PlannerHandler] Fetching planner {}".format(k))
            v = super().__getitem__(k)
        except:
            raise KeyError("[PlannerHandler] Planner {} is not supported".format(k))
        return v["planner"](**v["planner_kwargs"])

    def get_planner_type(self, type):
        """Get planners of specified type: optimal, satsificing.
        """
        assert type in ["satisficing", "optimal"]
        planners = [(k, self.__getitem__(k)) for k, v in self.items() if v["planner_type"] == type]
        return planners
