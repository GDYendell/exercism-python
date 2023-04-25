"""Functions which helps the locomotive engineer to keep track of the train."""

from typing import Dict, List, Tuple


def get_list_of_wagons(*wagons: int) -> List[int]:
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagons)


def fix_list_of_wagons(each_wagons_id: List[int], missing_wagons: List[int]):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    end1, end2, front, *rest = each_wagons_id
    return [front, *missing_wagons, *rest, end1, end2]


def add_missing_stops(route: Dict[str, str], **stops: Dict[str, str]) -> Dict[str, str]:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    return dict(**route, stops=list(stops.values()))


def extend_route_information(
    route: Dict[str, str], more_route_information: Dict[str, str]
) -> Dict[str, str]:
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return dict(**route, **more_route_information)


def fix_wagon_depot(
    wagons_rows: List[List[Tuple[int, str]]]
) -> List[List[Tuple[int, str]]]:
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    return [list(flipped_column) for flipped_column in zip(*wagons_rows)]
