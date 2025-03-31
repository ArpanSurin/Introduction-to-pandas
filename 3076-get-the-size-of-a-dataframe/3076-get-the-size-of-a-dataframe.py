import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    result = pd.DataFrame(players)
    return list(players.shape)