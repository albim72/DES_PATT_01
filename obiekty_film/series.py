class SeriesPart:
    def __init__(self,series_name:str,part_number:int):
        self.series_name = series_name
        self.part_number = part_number

    def get_series_info(self):
        return f"Seria: {self.series_name}, częśc: {self.part_number}."
