from dataclasses import dataclass

@dataclass
class Mine:
    hover: False
    mine: False
    nearby_mines: 0
    already_selected: False