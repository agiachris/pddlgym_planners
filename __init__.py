from ff import FF
from ffx import FFX
from fd import FD
from cerberus import Cerberus
from decstar import DecStar
from delfi import Delfi
from lapkt import LAPKTBFWS
from satplan import SATPlan
from lifted import Lifted


planners = globals()


def get_planner(name, alias=None):
    planner = None
    try:
        if alias is not None:
            planner = planners[name](alias)
        else:
            planner = planners[name]()
    except:
        raise ValueError("Specified planner {} (alias {}) is unsupported".format(name, alias))
    return planner


if __name__ == "__main__":
    planner = get_planner("FF")
